from mcup.configs import ConfigFile


class ServerPropertiesConfig(ConfigFile):
    """Class representing a server.properties Minecraft server configuration file."""
    def __init__(self):
        """Initialize the server.properties configuration with default values."""
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
            "max-build-height": None,  # 1.2.5-1.16.5
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
            "spawn-animals": None,  # 1.2.5-1.21.1
            "spawn-monsters": None,  # 1.2.5+
            "spawn-npcs": None,  # 1.2.5-1.21.1

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
            "text-filtering-config": None,  # 1.16.4+
            "text-filtering-version": None,  # 1.21.2+
            "hide-online-players": None,  # 1.18+
            "enforce-secure-profile": None,  # 1.19+
            "previews-chat": None,  # 1.19-1.19.2
            "accepts-transfers": None,  # 1.20.5+

            # Sever Communication & Remote Access
            "enable-query": None,
            "query.port": None,  # 1.14+
            "enable-rcon": None,
            "rcon.password": None,  # 1.14+
            "rcon.port": None,  # 1.14+
            "enable-status": None,  # 1.16+
            "enable-jmx-monitoring": None,  # 1.16+
            "rate-limit": None,  # 1.16.2+
            "log-ips": None,  # 1.20.2+
            "bug-report-link": None,  # 1.21+

            # Performance & Telemetry
            "view-distance": None,
            "simulation-distance": None,  # 1.18+
            "max-tick-time": None,  # 1.8+
            "use-native-transport": None,  # 1.14+
            "entity-broadcast-range-percentage": None,  # 1.16+
            "sync-chunk-writes": None,  # 1.16+
            "max-chained-neighbor-updates": None,  # 1.19+
            "region-file-compression": None,  # 1.20.5+
            "pause-when-empty-seconds": None,  # 1.21.2+
            "snooper-enabled": None,  # 1.3.2-1.17.1

            # Customization
            "texture-pack": None,  # 1.3.1-1.6.4
            "resource-pack": None,  # 1.7.2+
            "resource-pack-hash": None,  # 1.8-1.8.9
            "resource-pack-sha1": None,  # 1.9+
            "require-resource-pack": None,  # 1.17+
            "resource-pack-prompt": None,  # 1.17+
            "resource-pack-id": None,  # 1.20.3+
            "initial-enabled-packs": None,  # 1.19.3+
            "initial-disabled-packs": None  # 1.19.3+
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
            "spawn-animals": "true",
            "spawn-monsters": "true",
            "spawn-npcs": "true",

            # Server Access & Multiplayer
            "max-players": "20",
            "player-idle-timeout": "0",
            "white-list": "false",
            "enforce-whitelist": "false",
            "online-mode": "true",
            "server-ip": "",
            "server-port": "25565",
            "network-compression-threshold": "256",
            "prevent-proxy-connections": "false",
            "op-permission-level": "4",
            "function-permission-level": "2",
            "broadcast-console-to-ops": "true",
            "broadcast-rcon-to-ops": "true",
            "text-filtering-config": "",
            "text-filtering-version": "0",
            "hide-online-players": "false",
            "enforce-secure-profile": "true",
            "previews-chat": "false",
            "accepts-transfers": "false",

            # Sever Communication & Remote Access
            "enable-query": "false",
            "query.port": "25565",
            "enable-rcon": "false",
            "rcon.password": "",
            "rcon.port": "25575",
            "enable-status": "true",
            "enable-jmx-monitoring": "false",
            "rate-limit": "0",
            "log-ips": "true",
            "bug-report-link": "",

            # Performance & Telemetry
            "view-distance": "10",
            "simulation-distance": "10",
            "max-tick-time": "60000",
            "use-native-transport": "true",
            "entity-broadcast-range-percentage": "100",
            "sync-chunk-writes": "true",
            "max-chained-neighbor-updates": "1000000",
            "region-file-compression": "deflate",
            "pause-when-empty-seconds": "60",
            "snooper-enabled": "true",

            # Customization
            "texture-pack": "",
            "resource-pack": "",
            "resource-pack-hash": "",
            "resource-pack-sha1": "",
            "require-resource-pack": "false",
            "resource-pack-prompt": "",
            "resource-pack-id": "",
            "initial-enabled-packs": "vanilla",
            "initial-disabled-packs": ""
        }
