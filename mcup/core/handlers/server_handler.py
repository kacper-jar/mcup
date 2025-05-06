import os
import shutil
import subprocess
from pathlib import Path
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from mcup.core.config_assemblers import AssemblerLinkerConfig, AssemblerLinker
from mcup.core.utils.version import Version


class ServerHandler:
    """Class for handling server related actions."""
    def create(self, server_path: Path, server_version: str, source: str,
               target: str, assembler_linker_config: AssemblerLinkerConfig):
        """Downloads/Builds server in specified path along with all required configuration files."""
        version = Version.from_string(server_version)

        if not server_path.exists():
            os.makedirs(server_path)

        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn()
        ) as progress:
            if source == "DOWNLOAD":
                task = progress.add_task("Preparing to download server...", total=1)
                response = requests.get(target, stream=True)
                progress.update(task, advance=1)

                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    task = progress.add_task("Downloading server...", total=total_size)
                    file_name = target.split("/")[-1]
                    file_path = server_path / file_name
                    with open(file_path, "wb") as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                            progress.update(task, advance=len(chunk))
                    print(f"Downloaded: {file_path}")
                    progress.update(task, advance=1)
                else:
                    print(f"Failed to download server. HTTP {response.status_code}")
                    raise Exception("Failed to download server.")
            elif source == "BUILDTOOLS":
                task = progress.add_task("Preparing to download Spigot BuildTools...", total=1)
                spigot_buildtools_url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
                response = requests.get(spigot_buildtools_url, stream=True)
                progress.update(task, advance=1)

                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    task = progress.add_task("Downloading Spigot BuildTools...", total=total_size)
                    file_name = spigot_buildtools_url.split("/")[-1]
                    file_path = server_path / file_name
                    with open(file_path, "wb") as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                            progress.update(task, advance=len(chunk))
                    print(f"Downloaded: {file_path}")
                    progress.update(task, advance=1)
                else:
                    print(f"Failed to download Spigot BuildTools. HTTP {response.status_code}")
                    raise Exception("Failed to download Spigot BuildTools.")

                if not os.path.exists(file_path):
                    raise FileNotFoundError("Spigot BuildTools not found.")

                task = progress.add_task("Building server using Spigot BuildTools...", total=1)
                java_version_output = subprocess.check_output(["java", "-version"],
                                                              stderr=subprocess.STDOUT, text=True)
                java_major_version = int(java_version_output.split("\n")[0].split("\"")[1].split(".")[0])

                if version >= Version(1, 20, 6) and java_major_version < 21:
                    print("Warning: Minecraft 1.20.6 and above require at least JDK 21. BuildTools may fail. "
                          "(Azul Zulu JDK is recommended.)")
                elif version > Version(1, 17, 1) and java_major_version < 17:
                    print("Warning: Minecraft versions above 1.17.1 require at least JDK 17. BuildTools may fail. "
                          "(Azul Zulu JDK is recommended.)")
                elif version >= Version(1, 17, 0) and java_major_version < 16:
                    print("Warning: Minecraft 1.17 and 1.17.1 require at least JDK 16. BuildTools may fail. "
                          "(Azul Zulu JDK is recommended.)")
                elif version < Version(1, 17, 0) and java_major_version < 8:
                    print("Warning: Minecraft versions below 1.17 require at least JDK 8. BuildTools may fail. "
                          "(Azul Zulu JDK is recommended.)")

                subprocess.run(
                    ["java", "-jar", file_path, "--compile", target, "--rev", server_version],
                    cwd=server_path,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                progress.update(task, advance=1)

                if not os.path.exists(server_path / f"{target}-{server_version}.jar"):
                    raise FileNotFoundError("Server JAR file not found. "
                                            "Check BuildTools.log.txt in server folder for more info.")

                task = progress.add_task("Cleaning up...", total=1)
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
                        print(f"Deleted file: {full_path}")
                    elif os.path.isdir(full_path):
                        shutil.rmtree(full_path)
                        print(f"Deleted directory: {full_path}")
                    else:
                        print(f"Not found: {full_path}. Skipping...")
                progress.update(task, advance=1)

            task = progress.add_task("Assembling configuration files...", total=1)
            assembler_linker = AssemblerLinker(assembler_linker_config)
            assembler_linker.link()
            assembler_linker.assemble_linked_files(server_path)
            progress.update(task, advance=1)

            if version >= Version(1, 7, 10):
                task = progress.add_task("Assembling eula.txt...", total=1)
                eula_file_path = server_path / "eula.txt"
                with open(eula_file_path, "w") as file:
                    file.write("# Minecraft EULA available at https://aka.ms/MinecraftEULA\n")
                    file.write("eula=true")
                progress.update(task, advance=1)

            progress.stop()
            print("Server created successfully.")
