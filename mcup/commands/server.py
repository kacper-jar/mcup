import os
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
        for server in locker_data["servers"]:
            if server == server_type:
                is_valid_server_type = True
                break
            is_valid_server_type = False
        if not is_valid_server_type:
            print(f"Invalid or unsupported server type: {server_type}")
            return

        server_version = input(f"{server_type} server version (full list available at: ): ")
        for version in locker_data["servers"][server_type]:
            if version["version"] == server_version:
                is_valid_server_version = True
                url = version["url"]
                break
            is_valid_server_version = False
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

            task = progress.add_task("Assembling server.properties...", total=1)
            server_properties_assembler = ServerPropertiesAssembler()
            server_properties_assembler.assemble(server_path, server_properties)
            progress.update(task, advance=1)

            # TODO: Replace this with detecting configs inside locker.json
            if server_type == "spigot" or server_type == "paper":
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
