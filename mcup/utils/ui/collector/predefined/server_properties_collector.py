from mcup.utils.ui.collector import Collector, CollectorSection, CollectorInput
from mcup.utils.version import Version, LATEST_VERSION


class ServerPropertiesCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "server.properties - Server Identity",
            [
                CollectorInput("motd", "Server motd", Version(1, 2, 5), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - World Settings",
            [
                CollectorInput("level-name", "World name", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("level-seed", "World seed", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("level-type", "World type", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("generate-structures", "Generate structures", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("generator-settings", "Custom generator settings", Version(1, 4, 2), LATEST_VERSION),
                CollectorInput("max-build-height", "Max build height", Version(1, 2, 5), Version(1, 16, 5)),
                CollectorInput("max-world-size", "Max world size", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Gameplay Settings",
            [
                CollectorInput("gamemode", "Gamemode", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("force-gamemode", "Force Gamemode", Version(1, 5, 2), LATEST_VERSION),
                CollectorInput("difficulty", "Difficulty", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("hardcore", "Hardocre", Version(1, 3, 1), LATEST_VERSION),
                CollectorInput("pvp", "PVP", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("allow-flight", "Allow flight", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("allow-nether", "Allow nether", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("announce-player-achievements", "Announce player achievements",
                               Version(1, 7, 2), Version(1, 11, 2)),
                CollectorInput("enable-command-block", "Enable command blocks", Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("spawn-protection", "Spawn protection", Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("spawn-animals", "Spawn animals", Version(1, 2, 5), Version(1, 21, 1)),
                CollectorInput("spawn-monsters", "Spawn monsters", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("spawn-npcs", "Spawn NPCs", Version(1, 2, 5), Version(1, 21, 1)),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Server Access & Multiplayer",
            [
                CollectorInput("max-players", "Max players", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("player-idle-timeout", "Player idle timeout", Version(1, 6, 4), LATEST_VERSION),
                CollectorInput("white-list", "Whitelist", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("enforce-whitelist", "Enforce whitelist", Version(1, 13, 0), LATEST_VERSION),
                CollectorInput("online-mode", "Online mode", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("server-ip", "Server IP", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("server-port", "Server port", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("network-compression-threshold", "Network compression threshold", Version(1, 8, 0),
                               LATEST_VERSION),
                CollectorInput("prevent-proxy-connections", "Prevent proxy connections", Version(1, 11, 0),
                               LATEST_VERSION),
                CollectorInput("op-permission-level", "Server operator (OP) permission level", Version(1, 7, 2),
                               LATEST_VERSION),
                CollectorInput("function-permission-level", "Function permission level", Version(1, 14, 4),
                               LATEST_VERSION),
                CollectorInput("broadcast-console-to-ops", "Broadcast console to operators", Version(1, 14, 0),
                               LATEST_VERSION),
                CollectorInput("broadcast-rcon-to-ops", "Broadcast RCON to operators", Version(1, 14, 0),
                               LATEST_VERSION),
                CollectorInput("text-filtering-config", "Text filtering config", Version(1, 16, 4), LATEST_VERSION),
                CollectorInput("text-filtering-version", "Text filtering version", Version(1, 21, 2), LATEST_VERSION),
                CollectorInput("hide-online-players", "Hide online players", Version(1, 18, 0), LATEST_VERSION),
                CollectorInput("enforce-secure-profile", "Enforce secure profile", Version(1, 19, 0), LATEST_VERSION),
                CollectorInput("previews-chat", "Previews chat", Version(1, 19, 0), Version(1, 19, 2)),
                CollectorInput("accepts-transfers", "Accepts transfers", Version(1, 20, 5), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Server Communication & Remote Access",
            [
                CollectorInput("enable-query", "Enable query", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("query.port", "Query port", Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("enable-rcon", "Enable RCON", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("rcon.password", "RCON password", Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("rcon.port", "RCON port", Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("enable-status", "Enable status", Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("enable-jmx-monitoring", "Enable JMX monitoring", Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("rate-limit", "Rate limit", Version(1, 16, 2), LATEST_VERSION),
                CollectorInput("log-ips", "Log IPs", Version(1, 20, 2), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Performance & Telemetry",
            [
                CollectorInput("view-distance", "View distance", Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("simulation-distance", "Simulation distance", Version(1, 18, 0), LATEST_VERSION),
                CollectorInput("max-tick-time", "Max tick time", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("use-native-transport", "Use native transport", Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("entity-broadcast-range-percentage", "Entity broadcast range percentage",
                               Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("sync-chunk-writes", "Sync chunk writes", Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("max-chained-neighbor-updates", "Max chained neighbor updates",
                               Version(1, 19, 0), LATEST_VERSION),
                CollectorInput("region-file-compression", "Region file compression algorithm",
                               Version(1, 20, 5), LATEST_VERSION),
                CollectorInput("pause-when-empty-seconds", "Pause server when empty for",
                               Version(1, 21, 2), LATEST_VERSION),
                CollectorInput("snooper-enabled", "Enable Snooper (sending anonymous usage statistics to Mojang)",
                               Version(1, 3, 2), Version(1, 17, 1)),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Customization",
            [
                CollectorInput("texture-pack", "Texture pack", Version(1, 3, 1), Version(1, 6, 4)),
                CollectorInput("resource-pack", "Resource pack", Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("resource-pack-hash", "Resource pack hash", Version(1, 8, 0), Version(1, 8, 9)),
                CollectorInput("resource-pack-sha1", "Resource pack SHA1", Version(1, 9, 0), LATEST_VERSION),
                CollectorInput("require-resource-pack", "Require resource pack", Version(1, 17, 0), LATEST_VERSION),
                CollectorInput("resource-pack-prompt", "Resource pack prompt", Version(1, 17, 0), LATEST_VERSION),
                CollectorInput("resource-pack-id", "Resource pack ID", Version(1, 20, 3), LATEST_VERSION),
                CollectorInput("initial-enabled-packs", "Initial enabled data packs",
                               Version(1, 19, 3), LATEST_VERSION),
                CollectorInput("initial-disabled-packs", "Initial disabled data packs",
                               Version(1, 19, 3), LATEST_VERSION)
            ]
        ))
