from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.core.utils.version import Version, LATEST_VERSION


class ServerPropertiesCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "server.properties - Server Identity",
            [
                CollectorInput("motd", "COLLECTOR_SRV_PROP_MOTD",
                               CollectorInputType.STRING, Version(1, 2, 5), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - World Settings",
            [
                CollectorInput("level-name", "COLLECTOR_SRV_PROP_LEVEL_NAME", CollectorInputType.STRING,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("level-seed", "COLLECTOR_SRV_PROP_LEVEL_SEED", CollectorInputType.STRING,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("level-type", "COLLECTOR_SRV_PROP_LEVEL_TYPE", CollectorInputType.STRING,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("generate-structures", "COLLECTOR_SRV_PROP_GENERATE_STRUCTURES", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("generator-settings", "COLLECTOR_SRV_PROP_GENERATOR_SETTINGS", CollectorInputType.STRING,
                               Version(1, 4, 2), LATEST_VERSION),
                CollectorInput("max-build-height", "COLLECTOR_SRV_PROP_MAX_BUILD_HEIGHT", CollectorInputType.INT,
                               Version(1, 2, 5), Version(1, 16, 5)),
                CollectorInput("max-world-size", "COLLECTOR_SRV_PROP_MAX_WORLD_SIZE", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Gameplay Settings",
            [
                CollectorInput("gamemode", "COLLECTOR_SRV_PROP_GAMEMODE", CollectorInputType.STRING_OR_INT,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("force-gamemode", "COLLECTOR_SRV_PROP_FORCE_GAMEMODE", CollectorInputType.BOOL,
                               Version(1, 5, 2), LATEST_VERSION),
                CollectorInput("difficulty", "COLLECTOR_SRV_PROP_DIFFICULTY", CollectorInputType.STRING_OR_INT,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("hardcore", "COLLECTOR_SRV_PROP_HARDCORE", CollectorInputType.BOOL,
                               Version(1, 3, 1), LATEST_VERSION),
                CollectorInput("pvp", "COLLECTOR_SRV_PROP_PVP", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("allow-flight", "COLLECTOR_SRV_PROP_ALLOW_FLIGHT", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("allow-nether", "COLLECTOR_SRV_PROP_ALLOW_NETHER", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("announce-player-achievements", "COLLECTOR_SRV_PROP_ANNOUNCE_PLAYER_ACHIEVEMENTS",
                               CollectorInputType.BOOL, Version(1, 7, 2), Version(1, 11, 2)),
                CollectorInput("enable-command-block", "COLLECTOR_SRV_PROP_ENABLE_COMMAND_BLOCK",
                               CollectorInputType.BOOL, Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("spawn-protection", "COLLECTOR_SRV_PROP_SPAWN_PROTECTION", CollectorInputType.INT,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("spawn-animals", "COLLECTOR_SRV_PROP_SPAWN_ANIMALS", CollectorInputType.BOOL,
                               Version(1, 2, 5), Version(1, 21, 1)),
                CollectorInput("spawn-monsters", "COLLECTOR_SRV_PROP_SPAWN_MONSTERS", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("spawn-npcs", "COLLECTOR_SRV_PROP_SPAWN_NPCS", CollectorInputType.BOOL,
                               Version(1, 2, 5), Version(1, 21, 1)),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Server Access & Multiplayer",
            [
                CollectorInput("max-players", "COLLECTOR_SRV_PROP_MAX_PLAYERS", CollectorInputType.INT,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("player-idle-timeout", "COLLECTOR_SRV_PROP_PLAYER_IDLE_TIMEOUT", CollectorInputType.INT,
                               Version(1, 6, 4), LATEST_VERSION),
                CollectorInput("white-list", "COLLECTOR_SRV_PROP_WHITE_LIST", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("enforce-whitelist", "COLLECTOR_SRV_PROP_ENFORCE_WHITELIST", CollectorInputType.BOOL,
                               Version(1, 13, 0), LATEST_VERSION),
                CollectorInput("online-mode", "COLLECTOR_SRV_PROP_ONLINE_MODE", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("server-ip", "COLLECTOR_SRV_PROP_SERVER_IP", CollectorInputType.STRING,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("server-port", "COLLECTOR_SRV_PROP_SERVER_PORT", CollectorInputType.INT,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("network-compression-threshold", "COLLECTOR_SRV_PROP_NETWORK_COMPRESSION_THRESHOLD",
                               CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("prevent-proxy-connections", "COLLECTOR_SRV_PROP_PREVENT_PROXY_CONNECTIONS",
                               CollectorInputType.BOOL, Version(1, 11, 0), LATEST_VERSION),
                CollectorInput("op-permission-level", "COLLECTOR_SRV_PROP_OP_PERMISSION_LEVEL", CollectorInputType.INT,
                               Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("function-permission-level", "COLLECTOR_SRV_PROP_FUNCTION_PERMISSION_LEVEL",
                               CollectorInputType.INT, Version(1, 14, 4), LATEST_VERSION),
                CollectorInput("broadcast-console-to-ops", "COLLECTOR_SRV_PROP_BROADCAST_CONSOLE_TO_OPS",
                               CollectorInputType.BOOL, Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("broadcast-rcon-to-ops", "COLLECTOR_SRV_PROP_BROADCAST_RCON_TO_OPS",
                               CollectorInputType.BOOL, Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("text-filtering-config", "COLLECTOR_SRV_PROP_TEXT_FILTERING_CONFIG",
                               CollectorInputType.STRING, Version(1, 16, 4), LATEST_VERSION),
                CollectorInput("text-filtering-version", "COLLECTOR_SRV_PROP_TEXT_FILTERING_VERSION",
                               CollectorInputType.INT, Version(1, 21, 2), LATEST_VERSION),
                CollectorInput("hide-online-players", "COLLECTOR_SRV_PROP_HIDE_ONLINE_PLAYERS", CollectorInputType.BOOL,
                               Version(1, 18, 0), LATEST_VERSION),
                CollectorInput("enforce-secure-profile", "COLLECTOR_SRV_PROP_ENFORCE_SECURE_PROFILE",
                               CollectorInputType.BOOL, Version(1, 19, 0), LATEST_VERSION),
                CollectorInput("previews-chat", "COLLECTOR_SRV_PROP_PREVIEWS_CHAT", CollectorInputType.BOOL,
                               Version(1, 19, 0), Version(1, 19, 2)),
                CollectorInput("accepts-transfers", "COLLECTOR_SRV_PROP_ACCEPTS_TRANSFERS", CollectorInputType.BOOL,
                               Version(1, 20, 5), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Server Communication & Remote Access",
            [
                CollectorInput("enable-query", "COLLECTOR_SRV_PROP_ENABLE_QUERY", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("query.port", "COLLECTOR_SRV_PROP_QUERY_PORT", CollectorInputType.INT,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("enable-rcon", "COLLECTOR_SRV_PROP_ENABLE_RCON", CollectorInputType.BOOL,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("rcon.password", "COLLECTOR_SRV_PROP_RCON_PASSWORD", CollectorInputType.STRING,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("rcon.port", "COLLECTOR_SRV_PROP_RCON_PORT", CollectorInputType.INT,
                               Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("enable-status", "COLLECTOR_SRV_PROP_ENABLE_STATUS", CollectorInputType.BOOL,
                               Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("enable-jmx-monitoring", "COLLECTOR_SRV_PROP_ENABLE_JMX_MONITORING",
                               CollectorInputType.BOOL, Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("rate-limit", "COLLECTOR_SRV_PROP_RATE_LIMIT", CollectorInputType.INT,
                               Version(1, 16, 2), LATEST_VERSION),
                CollectorInput("log-ips", "COLLECTOR_SRV_PROP_LOG_IPS", CollectorInputType.BOOL,
                               Version(1, 20, 2), LATEST_VERSION),
                CollectorInput("bug-report-link", "COLLECTOR_SRV_PROP_BUG_REPORT_LINK", CollectorInputType.STRING,
                               Version(1, 20, 2), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Performance & Telemetry",
            [
                CollectorInput("view-distance", "COLLECTOR_SRV_PROP_VIEW_DISTANCE", CollectorInputType.INT,
                               Version(1, 2, 5), LATEST_VERSION),
                CollectorInput("simulation-distance", "COLLECTOR_SRV_PROP_SIMULATION_DISTANCE", CollectorInputType.INT,
                               Version(1, 18, 0), LATEST_VERSION),
                CollectorInput("max-tick-time", "COLLECTOR_SRV_PROP_MAX_TICK_TIME", CollectorInputType.INT,
                               Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("use-native-transport", "COLLECTOR_SRV_PROP_USE_NATIVE_TRANSPORT",
                               CollectorInputType.BOOL, Version(1, 14, 0), LATEST_VERSION),
                CollectorInput("entity-broadcast-range-percentage",
                               "COLLECTOR_SRV_PROP_ENTITY_BROADCAST_RANGE_PERCENTAGE",
                               CollectorInputType.INT, Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("sync-chunk-writes", "COLLECTOR_SRV_PROP_SYNC_CHUNK_WRITES", CollectorInputType.BOOL,
                               Version(1, 16, 0), LATEST_VERSION),
                CollectorInput("max-chained-neighbor-updates", "COLLECTOR_SRV_PROP_MAX_CHAINED_NEIGHBOR_UPDATES",
                               CollectorInputType.INT, Version(1, 19, 0), LATEST_VERSION),
                CollectorInput("region-file-compression", "COLLECTOR_SRV_PROP_REGION_FILE_COMPRESSION",
                               CollectorInputType.STRING, Version(1, 20, 5), LATEST_VERSION),
                CollectorInput("pause-when-empty-seconds", "COLLECTOR_SRV_PROP_PAUSE_WHEN_EMPTY_SECONDS",
                               CollectorInputType.INT, Version(1, 21, 2), LATEST_VERSION),
                CollectorInput("snooper-enabled", "COLLECTOR_SRV_PROP_SNOOPER_ENABLED",
                               CollectorInputType.BOOL, Version(1, 3, 2), Version(1, 17, 1)),
            ]
        ))
        self.add_section(CollectorSection(
            "server.properties - Customization",
            [
                CollectorInput("texture-pack", "COLLECTOR_SRV_PROP_TEXTURE_PACK", CollectorInputType.STRING,
                               Version(1, 3, 1), Version(1, 6, 4)),
                CollectorInput("resource-pack", "COLLECTOR_SRV_PROP_RESOURCE_PACK", CollectorInputType.STRING,
                               Version(1, 7, 2), LATEST_VERSION),
                CollectorInput("resource-pack-hash", "COLLECTOR_SRV_PROP_RESOURCE_PACK_HASH", CollectorInputType.STRING,
                               Version(1, 8, 0), Version(1, 8, 9)),
                CollectorInput("resource-pack-sha1", "COLLECTOR_SRV_PROP_RESOURCE_PACK_SHA1", CollectorInputType.STRING,
                               Version(1, 9, 0), LATEST_VERSION),
                CollectorInput("require-resource-pack", "COLLECTOR_SRV_PROP_REQUIRE_RESOURCE_PACK",
                               CollectorInputType.BOOL, Version(1, 17, 0), LATEST_VERSION),
                CollectorInput("resource-pack-prompt", "COLLECTOR_SRV_PROP_RESOURCE_PACK_PROMPT",
                               CollectorInputType.STRING, Version(1, 17, 0), LATEST_VERSION),
                CollectorInput("resource-pack-id", "COLLECTOR_SRV_PROP_RESOURCE_PACK_ID", CollectorInputType.STRING,
                               Version(1, 20, 3), LATEST_VERSION),
                CollectorInput("initial-enabled-packs", "COLLECTOR_SRV_PROP_INITIAL_ENABLED_PACKS",
                               CollectorInputType.STRING, Version(1, 19, 3), LATEST_VERSION),
                CollectorInput("initial-disabled-packs", "COLLECTOR_SRV_PROP_INITIAL_DISABLED_PACKS",
                               CollectorInputType.STRING, Version(1, 19, 3), LATEST_VERSION)
            ]
        ))
