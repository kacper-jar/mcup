from dataclasses import dataclass

from mcup.configs import ConfigFile


@dataclass
class ServerPropertiesConfig(ConfigFile):
    """Class representing a server.properties Minecraft server configuration file"""
    def __init__(self):
        self.config_file_name = "server.properties"
        self.config_file_path = "."

        self.configuration = {
            # Server Identity
            "motd": None,

            # World Settings
            "level-name": None,
            "level-seed": None,
            "level-type": None,
            "generate-structures": None,
            "generator-settings": None,  # 1.4.2+
            "max-build-height": None,

            # Gameplay settings
            "gamemode": None,
            "difficulty": None,
            "hardcore": None,  # 1.3.1+
            "pvp": None,
            "allow-flight": None,
            "allow-nether": None,

            # Entity spawning
            "spawn-animals": None,
            "spawn-monsters": None,
            "spawn-npcs": None,

            # Server Access & Multiplayer
            "max-players": None,
            "white-list": None,
            "online-mode": None,
            "server-ip": None,
            "server-port": None,

            # Sever Communication & Remote Access
            "enable-query": None,
            "enable-rcon": None,

            # Performance
            "view-distance": None,

            # Customization
            "texture-pack": None,  # 1.3.1+

            # Telemetry
            "snooper-enabled": None,  # 1.3.2+
        }

        self.default_configuration = {
            # Server Identity
            "motd": "mcup Minecraft Server",

            # World Settings
            "level-name": "world",
            "level-seed": "",
            "level-type": "DEFAULT",
            "generate-structures": "true",
            "generator-settings": "",
            "max-build-height": "256",

            # Gameplay settings
            "gamemode": "0",
            "difficulty": "1",
            "hardcore": "false",
            "pvp": "true",
            "allow-flight": "false",
            "allow-nether": "true",

            # Entity spawning
            "spawn-animals": "true",
            "spawn-monsters": "true",
            "spawn-npcs": "true",

            # Server Access & Multiplayer
            "max-players": "20",
            "white-list": "false",
            "online-mode": "true",
            "server-ip": "",
            "server-port": "25565",

            # Sever Communication & Remote Access
            "enable-query": "false",
            "enable-rcon": "false",

            # Performance
            "view-distance": "10",

            # Customization
            "texture-pack": "",

            # Telemetry
            "snooper-enabled": "true"
        }
