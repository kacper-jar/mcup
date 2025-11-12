from mcup.core.configs import ConfigFile
from mcup.core.utils.version import VersionDependantVariablePicker, VersionDependantVariable, Version, LATEST_VERSION


class BukkitConfig(ConfigFile):
    """Class representing a bukkit.yml Minecraft server configuration file."""
    def __init__(self):
        """Initialize the bukkit.yml configuration with default values."""
        self.config_file_name = "bukkit.yml"
        self.config_file_path = "."

        self.configuration = {
            "settings": {
                "minimum-api": None,  # 1.14.3+
                "use-map-color-cache": None,  # 1.19+
                "compatibility": {
                    "allow-old-keys-in-registry": None,  # 1.20.6+
                    "enum-compatibility-mode": None  # 1.21.1+
                },
                "allow-nether": None,  # 1.21.9+
                "allow-end": None,
                "warn-on-overload": None,
                "permissions-file": None,
                "update-folder": None,
                "ping-packet-limit": None,  # 1.8-1.21.5
                "use-exact-login-location": None,  # 1.8-1.21.5
                "plugin-profiling": None,
                "connection-throttle": None,
                "query-plugins": None,
                "deprecated-verbose": None,
                "shutdown-message": None
            },
            "spawn-limits": {
                "water-ambient": None,  # 1.16.1+
                "water-underground-creature": None,  # 1.18+
                "axolotls": None,  # 1.18.1+
                "monsters": None,
                "animals": None,
                "water-animals": None,
                "ambient": None
            },
            "chunk-gc": {
                "period-in-ticks": None,
                "load-threshold": None  # 1.8-1.21.5
            },
            "ticks-per": {
                "water-spawns": None,  # 1.15.2+
                "water-ambient-spawns": None,  # 1.16.1+
                "water-underground-creature-spawns": None,  # 1.18+
                "axolotl-spawns": None,  # 1.18.1+
                "ambient-spawns": None,  # 1.15.2+
                "animal-spawns": None,
                "monster-spawns": None,
                "autosave": None
            },
            "auto-updater": {  # 1.8-1.21.5
                "enabled": None,
                "on-broken": None,
                "on-update": None,
                "preferred-channel": None,
                "host": None,
                "suggest-channels": None
            },
            "aliases": None,
            "database": {  # 1.8-1.21.5
                "username": None,
                "isolation": None,
                "driver": None,
                "password": None,
                "url": None
            }
        }

        self.default_configuration = {
            "settings": {
                "minimum-api": None,
                "use-map-color-cache": True,
                "compatibility": {
                    "allow-old-keys-in-registry": False,
                    "enum-compatibility-mode": False
                },
                "allow-nether": True,
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
                "water-ambient": 20,
                "water-underground-creature": 5,
                "axolotls": 5,
                "monsters": 70,
                "animals": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 8, 0), Version(1, 21, 5), 15),
                    VersionDependantVariable(Version(1, 21, 6), LATEST_VERSION, 10)
                ]),
                "water-animals": 5,
                "ambient": 15
            },
            "chunk-gc": {
                "period-in-ticks": 600,
                "load-threshold": 0
            },
            "ticks-per": {
                "water-spawns": 1,
                "water-ambient-spawns": 1,
                "water-underground-creature-spawns": 1,
                "axolotl-spawns": 1,
                "ambient-spawns": 1,
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
