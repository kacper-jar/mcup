from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.core.utils.version import Version, LATEST_VERSION


class BukkitCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Bukkit - General Settings",
            [
                CollectorInput("settings/minimum-api", "Minimum API", CollectorInputType.STRING,
                               Version(1, 14, 3), LATEST_VERSION),
                CollectorInput("settings/allow-end", "Allow End", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/warn-on-overload", "Warn on overload", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/permissions-file", "Permission filename", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/update-folder", "Update folder", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/ping-packet-limit", "Limit ping packet", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/use-exact-login-location", "use-exact-login-location", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/plugin-profiling", "Profile plugins", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/connection-throttle", "Throttle connections", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/query-plugins", "Query plugins", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/deprecated-verbose", "Warn about deprecated plugins",
                               CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/shutdown-message", "Shutdown message", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Spawn Limits",
            [
                CollectorInput("spawn-limits/water-ambient", "Max water ambient creatures", CollectorInputType.INT,
                               Version(1, 16, 1), LATEST_VERSION),
                CollectorInput("spawn-limits/monsters", "Max monsters", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits/animals", "Max animals", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits/water-animals", "Max water animals", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits/ambient", "Max ambient creatures", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Chunk Garbage Collection (Unloader) Settings",
            [
                CollectorInput("chunk-gc/period-in-ticks", "Period in ticks between checks", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("chunk-gc/load-threshold", "Loaded chunks threshold", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Ticks Settings",
            [
                CollectorInput("ticks-per/water-spawns", "Ticks per water spawns", CollectorInputType.INT,
                               Version(1, 15, 2), LATEST_VERSION),
                CollectorInput("ticks-per/water-ambient-spawns", "Ticks per water ambient spawns",
                               CollectorInputType.INT, Version(1, 16, 1), LATEST_VERSION),
                CollectorInput("ticks-per/ambient-spawns", "Ticks per ambient spawns", CollectorInputType.INT,
                               Version(1, 15, 2), LATEST_VERSION),
                CollectorInput("ticks-per/animal-spawns", "Ticks per animal spawns", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("ticks-per/monster-spawns", "Ticks per monsters spawns", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("ticks-per/autosave", "Ticks per autosaves", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Auto-Updater Settings",
            [
                CollectorInput("auto-updater/enabled", "Enable Auto-Updater", CollectorInputType.BOOL,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater/on-broken", "Warn when broken version", CollectorInputType.STRING_LIST,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater/on-update", "Warn when outdated version", CollectorInputType.STRING_LIST,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater/preferred-channel", "Preferred update channel", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater/host", "Host to download updates from", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater/suggest-channels", "Automatically suggest update channel",
                               CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Command Aliases",
            [
                CollectorInput("aliases", "Command aliases filename", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Database Connection",
            [
                CollectorInput("database/username", "Database username", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("database/isolation", "Database isolation", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("database/driver", "Database driver", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("database/password", "Database password", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("database/url", "Database URL", CollectorInputType.STRING,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
