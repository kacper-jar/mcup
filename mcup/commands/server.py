import os
import shutil
import subprocess
from pathlib import Path
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from mcup.config_assemblers import ServerPropertiesAssembler
from mcup.config_assemblers import YmlAssembler
from mcup.configs import ServerPropertiesConfig
from mcup.configs import BukkitConfig
from mcup.utils.locker import LockerManager
from mcup.utils.ui.collector.predefined import ServerPropertiesCollector
from mcup.utils.version import Version


class ServerCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup server create [path]' command."""
        server_path = Path(args.path).resolve()

        if not server_path.exists():
            os.makedirs(server_path)

        print(f"Creating a Minecraft server in: {server_path}")

        locker = LockerManager()
        locker_data = locker.load_locker()

        print("By creating Minecraft server you agree with Minecraft EULA available at https://aka.ms/MinecraftEULA")

        server_type = input("Server type (full list available at: ): ")
        is_valid_server_type = False
        for server in locker_data["servers"]:
            if server == server_type:
                is_valid_server_type = True
                break
        if not is_valid_server_type:
            print(f"Invalid or unsupported server type: {server_type}")
            return

        server_version = input(f"{server_type} server version (full list available at: ): ")
        is_valid_server_version = False
        for version in locker_data["servers"][server_type]:
            if version["version"] == server_version:
                is_valid_server_version = True
                source = version["source"]
                if source == "DOWNLOAD":
                    url = version["url"]
                elif source == "BUILDTOOLS":
                    target = version["target"]
                configs = version["configs"]
                break
        if not is_valid_server_version:
            print(f"Invalid or unsupported server version: {server_version}")
            return

        server_properties = ServerPropertiesConfig()
        collector = ServerPropertiesCollector()

        major, minor, patch = server_version.split(".")
        version = Version(int(major), int(minor), int(patch))
        output = collector.start_collector(version)

        server_properties.set_configuration_properties(output)

        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn()
        ) as progress:
            if source == "DOWNLOAD":
                task = progress.add_task("Preparing to download server...", total=1)
                response = requests.get(url, stream=True)
                progress.update(task, advance=1)

                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    task = progress.add_task("Downloading server...", total=total_size)
                    file_name = url.split("/")[-1]
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
                java_version_output = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT, text=True)
                java_major_version = int(java_version_output.split("\n")[0].split("\"")[1].split(".")[0])

                if version >= Version(1, 20, 6) and java_major_version < 21:
                    raise RuntimeError("Minecraft 1.20.6 and above require at least JDK 21. (Azul Zulu JDK is recommended.)")
                elif version > Version(1, 17, 1) and java_major_version < 17:
                    raise RuntimeError("Minecraft versions above 1.17.1 require at least JDK 17. (Azul Zulu JDK is recommended.)")
                elif version >= Version(1, 17, 0) and java_major_version < 16:
                    raise RuntimeError("Minecraft 1.17 and 1.17.1 require at least JDK 16. (Azul Zulu JDK is recommended.)")
                elif version < Version(1, 17, 0) and java_major_version < 8:
                    raise RuntimeError("Minecraft versions below 1.17 require at least JDK 8. (Azul Zulu JDK is recommended.)")

                subprocess.run(
                    ["java", "-jar", file_path, "--compile", target, "--rev", server_version],
                    cwd=server_path,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                progress.update(task, advance=1)

                if not os.path.exists(server_path / f"{target}-{server_version}.jar"):
                    raise FileNotFoundError("Server JAR file not found. Check BuildTools.log.txt in server folder for more info.")

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

            task = progress.add_task("Assembling server.properties...", total=1)
            server_properties_assembler = ServerPropertiesAssembler()
            server_properties_assembler.assemble(server_path, server_properties)
            progress.update(task, advance=1)

            # TODO: replace this with some kind of "assembler linker" or smth
            if "bukkit" in configs:
                task = progress.add_task("Assembling bukkit.yml...", total=1)

                bukkit_config = BukkitConfig()

                yml_assembler = YmlAssembler()
                yml_assembler.assemble(server_path, bukkit_config)
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
