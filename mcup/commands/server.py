import os
from pathlib import Path
import requests
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from mcup.config_assemblers import ServerPropertiesAssembler
from mcup.configs import ServerPropertiesConfig
from mcup.utils.locker import LockerManager
from mcup.utils.ui.collector import Collector, CollectorSection, CollectorInput
from mcup.utils.version import Version, LATEST_VERSION


class ServerCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup server create [path]' command."""
        console = Console()

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
        collector = Collector()
        collector.add_section(CollectorSection(
            "server.properties - Server Identity",
            [
                CollectorInput("motd", "Server motd", Version(1, 2, 5), LATEST_VERSION),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - World Settings",
            [
                CollectorInput("level-name", "World name", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("level-seed", "World seed", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("level-type", "World type", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("generate-structures", "Generate structures", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("generator-settings", "Custom Generator settings", Version(1, 4, 2), LATEST_VERSION),
                CollectorInput("max-build-height", "Max build height", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("max-world-size", "Max world size", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Gameplay Settings",
            [
                CollectorInput("gamemode", "Gamemode", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("force-gamemode", "Force Gamemode", Version(1, 5, 2), LATEST_VERSION),
                CollectorInput("difficulty", "Difficulty", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("hardcore", "Hardocre", Version(1, 3, 1), LATEST_VERSION),
                CollectorInput("pvp", "PVP", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("allow-flight", "Allow flight", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("allow-nether", "Allow nether", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("announce-player-achievements", "Announce player achievements",
                               Version(1, 7, 2), Version(1, 11, 2)),
                CollectorInput("enable-command-block", "Enable command blocks", Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("spawn-protection", "Spawn protection", Version(1, 14, 0), LATEST_VERSION),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Entity Spawning",
            [
                CollectorInput("spawn-animals", "Spawn animals", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("spawn-monsters", "Spawn monsters", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("spawn-npcs", "Spawn NPCs", Version(1, 2, 5), LATEST_VERSION),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Server Access & Multiplayer",
            [
                CollectorInput("max-players", "Max players", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("player-idle-timeout", "Player idle timeout", Version(1, 6, 4), LATEST_VERSION),
                CollectorInput("white-list", "Whitelist", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("enforce-whitelist", "Enforce whitelist", Version(1, 13, 0), LATEST_VERSION),
                CollectorInput("online-mode", "Online mode", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("server-ip", "Server IP", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("server-port", "Server port", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("network-compression-threshold", "Network compression threshold", Version(1, 8, 0),
                               LATEST_VERSION),
                CollectorInput("prevent-proxy-connections", "Prevent proxy connections", Version(1, 11, 0),
                               LATEST_VERSION),
                CollectorInput("op-permission-level", "Server operator (OP) permission level", Version(1, 7, 2),
                               LATEST_VERSION),
                CollectorInput("function-permission-level", "Function permission level", Version(1, 14, 4),
                               LATEST_VERSION),
                CollectorInput("broadcast-console-to-ops", "Broadcast console to operators", Version(1, 14, 0),
                               LATEST_VERSION),
                CollectorInput("broadcast-rcon-to-ops", "Broadcast RCON to operators", Version(1, 14, 0),
                               LATEST_VERSION)
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Server Communication & Remote Access",
            [
                CollectorInput("enable-query", "Enable query", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("query.port", "Query port", Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("enable-rcon", "Enable RCON", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("rcon.password", "RCON password", Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("rcon.port", "RCON port", Version(1, 14, 0), LATEST_VERSION),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Performance",
            [
                CollectorInput("view-distance", "View distance", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("max-tick-time", "Max tick time", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("use-native-transport", "Use native transport", Version(1, 14, 0), LATEST_VERSION),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Customization",
            [
                CollectorInput("texture-pack", "Texture pack", Version(1, 3, 1), Version(1, 6, 4)),
                CollectorInput("resource-pack", "Resource pack", Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("resource-pack-hash", "Resource pack hash", Version(1, 8, 0), Version(1, 8, 9)),
                CollectorInput("resource-pack-sha1", "Resource pack SHA1", Version(1, 9, 0), LATEST_VERSION)
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Mojang Telemetry",
            [
                CollectorInput("snooper-enabled", "Enable Snooper (sending anonymous usage statistics to Mojang)",
                               Version(1, 3, 2), LATEST_VERSION),
            ]
        ))

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

            if version >= Version(1, 7, 10):
                task = progress.add_task("Assembling eula.txt...", total=1)
                eula_file_path = server_path / "eula.txt"
                with open(eula_file_path, "w") as file:
                    file.write("# Minecraft EULA available at https://aka.ms/MinecraftEULA\n")
                    file.write("eula=true")
                progress.update(task, advance=1)

            progress.stop()
            print("Server created successfully.")
