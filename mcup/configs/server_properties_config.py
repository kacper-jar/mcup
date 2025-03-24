from dataclasses import dataclass

from mcup.configs import ConfigFile


@dataclass
class ServerPropertiesConfig(ConfigFile):
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
            "max-build-height": None,

            # Gameplay settings
            "gamemode": None,
            "difficulty": None,
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
            "view-distance": None
        }