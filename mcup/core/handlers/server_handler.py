import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterator, Tuple, Optional

import requests

from mcup.core.config_assemblers import AssemblerLinkerConfig, AssemblerLinker
from mcup.core.configs import EulaFile
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

        java_validation_status = self._validate_java_installation()
        if java_validation_status:
            yield java_validation_status
            return

        version = Version.from_string(server_version)
        self._check_version_support(version)

        self._ensure_server_directory(server_path)

        server_jar_name, args_instead_of_jar = None, False

        if locker_entry["source"] == "DOWNLOAD":
            yield from self._handle_download_source(server_path, locker_entry)
            server_jar_name = locker_entry["server_url"].split("/")[-1]
            args_instead_of_jar = False
        elif locker_entry["source"] == "INSTALLER":
            result = yield from self._handle_installer_source(server_path, server_type, locker_entry, version)
            if result is None:
                return
            server_jar_name, args_instead_of_jar = result
        else:
            self.logger.error(f"Unsupported server source: {locker_entry['source']}")
            yield Status(StatusCode.ERROR_SERVER_SOURCE_NOT_SUPPORTED, locker_entry["source"])
            return

        self.logger.info(f"Server jar name: {server_jar_name}")

        yield from self._cleanup_files(server_path, locker_entry["cleanup"])
        yield from self._assemble_configuration_files(
            server_path, version, server_jar_name, args_instead_of_jar, assembler_linker_config
        )

        self.logger.info("Server creation completed successfully")

        yield Status(StatusCode.PROGRESSBAR_FINISH_TASK)
        yield Status(StatusCode.PROGRESSBAR_END)
        yield Status(StatusCode.SUCCESS)

    def _validate_java_installation(self) -> Optional[Status]:
        """Validate that Java is installed and accessible."""
        try:
            subprocess.check_output(
                ["java", "-version"],
                stderr=subprocess.STDOUT,
                text=True
            )
            self.logger.info("Java installation verified")
            return None
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            self.logger.error(f"Java is not installed or not accessible: {e}")
            return Status(StatusCode.ERROR_JAVA_NOT_FOUND)

    def _check_version_support(self, version: Version) -> None:
        """Check if the server version is supported."""
        if version > LATEST_VERSION:
            self.logger.warning(f"Server version {version} is not supported by this version of mcup - "
                                f"configuration files won't be assembled")

    def _ensure_server_directory(self, server_path: Path) -> None:
        """Create server directory if it doesn't exist."""
        if not server_path.exists():
            self.logger.info(f"Creating server directory: {server_path}")
            os.makedirs(server_path)

    def _handle_download_source(self, server_path: Path, locker_entry: dict) -> Iterator[Status]:
        """Handle downloading server from a direct download source."""
        self.logger.info(f"Downloading server from: {locker_entry['server_url']}")
        yield Status(StatusCode.PROGRESSBAR_NEXT, ["Preparing to download server...", 1])

        response = requests.get(locker_entry["server_url"], stream=True)

        if response.status_code != 200:
            self.logger.error(f"Failed to download server: {response.status_code}")
            yield Status(StatusCode.ERROR_DOWNLOAD_SERVER_FAILED, str(response.status_code))
            return

        file_name = locker_entry["server_url"].split("/")[-1]
        file_path = server_path / file_name

        yield from self._download_file(response, file_path, "server")

        if not file_path.exists():
            self.logger.error(f"Server jar file not found after download: {file_path}")
            yield Status(StatusCode.ERROR_SERVER_JAR_NOT_FOUND)

    def _handle_installer_source(self, server_path: Path, server_type: str, locker_entry: dict,
                                 version: Version) -> Iterator[Tuple[str, bool]]:
        """Handle downloading and running installer source."""
        self.logger.info(f"Downloading installer from: {locker_entry['installer_url']}")
        yield Status(StatusCode.PROGRESSBAR_NEXT, ["Preparing to download installer...", 1])

        response = requests.get(locker_entry["installer_url"], stream=True)

        if response.status_code != 200:
            self.logger.error(f"Failed to download installer: {response.status_code}")
            yield Status(StatusCode.ERROR_DOWNLOAD_INSTALLER_FAILED, str(response.status_code))
            yield None
            return

        file_name = locker_entry["installer_url"].split("/")[-1]
        file_path = server_path / file_name

        yield from self._download_file(response, file_path, "installer")

        if not file_path.exists():
            self.logger.error(f"Installer file not found after download: {file_path}")
            yield Status(StatusCode.ERROR_INSTALLER_NOT_FOUND)
            yield None
            return

        java_version_status = self._validate_java_version_for_minecraft(version)
        if java_version_status:
            yield java_version_status
            yield None
            return

        yield from self._run_installer(server_path, locker_entry, file_path, version)

        server_jar_name, args_instead_of_jar = self._determine_server_jar_info(
            server_path, server_type, file_name, version
        )

        if not server_jar_name:
            yield Status(StatusCode.ERROR_SERVER_JAR_NOT_FOUND)
            yield None
            return

        yield (server_jar_name, args_instead_of_jar)

    def _download_file(self, response: requests.Response, file_path: Path, file_type: str) -> Iterator[Status]:
        """Download a file with progress tracking."""
        total_size = int(response.headers.get('content-length', 0))
        self.logger.debug(f"{file_type.capitalize()} size: {total_size} bytes")

        if total_size > 0:
            yield Status(StatusCode.PROGRESSBAR_NEXT, [f"Downloading {file_type}...", total_size])
            show_progress = True
        else:
            self.logger.warning("Content-length not available, using 0% -> 100% progress")
            yield Status(StatusCode.PROGRESSBAR_NEXT, [f"Downloading {file_type}...", 1])
            show_progress = False

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

        self.logger.info(f"{file_type.capitalize()} downloaded successfully: {downloaded_bytes} bytes")

        if not show_progress:
            yield Status(StatusCode.PROGRESSBAR_UPDATE, 1)

    def _get_java_major_version(self) -> Optional[int]:
        """Get the major version of the installed Java."""
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
                return None

            version_string = match.group(1)

            if version_string.startswith('1.'):
                parts = version_string.split('.')
                if len(parts) >= 2:
                    return int(parts[1])
                else:
                    self.logger.error(f"Unexpected Java version format: {version_string}")
                    return None
            else:
                major_version = version_string.split('.')[0]
                return int(major_version)

        except (subprocess.CalledProcessError, ValueError) as e:
            self.logger.error(f"Failed to detect Java version: {e}")
            return None

    def _validate_java_version_for_minecraft(self, minecraft_version: Version) -> Optional[Status]:
        """Validate Java version compatibility with Minecraft version."""
        yield Status(StatusCode.PROGRESSBAR_NEXT, ["Installing server...", 1])

        java_major_version = self._get_java_major_version()
        if java_major_version is None:
            return Status(StatusCode.ERROR_JAVA_VERSION_DETECTION_FAILED, "Could not detect Java version")

        self.logger.debug(f"Detected Java version: {java_major_version}")

        if minecraft_version >= Version(1, 20, 6) and java_major_version < 21:
            self.logger.warning(
                f"Java 21+ recommended for Minecraft {minecraft_version.get_string()}, found Java {java_major_version}")
            return Status(StatusCode.INFO_JAVA_MINIMUM_21)
        elif minecraft_version > Version(1, 17, 1) and java_major_version < 17:
            self.logger.warning(
                f"Java 17+ recommended for Minecraft {minecraft_version.get_string()}, found Java {java_major_version}")
            return Status(StatusCode.INFO_JAVA_MINIMUM_17)
        elif minecraft_version >= Version(1, 17, 0) and java_major_version < 16:
            self.logger.warning(
                f"Java 16+ recommended for Minecraft {minecraft_version.get_string()}, found Java {java_major_version}")
            return Status(StatusCode.INFO_JAVA_MINIMUM_16)
        elif minecraft_version < Version(1, 17, 0) and java_major_version < 8:
            self.logger.warning(
                f"Java 8+ required for Minecraft {minecraft_version.get_string()}, found Java {java_major_version}")
            return Status(StatusCode.INFO_JAVA_MINIMUM_8)
        else:
            self.logger.info(
                f"Java version {java_major_version} is compatible with Minecraft {minecraft_version.get_string()}")
            return None

    def _run_installer(self, server_path: Path, locker_entry: dict, file_path: Path,
                       version: Version) -> Iterator[Status]:
        """Run the installer with appropriate arguments."""
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
        yield Status(StatusCode.PROGRESSBAR_UPDATE, 1)

    def _determine_server_jar_info(self, server_path: Path, server_type: str,
                                   installer_file_name: str, version: Version) -> Tuple[Optional[str], bool]:
        """Determine the server jar name and whether to use args instead of jar."""
        self.logger.debug("Searching for server jar file")

        if server_type == "forge" and version >= Version(1, 17, 1):
            return self._get_forge_args_file(installer_file_name), True
        elif server_type == "neoforge":
            return self._get_neoforge_args_file(installer_file_name), True
        else:
            matching_files = [
                f for f in server_path.iterdir()
                if f.is_file()
                   and f.suffix == ".jar"
                   and server_type in f.name
                   and f.name != installer_file_name
            ]

            if matching_files:
                server_jar_name = matching_files[0].name
                self.logger.info(f"Found server jar: {server_jar_name}")
                return server_jar_name, False
            else:
                self.logger.error(f"No server jar found after installation in {server_path}")
                self.logger.debug(
                    f"Available jar files: {[f.name for f in server_path.iterdir() if f.suffix == '.jar']}")
                return None, False

    def _get_forge_args_file(self, installer_file_name: str) -> str:
        """Get the appropriate Forge args file path based on platform."""
        parts = installer_file_name.split('-')
        minecraft_version = parts[1]
        forge_version = parts[2]

        if sys.platform in ["linux", "darwin"]:
            return f"@libraries/net/minecraftforge/forge/{minecraft_version}-{forge_version}/unix_args.txt"
        else:
            return f"@libraries/net/minecraftforge/forge/{minecraft_version}-{forge_version}/win_args.txt"

    def _get_neoforge_args_file(self, installer_file_name: str) -> str:
        """Get the appropriate NeoForge args file path based on platform."""
        parts = installer_file_name.split('-')
        neoforge_version = parts[1]

        if sys.platform in ["linux", "darwin"]:
            return f"@libraries/net/neoforged/neoforge/{neoforge_version}/unix_args.txt"
        else:
            return f"@libraries/net/neoforged/neoforge/{neoforge_version}/win_args.txt"

    def _cleanup_files(self, server_path: Path, cleanup_items: list) -> Iterator[Status]:
        """Clean up specified files and directories."""
        yield Status(StatusCode.PROGRESSBAR_NEXT, ["Cleaning up...", 1])

        if not cleanup_items:
            self.logger.debug("No cleanup items specified")
        else:
            self.logger.info(f"Cleaning up {len(cleanup_items)} items")
            for item in cleanup_items:
                full_path = os.path.join(server_path, item)
                if os.path.isfile(full_path):
                    os.remove(full_path)
                    self.logger.debug(f"Removed file: {item}")
                elif os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                    self.logger.debug(f"Removed directory: {item}")
                else:
                    self.logger.debug(f"Cleanup item not found: {item}")

        yield Status(StatusCode.PROGRESSBAR_UPDATE, 1)

    def _assemble_configuration_files(self, server_path: Path, version: Version, server_jar_name: str,
                                      args_instead_of_jar: bool,
                                      assembler_linker_config: AssemblerLinkerConfig) -> Iterator[Status]:
        """Assemble configuration files for the server."""
        self.logger.info("Assembling configuration files")
        yield Status(StatusCode.PROGRESSBAR_NEXT, ["Assembling configuration files...", 1])

        config_files = assembler_linker_config.get_configuration_files()

        if version >= Version(1, 7, 10):
            config_files.append(EulaFile())
            self.logger.debug("EULA file added to configuration files")
        else:
            self.logger.info("EULA file not required, creation skipped")

        self.logger.debug(f"Found {len(config_files)} configuration files to process")

        for config in config_files:
            if config.config_file_name in ["start.sh", "start.bat"]:
                self.logger.debug(f"Setting server-jar property for {config.config_file_name}")
                config.set_configuration_property("server-jar", server_jar_name, version)
                config.set_configuration_property("server-args-instead-of-jar", args_instead_of_jar, version)

        assembler_linker = AssemblerLinker(assembler_linker_config)
        assembler_linker.link()
        assembler_linker.assemble_linked_files(server_path)

        self.logger.info("Configuration files assembled successfully")
        yield Status(StatusCode.PROGRESSBAR_UPDATE, 1)
