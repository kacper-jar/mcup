from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.core.utils.version import Version, LATEST_VERSION


class BukkitCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Bukkit - General Settings",
            [
                CollectorInput("settings/minimum-api", "COLLECTOR_BUKKIT_MINIMUM_API", CollectorInputType.STRING,
                               Version(1, 14, 3), LATEST_VERSION),
                CollectorInput("settings/use-map-color-cache", "COLLECTOR_BUKKIT_USE_MAP_COLOR_CACHE",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("settings/compatibility/allow-old-keys-in-registry",
                               "COLLECTOR_BUKKIT_ALLOW_OLD_KEYS_IN_REGISTRY",
                               CollectorInputType.BOOL, Version(1, 20, 6), LATEST_VERSION),
                CollectorInput("settings/compatibility/enum-compatibility-mode",
                               "COLLECTOR_BUKKIT_ENABLE_ENUM_COMPATIBILITY_MODE",
                               CollectorInputType.BOOL, Version(1, 21, 1), LATEST_VERSION),
                CollectorInput("settings/allow-end", "COLLECTOR_BUKKIT_ALLOW_END", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/warn-on-overload", "COLLECTOR_BUKKIT_WARN_ON_OVERLOAD",
                               CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/permissions-file", "COLLECTOR_BUKKIT_PERMISSION_FILENAME",
                               CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/update-folder", "COLLECTOR_BUKKIT_UPDATE_FOLDER", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/ping-packet-limit", "COLLECTOR_BUKKIT_PING_PACKET_LIMIT",
                               CollectorInputType.INT, Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("settings/use-exact-login-location", "COLLECTOR_BUKKIT_USE_EXACT_LOGIN_LOCATION",
                               CollectorInputType.BOOL, Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("settings/plugin-profiling", "COLLECTOR_BUKKIT_PROFILE_PLUGINS", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/connection-throttle", "COLLECTOR_BUKKIT_CONNECTION_THROTTLE",
                               CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/query-plugins", "COLLECTOR_BUKKIT_QUERY_PLUGINS", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/deprecated-verbose", "COLLECTOR_BUKKIT_WARN_DEPRECATED_PLUGINS",
                               CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/shutdown-message", "COLLECTOR_BUKKIT_SHUTDOWN_MESSAGE",
                               CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Spawn Limits",
            [
                CollectorInput("spawn-limits/water-ambient", "COLLECTOR_BUKKIT_MAX_WATER_AMBIENT_CREATURES",
                               CollectorInputType.INT, Version(1, 16, 1), LATEST_VERSION),
                CollectorInput("spawn-limits/water-underground-creature",
                               "COLLECTOR_BUKKIT_MAX_WATER_UNDERGROUND_CREATURES",
                               CollectorInputType.INT, Version(1, 18), LATEST_VERSION),
                CollectorInput("spawn-limits/axolotls", "COLLECTOR_BUKKIT_MAX_AXOLOTLS", CollectorInputType.INT,
                               Version(1, 18, 1), LATEST_VERSION),
                CollectorInput("spawn-limits/monsters", "COLLECTOR_BUKKIT_MAX_MONSTERS", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits/animals", "COLLECTOR_BUKKIT_MAX_ANIMALS", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits/water-animals", "COLLECTOR_BUKKIT_MAX_WATER_ANIMALS",
                               CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits/ambient", "COLLECTOR_BUKKIT_MAX_AMBIENT_CREATURES", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Chunk Garbage Collection (Unloader) Settings",
            [
                CollectorInput("chunk-gc/period-in-ticks", "COLLECTOR_BUKKIT_CHUNK_GC_PERIOD", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("chunk-gc/load-threshold", "COLLECTOR_BUKKIT_CHUNK_GC_LOAD_THRESHOLD",
                               CollectorInputType.INT, Version(1, 8, 0), Version(1, 21, 5)),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Ticks Settings",
            [
                CollectorInput("ticks-per/water-spawns", "COLLECTOR_BUKKIT_TICKS_PER_WATER_SPAWNS",
                               CollectorInputType.INT, Version(1, 15, 2), LATEST_VERSION),
                CollectorInput("ticks-per/water-ambient-spawns", "COLLECTOR_BUKKIT_TICKS_PER_WATER_AMBIENT_SPAWNS",
                               CollectorInputType.INT, Version(1, 16, 1), LATEST_VERSION),
                CollectorInput("ticks-per/water-underground-creature-spawns",
                               "COLLECTOR_BUKKIT_TICKS_PER_WATER_UNDERGROUND_CREATURE_SPAWNS",
                               CollectorInputType.INT, Version(1, 18), LATEST_VERSION),
                CollectorInput("ticks-per/axolotl-spawns", "COLLECTOR_BUKKIT_TICKS_PER_AXOLOTL_SPAWNS",
                               CollectorInputType.INT, Version(1, 18, 1), LATEST_VERSION),
                CollectorInput("ticks-per/ambient-spawns", "COLLECTOR_BUKKIT_TICKS_PER_AMBIENT_SPAWNS",
                               CollectorInputType.INT, Version(1, 15, 2), LATEST_VERSION),
                CollectorInput("ticks-per/animal-spawns", "COLLECTOR_BUKKIT_TICKS_PER_ANIMAL_SPAWNS",
                               CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("ticks-per/monster-spawns", "COLLECTOR_BUKKIT_TICKS_PER_MONSTER_SPAWNS",
                               CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("ticks-per/autosave", "COLLECTOR_BUKKIT_TICKS_PER_AUTOSAVE", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Auto-Updater Settings",
            [
                CollectorInput("auto-updater/enabled", "COLLECTOR_BUKKIT_AUTO_UPDATER_ENABLED", CollectorInputType.BOOL,
                               Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("auto-updater/on-broken", "COLLECTOR_BUKKIT_AUTO_UPDATER_ON_BROKEN",
                               CollectorInputType.STRING_LIST, Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("auto-updater/on-update", "COLLECTOR_BUKKIT_AUTO_UPDATER_ON_UPDATE",
                               CollectorInputType.STRING_LIST, Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("auto-updater/preferred-channel", "COLLECTOR_BUKKIT_AUTO_UPDATER_PREFERRED_CHANNEL",
                               CollectorInputType.STRING, Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("auto-updater/host", "COLLECTOR_BUKKIT_AUTO_UPDATER_HOST", CollectorInputType.STRING,
                               Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("auto-updater/suggest-channels", "COLLECTOR_BUKKIT_AUTO_UPDATER_SUGGEST_CHANNELS",
                               CollectorInputType.BOOL, Version(1, 8, 0), Version(1, 21, 5)),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Command Aliases",
            [
                CollectorInput("aliases", "COLLECTOR_BUKKIT_COMMAND_ALIASES", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Database Connection",
            [
                CollectorInput("database/username", "COLLECTOR_BUKKIT_DATABASE_USERNAME", CollectorInputType.STRING,
                               Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("database/isolation", "COLLECTOR_BUKKIT_DATABASE_ISOLATION", CollectorInputType.STRING,
                               Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("database/driver", "COLLECTOR_BUKKIT_DATABASE_DRIVER", CollectorInputType.STRING,
                               Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("database/password", "COLLECTOR_BUKKIT_DATABASE_PASSWORD", CollectorInputType.STRING,
                               Version(1, 8, 0), Version(1, 21, 5)),
                CollectorInput("database/url", "COLLECTOR_BUKKIT_DATABASE_URL", CollectorInputType.STRING,
                               Version(1, 8, 0), Version(1, 21, 5)),
            ]
        ))
