from mcup.utils.ui.collector import Collector, CollectorSection, CollectorInput
from mcup.utils.version import Version, LATEST_VERSION


class BukkitCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Bukkit - General Settings",
            [
                CollectorInput("settings:allow-end", "Allow End", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:warn-on-overload", "Warn on overload", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:permissions-file", "Permission filename", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:update-folder", "Update folder", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:ping-packet-limit", "Limit ping packet", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:use-exact-login-location", "use-exact-login-location", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:plugin-profiling", "Profile plugins", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:connection-throttle", "Throttle connections", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:query-plugins", "Query plugins", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:deprecated-verbose", "Warn about deprecated plugins", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings:shutdown-message", "Shutdown message", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Spawn Limits",
            [
                CollectorInput("spawn-limits:monsters", "Max monsters", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits:animals", "Max animals", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits:water-animals", "Max water animals", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("spawn-limits:ambient", "Max ambient creatures", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Chunk gc",
            [
                CollectorInput("chunk-gc:period-in-ticks", "Chunk GC period in ticks", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("chunk-gc:load-threshold", "Chunk GC load threshold", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Ticks Settings",
            [
                CollectorInput("ticks-per:animal-spawns", "Ticks per animal spawns", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("ticks-per:monster-spawns", "Ticks per monsters spawns", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("ticks-per:autosave", "Ticks per autosaves", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Auto-Updater Settings",
            [
                CollectorInput("auto-updater:enabled", "Enable Auto-Updater", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater:on-broken", "Warn when broken version", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater:on-update", "Warn when outdated version", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater:on-update", "Warn when outdated version", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater:preferred-channel", "Preferred update channel", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater:host", "Host to download updates from", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("auto-updater:suggest-channels", "Automatically suggest update channel", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Command Aliases",
            [
                CollectorInput("aliases", "Command aliases filename", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Bukkit - Database Connection",
            [
                CollectorInput("database:username", "Database username", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("database:isolation", "Database isolation", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("database:driver", "Database driver", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("database:password", "Database password", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("database:url", "Database url", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
