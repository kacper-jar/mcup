from mcup.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.utils.version import Version, LATEST_VERSION


class ServerPropertiesCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "server.properties - Server Identity",
            [
                CollectorInput("motd", "Server motd", CollectorInputType.STRING, Version(1, 2, 5), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - World Settings",
            [
                CollectorInput("level-name", "World name", CollectorInputType.STRING, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("level-seed", "World seed", CollectorInputType.STRING, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("level-type", "World type", CollectorInputType.STRING, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("generate-structures", "Generate structures", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("generator-settings", "Custom generator settings", CollectorInputType.STRING,
                               Version(1, 4, 2), LATEST_VERSION),
                CollectorInput("max-build-height", "Max build height", CollectorInputType.INT,
                               Version(1, 2, 5), Version(1, 16, 5)),
                CollectorInput("max-world-size", "Max world size", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Gameplay Settings",
            [
                CollectorInput("gamemode", "Gamemode", CollectorInputType.INT, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("force-gamemode", "Force Gamemode", CollectorInputType.BOOL,
                               Version(1, 5, 2), LATEST_VERSION),
                CollectorInput("difficulty", "Difficulty", CollectorInputType.INT, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("hardcore", "Hardocre", CollectorInputType.BOOL, Version(1, 3, 1), LATEST_VERSION),
                CollectorInput("pvp", "PVP", CollectorInputType.BOOL, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("allow-flight", "Allow flight", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("allow-nether", "Allow nether", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("announce-player-achievements", "Announce player achievements", CollectorInputType.BOOL,
                               Version(1, 7, 2), Version(1, 11, 2)),
                CollectorInput("enable-command-block", "Enable command blocks", CollectorInputType.BOOL,
                               Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("spawn-protection", "Spawn protection", CollectorInputType.INT,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("spawn-animals", "Spawn animals", CollectorInputType.BOOL,
                               Version(1, 2, 5), Version(1, 21, 1)),
                CollectorInput("spawn-monsters", "Spawn monsters", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("spawn-npcs", "Spawn NPCs", CollectorInputType.BOOL,
                               Version(1, 2, 5), Version(1, 21, 1)),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Server Access & Multiplayer",
            [
                CollectorInput("max-players", "Max players", CollectorInputType.INT, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("player-idle-timeout", "Player idle timeout", CollectorInputType.INT,
                               Version(1, 6, 4), LATEST_VERSION),
                CollectorInput("white-list", "Whitelist", CollectorInputType.BOOL, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("enforce-whitelist", "Enforce whitelist", CollectorInputType.BOOL,
                               Version(1, 13, 0), LATEST_VERSION),
                CollectorInput("online-mode", "Online mode", CollectorInputType.BOOL, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("server-ip", "Server IP", CollectorInputType.STRING, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("server-port", "Server port", CollectorInputType.INT, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("network-compression-threshold", "Network compression threshold", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("prevent-proxy-connections", "Prevent proxy connections", CollectorInputType.BOOL,
                               Version(1, 11, 0), LATEST_VERSION),
                CollectorInput("op-permission-level", "Server operator (OP) permission level", CollectorInputType.INT,
                               Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("function-permission-level", "Function permission level", CollectorInputType.INT,
                               Version(1, 14, 4), LATEST_VERSION),
                CollectorInput("broadcast-console-to-ops", "Broadcast console to operators", CollectorInputType.BOOL,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("broadcast-rcon-to-ops", "Broadcast RCON to operators", CollectorInputType.BOOL,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("text-filtering-config", "Text filtering config", CollectorInputType.STRING,
                               Version(1, 16, 4), LATEST_VERSION),
                CollectorInput("text-filtering-version", "Text filtering version", CollectorInputType.INT,
                               Version(1, 21, 2), LATEST_VERSION),
                CollectorInput("hide-online-players", "Hide online players", CollectorInputType.BOOL,
                               Version(1, 18, 0), LATEST_VERSION),
                CollectorInput("enforce-secure-profile", "Enforce secure profile", CollectorInputType.BOOL,
                               Version(1, 19, 0), LATEST_VERSION),
                CollectorInput("previews-chat", "Previews chat", CollectorInputType.BOOL,
                               Version(1, 19, 0), Version(1, 19, 2)),
                CollectorInput("accepts-transfers", "Accepts transfers", CollectorInputType.BOOL,
                               Version(1, 20, 5), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Server Communication & Remote Access",
            [
                CollectorInput("enable-query", "Enable query", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("query.port", "Query port", CollectorInputType.INT, Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("enable-rcon", "Enable RCON", CollectorInputType.BOOL, Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("rcon.password", "RCON password", CollectorInputType.STRING,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("rcon.port", "RCON port", CollectorInputType.INT, Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("enable-status", "Enable status", CollectorInputType.BOOL,
                               Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("enable-jmx-monitoring", "Enable JMX monitoring", CollectorInputType.BOOL,
                               Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("rate-limit", "Rate limit", CollectorInputType.INT, Version(1, 16, 2), LATEST_VERSION),
                CollectorInput("log-ips", "Log IPs", CollectorInputType.BOOL, Version(1, 20, 2), LATEST_VERSION),
                CollectorInput("bug-report-link", "Bug report URL", CollectorInputType.STRING,
                               Version(1, 20, 2), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Performance & Telemetry",
            [
                CollectorInput("view-distance", "View distance", CollectorInputType.INT,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("simulation-distance", "Simulation distance", CollectorInputType.INT,
                               Version(1, 18, 0), LATEST_VERSION),
                CollectorInput("max-tick-time", "Max tick time", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("use-native-transport", "Use native transport", CollectorInputType.BOOL,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("entity-broadcast-range-percentage", "Entity broadcast range percentage",
                               CollectorInputType.INT, Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("sync-chunk-writes", "Sync chunk writes", CollectorInputType.BOOL,
                               Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("max-chained-neighbor-updates", "Max chained neighbor updates", CollectorInputType.INT,
                               Version(1, 19, 0), LATEST_VERSION),
                CollectorInput("region-file-compression", "Region file compression algorithm",
                               CollectorInputType.STRING, Version(1, 20, 5), LATEST_VERSION),
                CollectorInput("pause-when-empty-seconds", "Pause server when empty for", CollectorInputType.INT,
                               Version(1, 21, 2), LATEST_VERSION),
                CollectorInput("snooper-enabled", "Enable Snooper (sending anonymous usage statistics to Mojang)",
                               CollectorInputType.BOOL, Version(1, 3, 2), Version(1, 17, 1)),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Customization",
            [
                CollectorInput("texture-pack", "Texture pack", CollectorInputType.STRING,
                               Version(1, 3, 1), Version(1, 6, 4)),
                CollectorInput("resource-pack", "Resource pack", CollectorInputType.STRING,
                               Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("resource-pack-hash", "Resource pack hash", CollectorInputType.STRING,
                               Version(1, 8, 0), Version(1, 8, 9)),
                CollectorInput("resource-pack-sha1", "Resource pack SHA1", CollectorInputType.STRING,
                               Version(1, 9, 0), LATEST_VERSION),
                CollectorInput("require-resource-pack", "Require resource pack", CollectorInputType.BOOL,
                               Version(1, 17, 0), LATEST_VERSION),
                CollectorInput("resource-pack-prompt", "Resource pack prompt", CollectorInputType.STRING,
                               Version(1, 17, 0), LATEST_VERSION),
                CollectorInput("resource-pack-id", "Resource pack ID", CollectorInputType.STRING,
                               Version(1, 20, 3), LATEST_VERSION),
                CollectorInput("initial-enabled-packs", "Initial enabled data packs", CollectorInputType.STRING,
                               Version(1, 19, 3), LATEST_VERSION),
                CollectorInput("initial-disabled-packs", "Initial disabled data packs", CollectorInputType.STRING,
                               Version(1, 19, 3), LATEST_VERSION)
            ]
        ))
