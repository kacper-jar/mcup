import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterator

import requests

from mcup.core.config_assemblers import AssemblerLinkerConfig, AssemblerLinker
from mcup.core.status import Status, StatusCode
from mcup.core.utils.version import Version, LATEST_VERSION


class ServerHandler:
    """Class for handling server-related actions."""

    def __init__(self):
        """Initialize the server handler."""
        self.logger = logging.getLogger(__name__)

    def create(self, server_path: Path, server_type: str, server_version: str, locker_entry: dict,
               assembler_linker_config: AssemblerLinkerConfig) -> Iterator[Status]:
        """Downloads/Builds server in a specified path along with all required configuration files."""
        self.logger.info(f"Creating server: type={server_type}, version={server_version}, path={server_path}")
        self.logger.debug(f"Locker entry: {locker_entry}")

        try:
            subprocess.check_output(
                ["java", "-version"],
                stderr=subprocess.STDOUT,
                text=True
            )
            self.logger.info("Java installation verified")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            self.logger.error(f"Java is not installed or not accessible: {e}")
            yield Status(StatusCode.ERROR_JAVA_NOT_FOUND)
            return

        version = Version.from_string(server_version)

        if version > LATEST_VERSION:
            self.logger.warning(f"Server version {version} is not supported by this version of mcup - "
                                f"configuration files won't be assembled")
            yield Status(StatusCode.INFO_VERSION_NEWER_THAN_SUPPORTED)

        if not server_path.exists():
            self.logger.info(f"Creating server directory: {server_path}")
            os.makedirs(server_path)

        if locker_entry["source"] == "DOWNLOAD":
            self.logger.info(f"Downloading server from: {locker_entry['server_url']}")
            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Preparing to download server...", 1])
            response = requests.get(locker_entry["server_url"], stream=True)

            if response.status_code == 200:
                total_size = int(response.headers.get('content-length', 0))
                self.logger.debug(f"Download size: {total_size} bytes")

                if total_size > 0:
                    yield Status(StatusCode.PROGRESSBAR_NEXT, ["Downloading server...", total_size])
                    show_progress = True
                else:
                    self.logger.warning("Content-length not available, using 0% -> 100% progress")
                    yield Status(StatusCode.PROGRESSBAR_NEXT, ["Downloading server...", 1])
                    show_progress = False

                file_name = locker_entry["server_url"].split("/")[-1]
                file_path = server_path / file_name
                self.logger.debug(f"Saving to: {file_path}")
                server_jar_name = file_name
                args_instead_of_jar = False

                downloaded_bytes = 0
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        if chunk:
                            file.write(chunk)
                            chunk_size = len(chunk)
                            downloaded_bytes += chunk_size

                            if show_progress:
                                yield Status(StatusCode.PROGRESSBAR_UPDATE, chunk_size)

                self.logger.info(f"Server downloaded successfully: {downloaded_bytes} bytes")

                if not show_progress:
                    yield Status(StatusCode.PROGRESSBAR_UPDATE, 1)
            else:
                self.logger.error(f"Failed to download server: {str(response.status_code)}")
                yield Status(StatusCode.ERROR_DOWNLOAD_SERVER_FAILED, str(response.status_code))
                return

            if not os.path.exists(file_path):
                self.logger.error(f"Server jar file not found after download: {file_path}")
                yield Status(StatusCode.ERROR_SERVER_JAR_NOT_FOUND)
                return

        elif locker_entry["source"] == "INSTALLER":
            self.logger.info(f"Downloading installer from: {locker_entry['installer_url']}")
            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Preparing to download installer...", 1])
            response = requests.get(locker_entry["installer_url"], stream=True)

            if response.status_code == 200:
                total_size = int(response.headers.get('content-length', 0))
                self.logger.debug(f"Installer size: {total_size} bytes")

                if total_size > 0:
                    yield Status(StatusCode.PROGRESSBAR_NEXT, ["Downloading installer...", total_size])
                    show_progress = True
                else:
                    self.logger.warning("Content-length not available, using 0% -> 100% progress")
                    yield Status(StatusCode.PROGRESSBAR_NEXT, ["Downloading installer...", 1])
                    show_progress = False

                file_name = locker_entry["installer_url"].split("/")[-1]
                file_path = server_path / file_name
                self.logger.debug(f"Saving to: {file_path}")

                downloaded_bytes = 0
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        if chunk:
                            file.write(chunk)
                            chunk_size = len(chunk)
                            downloaded_bytes += chunk_size

                            if show_progress:
                                yield Status(StatusCode.PROGRESSBAR_UPDATE, chunk_size)

                self.logger.info(f"Server downloaded successfully: {downloaded_bytes} bytes")

                if not show_progress:
                    yield Status(StatusCode.PROGRESSBAR_UPDATE, 1)
            else:
                self.logger.error(f"Failed to download installer: {str(response.status_code)}")
                yield Status(StatusCode.ERROR_DOWNLOAD_INSTALLER_FAILED, str(response.status_code))
                return

            if not os.path.exists(file_path):
                self.logger.error(f"Installer file not found after download: {file_path}")
                yield Status(StatusCode.ERROR_INSTALLER_NOT_FOUND)
                return

            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Installing server...", 1])
            try:
                java_version_output = subprocess.check_output(
                    ["java", "-version"],
                    stderr=subprocess.STDOUT,
                    text=True
                )

                version_pattern = r'(?:java\s+version\s+|openjdk\s+version\s+|openjdk\s+)[\"\']?(\d+(?:\.\d+)*(?:_\d+)?)[\"\']?'
                match = re.search(version_pattern, java_version_output, re.IGNORECASE)

                if not match:
                    first_line = java_version_output.split('\n')[0]
                    fallback_pattern = r'[\"\'](\d+(?:\.\d+)*(?:_\d+)?)[\"\']'
                    match = re.search(fallback_pattern, first_line)

                if not match:
                    self.logger.error(f"Could not parse Java version from output: {java_version_output}")
                    yield Status(StatusCode.ERROR_JAVA_VERSION_DETECTION_FAILED, "Could not parse Java version")
                    return

                version_string = match.group(1)

                if version_string.startswith('1.'):
                    parts = version_string.split('.')
                    if len(parts) >= 2:
                        java_major_version = int(parts[1])
                    else:
                        self.logger.error(f"Unexpected Java version format: {version_string}")
                        yield Status(StatusCode.ERROR_JAVA_VERSION_DETECTION_FAILED,
                                     f"Unexpected version format: {version_string}")
                        return
                else:
                    major_version = version_string.split('.')[0]
                    java_major_version = int(major_version)

                self.logger.debug(f"Detected Java version: {java_major_version}")

            except subprocess.CalledProcessError as e:
                self.logger.error(f"Failed to execute 'java -version': {e}")
                yield Status(StatusCode.ERROR_JAVA_VERSION_DETECTION_FAILED, str(e))
                return
            except ValueError as e:
                self.logger.error(f"Failed to parse Java version number: {e}")
                yield Status(StatusCode.ERROR_JAVA_VERSION_DETECTION_FAILED, str(e))
                return

            if version >= Version(1, 20, 6) and java_major_version < 21:
                self.logger.warning(
                    f"Java 21+ recommended for Minecraft {version.get_string()}, found Java {java_major_version}")
                yield Status(StatusCode.INFO_JAVA_MINIMUM_21)
            elif version > Version(1, 17, 1) and java_major_version < 17:
                self.logger.warning(
                    f"Java 17+ recommended for Minecraft {version.get_string()}, found Java {java_major_version}")
                yield Status(StatusCode.INFO_JAVA_MINIMUM_17)
            elif version >= Version(1, 17, 0) and java_major_version < 16:
                self.logger.warning(
                    f"Java 16+ recommended for Minecraft {version.get_string()}, found Java {java_major_version}")
                yield Status(StatusCode.INFO_JAVA_MINIMUM_16)
            elif version < Version(1, 17, 0) and java_major_version < 8:
                self.logger.warning(
                    f"Java 8+ required for Minecraft {version.get_string()}, found Java {java_major_version}")
                yield Status(StatusCode.INFO_JAVA_MINIMUM_8)
            else:
                self.logger.info(
                    f"Java version {java_major_version} is compatible with Minecraft {version.get_string()}")

            installer_args = [
                file_path if arg == "%file_path"
                else version.get_string() if arg == "%version"
                else arg
                for arg in locker_entry["installer_args"]
            ]

            self.logger.info(f"Running installer with args: {installer_args}")
            subprocess.run(
                installer_args,
                cwd=server_path,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            self.logger.debug("Searching for server jar file")
            matching_files = [
                f for f in server_path.iterdir()
                if f.is_file()
                   and f.suffix == ".jar"
                   and server_type in f.name
                   and f.name != file_name
            ]

            if server_type == "forge" and version >= Version(1, 17, 1):
                args_instead_of_jar = True

                parts = file_name.split('-')
                minecraft_version = parts[1]
                forge_version = parts[2]

                match sys.platform:
                    case "linux" | "darwin":
                        server_jar_name = f"@libraries/net/minecraftforge/forge/{minecraft_version}-{forge_version}/unix_args.txt"
                    case "win32":
                        server_jar_name = f"@libraries/net/minecraftforge/forge/{minecraft_version}-{forge_version}/win_args.txt"
            elif server_type == "neoforge":
                args_instead_of_jar = True

                parts = file_name.split('-')
                neoforge_version = parts[1]

                match sys.platform:
                    case "linux" | "darwin":
                        server_jar_name = f"@libraries/net/neoforged/neoforge/{neoforge_version}/unix_args.txt"
                    case "win32":
                        server_jar_name = f"@libraries/net/neoforged/neoforge/{neoforge_version}/win_args.txt"
            else:
                args_instead_of_jar = False
                server_jar_name = matching_files[0].name
            self.logger.info(f"Found server jar: {server_jar_name}")

            if not matching_files and server_jar_name is None:
                self.logger.error(f"No server jar found after installation in {server_path}")
                self.logger.debug(
                    f"Available jar files: {[f.name for f in server_path.iterdir() if f.suffix == '.jar']}")
                yield Status(StatusCode.ERROR_SERVER_JAR_NOT_FOUND)
                return
        else:
            self.logger.error(f"Unsupported server source: {locker_entry['source']}")
            yield Status(StatusCode.ERROR_SERVER_SOURCE_NOT_SUPPORTED, locker_entry["source"])
            return

        self.logger.info(f"Server jar name: {server_jar_name}")

        yield Status(StatusCode.PROGRESSBAR_NEXT, ["Cleaning up...", 1])

        if not locker_entry["cleanup"]:
            self.logger.debug("No cleanup items specified")
        else:
            self.logger.info(f"Cleaning up {len(locker_entry['cleanup'])} items")
            for item in locker_entry["cleanup"]:
                full_path = os.path.join(server_path, item)
                if os.path.isfile(full_path):
                    os.remove(full_path)
                    self.logger.debug(f"Removed file: {item}")
                elif os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                    self.logger.debug(f"Removed directory: {item}")
                else:
                    self.logger.debug(f"Cleanup item not found: {item}")

        self.logger.info("Assembling configuration files")
        yield Status(StatusCode.PROGRESSBAR_NEXT, ["Assembling configuration files...", 1])

        config_files = assembler_linker_config.get_configuration_files()
        self.logger.debug(f"Found {len(config_files)} configuration files to process")

        for config in config_files:
            if config.config_file_name == "start.sh" or config.config_file_name == "start.bat":
                self.logger.debug(f"Setting server-jar property for {config.config_file_name}")
                config.set_configuration_property("server-jar", server_jar_name, version)
                config.set_configuration_property("server-args-instead-of-jar", args_instead_of_jar, version)

        assembler_linker = AssemblerLinker(assembler_linker_config)
        assembler_linker.link()
        assembler_linker.assemble_linked_files(server_path)

        self.logger.info("Configuration files assembled successfully")

        if version >= Version(1, 7, 10):
            self.logger.info("Creating EULA file")
            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Assembling eula.txt...", 1])
            eula_file_path = server_path / "eula.txt"
            with open(eula_file_path, "w") as file:
                file.write("# Minecraft EULA available at https://aka.ms/MinecraftEULA\n")
                file.write("eula=true")
            self.logger.debug(f"EULA file created: {eula_file_path}")
        else:
            self.logger.info("EULA file not required, creation skipped")

        yield Status(StatusCode.PROGRESSBAR_FINISH_TASK)
        yield Status(StatusCode.PROGRESSBAR_END)
        yield Status(StatusCode.SUCCESS)

        self.logger.info(f"Server creation completed successfully")
