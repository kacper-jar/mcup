import os
import shutil
import subprocess
from pathlib import Path
from typing import Iterator
import requests

from mcup.core.config_assemblers import AssemblerLinkerConfig, AssemblerLinker
from mcup.core.status import Status, StatusCode
from mcup.core.utils.version import Version


class ServerHandler:
    """Class for handling server-related actions."""
    def create(self, server_path: Path, server_version: str, source: str,
               target: str, assembler_linker_config: AssemblerLinkerConfig) -> Iterator[Status]:
        """Downloads/Builds server in a specified path along with all required configuration files."""
        version = Version.from_string(server_version)

        if not server_path.exists():
            os.makedirs(server_path)

        if source == "DOWNLOAD":
            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Preparing to download server...", 1])
            response = requests.get(target, stream=True)

            if response.status_code == 200:
                total_size = int(response.headers.get('content-length', 0))
                yield Status(StatusCode.PROGRESSBAR_NEXT, ["Downloading server...", total_size])
                file_name = target.split("/")[-1]
                file_path = server_path / file_name
                server_jar_name = file_name
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                        yield Status(StatusCode.PROGRESSBAR_UPDATE, len(chunk))
            else:
                yield Status(StatusCode.ERROR_DOWNLOAD_SERVER_FAILED, str(response.status_code))
                return

            if not os.path.exists(file_path):
                yield Status(StatusCode.ERROR_SERVER_JAR_NOT_FOUND)
                return
        elif source == "BUILDTOOLS":
            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Preparing to download Spigot BuildTools...", 1])
            spigot_buildtools_url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
            response = requests.get(spigot_buildtools_url, stream=True)

            if response.status_code == 200:
                total_size = int(response.headers.get('content-length', 0))
                yield Status(StatusCode.PROGRESSBAR_NEXT, ["Downloading Spigot BuildTools...", total_size])
                file_name = spigot_buildtools_url.split("/")[-1]
                file_path = server_path / file_name
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                        yield Status(StatusCode.PROGRESSBAR_UPDATE, len(chunk))
            else:
                yield Status(StatusCode.ERROR_DOWNLOAD_BUILDTOOLS_FAILED, str(response.status_code))
                return

            if not os.path.exists(file_path):
                yield Status(StatusCode.ERROR_BUILD_TOOLS_NOT_FOUND)
                return

            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Building server using Spigot BuildTools...", 1])
            java_version_output = subprocess.check_output(["java", "-version"],
                                                          stderr=subprocess.STDOUT, text=True)
            java_major_version = int(java_version_output.split("\n")[0].split("\"")[1].split(".")[0])

            if version >= Version(1, 20, 6) and java_major_version < 21:
                yield Status(StatusCode.INFO_JAVA_MINIMUM_21)
            elif version > Version(1, 17, 1) and java_major_version < 17:
                yield Status(StatusCode.INFO_JAVA_MINIMUM_17)
            elif version >= Version(1, 17, 0) and java_major_version < 16:
                yield Status(StatusCode.INFO_JAVA_MINIMUM_16)
            elif version < Version(1, 17, 0) and java_major_version < 8:
                yield Status(StatusCode.INFO_JAVA_MINIMUM_8)

            subprocess.run(
                ["java", "-jar", file_path, "--compile", target, "--rev", server_version],
                cwd=server_path,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            server_jar_name = f"{target}-{server_version}.jar"
            if not os.path.exists(server_path / server_jar_name):
                yield Status(StatusCode.ERROR_SERVER_JAR_NOT_FOUND)
                return

            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Cleaning up...", 1])
            to_clean_up = [
                "BuildTools.jar",
                "Bukkit",
                "CraftBukkit",
                "work",
                "Spigot",
                "BuildData",
                "apache-maven-3.9.6"
            ]

            for item in to_clean_up:
                full_path = os.path.join(server_path, item)
                if os.path.isfile(full_path):
                    os.remove(full_path)
                elif os.path.isdir(full_path):
                    shutil.rmtree(full_path)
        else:
            yield Status(StatusCode.ERROR_SERVER_SOURCE_NOT_SUPPORTED, source)
            return

        yield Status(StatusCode.PROGRESSBAR_NEXT, ["Assembling configuration files...", 1])
        config_files = assembler_linker_config.get_configuration_files()
        for config in config_files:
            if config.config_file_name == "start.sh":
                config.set_configuration_property("server-jar", server_jar_name, version)

        assembler_linker = AssemblerLinker(assembler_linker_config)
        assembler_linker.link()
        assembler_linker.assemble_linked_files(server_path)

        if version >= Version(1, 7, 10):
            yield Status(StatusCode.PROGRESSBAR_NEXT, ["Assembling eula.txt...", 1])
            eula_file_path = server_path / "eula.txt"
            with open(eula_file_path, "w") as file:
                file.write("# Minecraft EULA available at https://aka.ms/MinecraftEULA\n")
                file.write("eula=true")

        yield Status(StatusCode.PROGRESSBAR_FINISH_TASK)
        yield Status(StatusCode.PROGRESSBAR_END)
        yield Status(StatusCode.SUCCESS)
