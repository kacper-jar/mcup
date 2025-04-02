import os
from pathlib import Path
import requests

from mcup.config_assemblers import ServerPropertiesAssembler
from mcup.configs import ServerPropertiesConfig
from mcup.utils.locker import LockerManager
from mcup.utils.ui.collector import Collector, CollectorSection, CollectorInput
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
        collector = Collector()
        collector.add_section(CollectorSection(
            "server.properties - Server Identity",
            [
                CollectorInput("motd", "Server motd", Version(1, 2, 5), Version(1, 5, 1)),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - World Settings",
            [
                CollectorInput("level-name", "World name", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("level-seed", "World seed", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("level-type", "World type", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("generate-structures", "Generate structures", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("generator-settings", "Custom Generator settings", Version(1, 4, 2), Version(1, 5, 1)),
                CollectorInput("max-build-height", "Max build height", Version(1, 2, 5), Version(1, 5, 1)),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Gameplay Settings",
            [
                CollectorInput("gamemode", "Gamemode", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("difficulty", "Difficulty", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("hardcore", "Hardocre", Version(1, 3, 1), Version(1, 5, 1)),
                CollectorInput("pvp", "PVP", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("allow-flight", "Allow flight", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("allow-nether", "Allow nether", Version(1, 2, 5), Version(1, 5, 1)),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Entity Spawning",
            [
                CollectorInput("spawn-animals", "Spawn animals", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("spawn-monsters", "Spawn monsters", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("spawn-npcs", "Spawn NPCs", Version(1, 2, 5), Version(1, 5, 1)),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Server Access & Multiplayer",
            [
                CollectorInput("max-players", "Max players", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("white-list", "Whitelist", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("online-mode", "Online mode", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("server-ip", "Server IP", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("server-port", "Server port", Version(1, 2, 5), Version(1, 5, 1)),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Server Communication & Remote Access",
            [
                CollectorInput("enable-query", "Enable query", Version(1, 2, 5), Version(1, 5, 1)),
                CollectorInput("enable-rcon", "Enable RCON", Version(1, 2, 5), Version(1, 5, 1)),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Performance",
            [
                CollectorInput("view-distance", "View distance", Version(1, 2, 5), Version(1, 5, 1)),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Customization",
            [
                CollectorInput("texture-pack", "Texture pack", Version(1, 3, 1), Version(1, 5, 1)),
            ]
        ))
        collector.add_section(CollectorSection(
            "server.properties - Mojang Telemetry",
            [
                CollectorInput("snooper-enabled", "Enable Snooper (sending anonymous usage statistics to Mojang)",
                               Version(1, 3, 2), Version(1, 5, 1)),
            ]
        ))

        major, minor, patch = server_version.split(".")
        version = Version(int(major), int(minor), int(patch))
        output = collector.start_collector(version)

        server_properties.set_configuration_properties(output)

        print("Downloading server...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_name = url.split("/")[-1]
            file_path = server_path / file_name
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download server. HTTP {response.status_code}")

        print("Writing server.properties...")
        server_properties_assembler = ServerPropertiesAssembler()
        server_properties_assembler.assemble(server_path, server_properties)

        print("Server created successfully.")
