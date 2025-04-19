from mcup.configs import ConfigFile


class BukkitConfig(ConfigFile):
    """Class representing a bukkit.yml Minecraft server configuration file."""
    def __init__(self):
        """Initialize the bukkit.yml configuration with default values."""
        self.config_file_name = "bukkit.yml"
        self.config_file_path = "."

        self.configuration = {
            "settings": {
                "allow-end": None,
                "warn-on-overload": None,
                "permissions-file": None,
                "update-folder": None,
                "ping-packet-limit": None,
                "use-exact-login-location": None,
                "plugin-profiling": None,
                "connection-throttle": None,
                "query-plugins": None,
                "deprecated-verbose": None,
                "shutdown-message": None
            },
            "spawn-limits": {
                "monsters": None,
                "animals": None,
                "water-animals": None,
                "ambient": None
            },
            "chunk-gc": {
                "period-in-ticks": None,
                "load-threshold": None
            },
            "ticks-per": {
                "animal-spawns": None,
                "monster-spawns": None,
                "autosave": None
            },
            "auto-updater": {
                "enabled": None,
                "on-broken": None,
                "on-update": None,
                "preferred-channel": None,
                "host": None,
                "suggest-channels": None
            },
            "aliases": None,
            "database": {
                "username": None,
                "isolation": None,
                "driver": None,
                "password": None,
                "url": None
            }
        }

        self.default_configuration = {
            "settings": {
                "allow-end": True,
                "warn-on-overload": True,
                "permissions-file": "permissions.yml",
                "update-folder": "update",
                "ping-packet-limit": 100,
                "use-exact-login-location": False,
                "plugin-profiling": False,
                "connection-throttle": 4000,
                "query-plugins": True,
                "deprecated-verbose": "default",
                "shutdown-message": "Server closed"
            },
            "spawn-limits": {
                "monsters": 70,
                "animals": 15,
                "water-animals": 5,
                "ambient": 15
            },
            "chunk-gc": {
                "period-in-ticks": 600,
                "load-threshold": 0
            },
            "ticks-per": {
                "animal-spawns": 400,
                "monster-spawns": 1,
                "autosave": 6000
            },
            "auto-updater": {
                "enabled": True,
                "on-broken": [
                    "warn-console",
                    "warn-ops"
                ],
                "on-update": [
                    "warn-console",
                    "warn-ops"
                ],
                "preferred-channel": "rb",
                "host": "dl.bukkit.org",
                "suggest-channels": True
            },
            "aliases": "now-in-commands.yml",
            "database": {
                "username": "bukkit",
                "isolation": "SERIALIZABLE",
                "driver": "org.sqlite.JDBC",
                "password": "walrus",
                "url": "jdbc:sqlite:{DIR}{NAME}.db"
            }
        }
