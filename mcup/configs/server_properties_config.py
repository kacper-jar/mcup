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
            "max-world-size": None,  # 1.8+

            # Gameplay settings
            "gamemode": None,
            "force-gamemode": None,  # 1.5.2+
            "difficulty": None,
            "hardcore": None,  # 1.3.1+
            "pvp": None,
            "allow-flight": None,
            "allow-nether": None,
            "announce-player-achievements": None,  # 1.7.2-1.11.2
            "enable-command-block": None,  # 1.7.2+
            "spawn-protection": None,  # 1.14+

            # Entity spawning
            "spawn-animals": None,
            "spawn-monsters": None,
            "spawn-npcs": None,

            # Server Access & Multiplayer
            "max-players": None,
            "player-idle-timeout": None,  # 1.6.4+
            "white-list": None,
            "enforce-whitelist": None,  # 1.13+
            "online-mode": None,
            "server-ip": None,
            "server-port": None,
            "network-compression-threshold": None,  # 1.8+
            "prevent-proxy-connections": None,  # 1.11+
            "op-permission-level": None,  # 1.7.2+
            "function-permission-level": None,  # 1.14.4+
            "broadcast-console-to-ops": None,  # 1.14+
            "broadcast-rcon-to-ops": None,  # 1.14+

            # Sever Communication & Remote Access
            "enable-query": None,
            "query.port": None,  # 1.14+
            "enable-rcon": None,
            "rcon.password": None,  # 1.14+
            "rcon.port": None,  # 1.14+

            # Performance
            "view-distance": None,
            "max-tick-time": None,  # 1.8+
            "use-native-transport": None,  # 1.14+

            # Customization
            "texture-pack": None,  # 1.3.1-1.6.4
            "resource-pack": None,  # 1.7.2+
            "resource-pack-hash": None,  # 1.8-1.8.9
            "resource-pack-sha1": None,  # 1.9+

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
            "max-world-size": "29999984",

            # Gameplay settings
            "gamemode": "0",
            "force-gamemode": "false",
            "difficulty": "1",
            "hardcore": "false",
            "pvp": "true",
            "allow-flight": "false",
            "allow-nether": "true",
            "announce-player-achievements": "true",
            "enable-command-block": "false",
            "spawn-protection": "16",

            # Entity spawning
            "spawn-animals": "true",
            "spawn-monsters": "true",
            "spawn-npcs": "true",

            # Server Access & Multiplayer
            "max-players": "20",
            "player-idle-timeout": "0",
            "white-list": "false",
            "online-mode": "true",
            "server-ip": "",
            "server-port": "25565",
            "network-compression-threshold": "256",
            "prevent-proxy-connections": "false",
            "op-permission-level": "4",
            "function-permission-level": "2",
            "broadcast-console-to-ops": "true",
            "broadcast-rcon-to-ops": "true",

            # Sever Communication & Remote Access
            "enable-query": "false",
            "query.port": "25565",
            "enable-rcon": "false",
            "rcon.password": "",
            "rcon.port": "25575",

            # Performance
            "view-distance": "10",
            "max-tick-time": "60000",
            "use-native-transport": "true",

            # Customization
            "texture-pack": "",
            "resource-pack": "",
            "resource-pack-hash": "",
            "resource-pack-sha1": "",

            # Telemetry
            "snooper-enabled": "true"
        }
