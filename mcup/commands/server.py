import os
from pathlib import Path

from mcup.config_assemblers import ServerPropertiesAssembler
from mcup.configs import ServerPropertiesConfig
from mcup.utils import LockerManager


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

        print(f"By creating Minecraft server you agree with Minecraft EULA available at https://aka.ms/MinecraftEULA")

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
                break
            is_valid_server_version = False
        if not is_valid_server_version:
            print(f"Invalid or unsupported server version: {server_version}")
            return

        server_properties = ServerPropertiesConfig()

        print("server.properties - Server Identity")
        server_properties.set_configuration_property("motd", input("Server motd: "))

        print("server.properties - World Settings")
        server_properties.set_configuration_property("level-name", input("World name: "))
        server_properties.set_configuration_property("level-seed", input("World seed: "))
        server_properties.set_configuration_property("level-type", input("World type: "))
        server_properties.set_configuration_property("generate-structures", input("Generate structures: "))
        server_properties.set_configuration_property("max-build-height", input("Max build height: "))

        print("server.properties - Gameplay Settings")
        server_properties.set_configuration_property("gamemode", input("Gamemode: "))
        server_properties.set_configuration_property("difficulty", input("Difficulty: "))
        server_properties.set_configuration_property("pvp", input("PVP: "))
        server_properties.set_configuration_property("allow-flight", input("Allow flight: "))
        server_properties.set_configuration_property("allow-nether", input("Allow nether: "))

        print("server.properties - Entity Spawning")
        server_properties.set_configuration_property("spawn-animals", input("Spawn animals: "))
        server_properties.set_configuration_property("spawn-monsters", input("Spawn monsters: "))
        server_properties.set_configuration_property("spawn-npcs", input("Spawn NPCs: "))

        print("server.properties - Server Access & Multiplayer")
        server_properties.set_configuration_property("max-players", input("Max players: "))
        server_properties.set_configuration_property("white-list", input("Whitelist: "))
        server_properties.set_configuration_property("online-mode", input("Online mode: "))
        server_properties.set_configuration_property("server-ip", input("Server IP: "))
        server_properties.set_configuration_property("server-port", input("Server port: "))

        print("server.properties - Server Communication & Remote Access")
        server_properties.set_configuration_property("enable-query", input("Enable query: "))
        server_properties.set_configuration_property("enable-rcon", input("Enable RCON: "))

        print("server.properties - Performance")
        server_properties.set_configuration_property("view-distance", input("View distance: "))

        server_properties_assembler = ServerPropertiesAssembler()
        ServerPropertiesAssembler.assemble(server_properties)

