import os
from pathlib import Path
import requests

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

        # TODO: rework entire config part into it's own class
        print("server.properties - Server Identity")
        if input("use default configuration? y/n: ") == "y":
            server_properties.set_configuration_default_properties(["motd"])
        else:
            server_properties.set_configuration_property("motd", input("Server motd: "))

        print("server.properties - World Settings")
        if input("use default configuration? y/n: ") == "y":
            server_properties.set_configuration_default_properties(["level-name", "level-seed", "level-type",
                                                                    "generate-structures", "max-build-height"])
        else:
            server_properties.set_configuration_property("level-name", input("World name: "))
            server_properties.set_configuration_property("level-seed", input("World seed: "))
            server_properties.set_configuration_property("level-type", input("World type: "))
            server_properties.set_configuration_property("generate-structures", input("Generate structures: "))
            server_properties.set_configuration_property("max-build-height", input("Max build height: "))

        print("server.properties - Gameplay Settings")
        if input("use default configuration? y/n: ") == "y":
            server_properties.set_configuration_default_properties(["gamemode", "difficulty", "pvp", "allow-flight",
                                                                    "allow-nether"])
        else:
            server_properties.set_configuration_property("gamemode", input("Gamemode: "))
            server_properties.set_configuration_property("difficulty", input("Difficulty: "))
            server_properties.set_configuration_property("pvp", input("PVP: "))
            server_properties.set_configuration_property("allow-flight", input("Allow flight: "))
            server_properties.set_configuration_property("allow-nether", input("Allow nether: "))

        print("server.properties - Entity Spawning")
        if input("use default configuration? y/n: ") == "y":
            server_properties.set_configuration_default_properties(["spawn-animals", "spawn-monsters", "spawn-npcs"])
        else:
            server_properties.set_configuration_property("spawn-animals", input("Spawn animals: "))
            server_properties.set_configuration_property("spawn-monsters", input("Spawn monsters: "))
            server_properties.set_configuration_property("spawn-npcs", input("Spawn NPCs: "))

        print("server.properties - Server Access & Multiplayer")
        if input("use default configuration? y/n: ") == "y":
            server_properties.set_configuration_default_properties(["max-players", "white-list", "online-mode",
                                                                    "server-ip", "server-port"])
        else:
            server_properties.set_configuration_property("max-players", input("Max players: "))
            server_properties.set_configuration_property("white-list", input("Whitelist: "))
            server_properties.set_configuration_property("online-mode", input("Online mode: "))
            server_properties.set_configuration_property("server-ip", input("Server IP: "))
            server_properties.set_configuration_property("server-port", input("Server port: "))

        print("server.properties - Server Communication & Remote Access")
        if input("use default configuration? y/n: ") == "y":
            server_properties.set_configuration_default_properties(["enable-query", "enable-rcon"])
        else:
            server_properties.set_configuration_property("enable-query", input("Enable query: "))
            server_properties.set_configuration_property("enable-rcon", input("Enable RCON: "))

        print("server.properties - Performance")
        if input("use default configuration? y/n: ") == "y":
            server_properties.set_configuration_default_properties(["view-distance"])
        else:
            server_properties.set_configuration_property("view-distance", input("View distance: "))

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
        server_properties_assembler.assemble(server_properties)

        print("Server created successfully.")
