from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.core.utils.version import Version, LATEST_VERSION


class PaperGlobalCollector(Collector):
    def __init__(self):
        super().__init__("Paper (Global)")

        self.add_section(CollectorSection(
            "Anti-cheat",
            [
                CollectorInput("anticheat/obfuscation/items/all-models/also-obfuscate",
                               "COLLECTOR_PAPER_GLOBAL_ANTICHEAT_OBFUSCATION_ITEMS_ALL_MODELS_ALSO_OBFUSCATE",
                               CollectorInputType.STRING_LIST, Version(1, 21, 4), LATEST_VERSION),
                CollectorInput("anticheat/obfuscation/items/all-models/dont-obfuscate",
                               "COLLECTOR_PAPER_GLOBAL_ANTICHEAT_OBFUSCATION_ITEMS_ALL_MODELS_DONT_OBFUSCATE",
                               CollectorInputType.STRING_LIST, Version(1, 21, 4), LATEST_VERSION),
                CollectorInput("anticheat/obfuscation/items/all-models/sanitize-count",
                               "COLLECTOR_PAPER_GLOBAL_ANTICHEAT_OBFUSCATION_ITEMS_ALL_MODELS_SANITIZE_COUNT",
                               CollectorInputType.BOOL, Version(1, 21, 4), LATEST_VERSION),
                CollectorInput("anticheat/obfuscation/items/enable-item-obfuscation",
                               "COLLECTOR_PAPER_GLOBAL_ANTICHEAT_OBFUSCATION_ITEMS_ENABLE_ITEM_OBFUSCATION",
                               CollectorInputType.STRING_LIST, Version(1, 21, 4), LATEST_VERSION),
            ],
            "COLLECTOR_HEADER_DEFAULT_RECOMMENDED"
        ))
        self.add_section(CollectorSection(
            "Block Updates",
            [
                CollectorInput("block-updates/disable-chorus-plant-updates",
                               "COLLECTOR_PAPER_GLOBAL_BLOCK_UPDATES_DISABLE_CHORUS_PLANT_UPDATES",
                               CollectorInputType.BOOL, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("block-updates/disable-mushroom-block-updates",
                               "COLLECTOR_PAPER_GLOBAL_BLOCK_UPDATES_DISABLE_MUSHROOM_BLOCK_UPDATES",
                               CollectorInputType.BOOL, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("block-updates/disable-noteblock-updates",
                               "COLLECTOR_PAPER_GLOBAL_BLOCK_UPDATES_DISABLE_NOTEBLOCK_UPDATES",
                               CollectorInputType.BOOL, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("block-updates/disable-tripwire-updates",
                               "COLLECTOR_PAPER_GLOBAL_BLOCK_UPDATES_DISABLE_TRIPWIRE_UPDATES",
                               CollectorInputType.BOOL, Version(1, 20, 1), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Chunk System & Chunk Loading",
            [
                CollectorInput("async-chunks/threads", "COLLECTOR_PAPER_GLOBAL_ASYNC_CHUNKS_THREADS",
                               CollectorInputType.INT, Version(1, 19), Version(1, 19, 1)),
                CollectorInput("chunk-loading/autoconfig-send-distance",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_AUTOCONFIG_SEND_DISTANCE",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/enable-frustum-priority",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_ENABLE_FRUSTUM_PRIORITY", CollectorInputType.BOOL,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/global-max-chunk-load-rate",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_GLOBAL_MAX_CHUNK_LOAD_RATE",
                               CollectorInputType.INT, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/global-max-chunk-send-rate",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_GLOBAL_MAX_CHUNK_SEND_RATE",
                               CollectorInputType.INT, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/global-max-concurrent-loads",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_GLOBAL_MAX_CONCURRENT_LOADS",
                               CollectorInputType.INT, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/min-load-radius", "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_MIN_LOAD_RADIUS",
                               CollectorInputType.INT, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/player-max-chunk-load-rate",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_PLAYER_MAX_CHUNK_LOAD_RATE",
                               CollectorInputType.INT, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/player-max-concurrent-loads",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_PLAYER_MAX_CONCURRENT_LOADS",
                               CollectorInputType.INT, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/target-player-chunk-send-rate",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_TARGET_PLAYER_CHUNK_SEND_RATE",
                               CollectorInputType.INT, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading-advanced/auto-config-send-distance",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_AUTOCONFIG_SEND_DISTANCE",
                               CollectorInputType.BOOL, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-advanced/player-max-concurrent-chunk-generates",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_PLAYER_MAX_CONCURRENT_GENERATES",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-advanced/player-max-concurrent-chunk-loads",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_PLAYER_MAX_CONCURRENT_LOADS",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-basic/player-max-chunk-generate-rate",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_PLAYER_MAX_CHUNK_GENERATE_RATE",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-basic/player-max-chunk-load-rate",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_PLAYER_MAX_CHUNK_LOAD_RATE",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-basic/player-max-chunk-send-rate",
                               "COLLECTOR_PAPER_GLOBAL_CHUNK_LOADING_PLAYER_MAX_CHUNK_SEND_RATE",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-system/gen-parallelism", "COLLECTOR_PAPER_GLOBAL_CHUNK_SYSTEM_GEN_PARALLELISM",
                               CollectorInputType.BOOL, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-system/io-threads", "COLLECTOR_PAPER_GLOBAL_CHUNK_SYSTEM_IO_THREADS",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-system/worker-threads", "COLLECTOR_PAPER_GLOBAL_CHUNK_SYSTEM_IO_THREADS",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Collisions",
            [
                CollectorInput("collisions/enable-player-collisions",
                               "COLLECTOR_PAPER_GLOBAL_COLLISIONS_ENABLE_PLAYER_COLLISIONS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("collisions/send-full-pos-for-hard-colliding-entities",
                               "COLLECTOR_PAPER_GLOBAL_COLLISIONS_SEND_FULL_POS_FOR_HARD_COLLIDING_ENTITIES",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION)
            ]
        ))
        self.add_section(CollectorSection(
            "Commands",
            [
                CollectorInput("commands/fix-target-selector-tag-completion",
                               "COLLECTOR_PAPER_GLOBAL_COMMANDS_FIX_TARGET_SELECTOR_TAG_COMPLETION",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 21, 3)),
                CollectorInput("commands/ride-command-allow-player-as-vehicle",
                               "COLLECTOR_PAPER_GLOBAL_COMMANDS_RIDE_COMMAND_ALLOW_PLAYER_AS_VEHICLE",
                               CollectorInputType.BOOL, Version(1, 21, 4), LATEST_VERSION),
                CollectorInput("commands/suggest-player-names-when-null-tab-completions",
                               "COLLECTOR_PAPER_GLOBAL_COMMANDS_SUGGEST_PLAYER_NAMES_WHEN_NULL_TAB_COMPLETION",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("commands/time-command-affects-all-worlds",
                               "COLLECTOR_PAPER_GLOBAL_COMMANDS_TIME_COMMAND_AFFECTS_ALL_WORLD",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Console",
            [
                CollectorInput("console/enable-brigadier-completions",
                               "COLLECTOR_PAPER_GLOBAL_CONSOLE_ENABLE_BRIGADIER_COMPLETIONS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("console/enable-brigadier-highlighting",
                               "COLLECTOR_PAPER_GLOBAL_CONSOLE_ENABLE_BRIGADIER_HIGHLIGHTING",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("console/has-all-permissions",
                               "COLLECTOR_PAPER_GLOBAL_CONSOLE_HAS_ALL_PERMISSIONS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Item Validation",
            [
                CollectorInput("item-validation/book/author", "COLLECTOR_PAPER_GLOBAL_ITEM_VALIDATION_BOOK_AUTHOR",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/book/page", "COLLECTOR_PAPER_GLOBAL_ITEM_VALIDATION_BOOK_PAGE",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/book/title", "COLLECTOR_PAPER_GLOBAL_ITEM_VALIDATION_BOOK_TITLE",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/book-size/page-max",
                               "COLLECTOR_PAPER_GLOBAL_ITEM_VALIDATION_BOOK_SIZE_PAGE_MAX",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/book-size/total-multiplier",
                               "COLLECTOR_PAPER_GLOBAL_ITEM_VALIDATION_BOOK_SIZE_TOTAL_MULTIPLIER",
                               CollectorInputType.FLOAT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/display-name", "COLLECTOR_PAPER_GLOBAL_ITEM_VALIDATION_DISPLAY_NAME",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/lore-line", "COLLECTOR_PAPER_GLOBAL_ITEM_VALIDATION_LORE_LINE",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/resolve-selectors-in-books",
                               "COLLECTOR_PAPER_GLOBAL_ITEM_VALIDATION_RESOLVE_SELECTORS_IN_BOOKS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Logging",
            [
                CollectorInput("logging/deobfuscate-stacktraces",
                               "COLLECTOR_PAPER_GLOBAL_LOGGING_DEOBFUSCATE_STACKTRACES",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("logging/log-player-ip-addresses",
                               "COLLECTOR_PAPER_GLOBAL_LOGGING_LOG_PLAYER_IP_ADDRESSES",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 20, 1)),
                CollectorInput("logging/use-rgb-for-named-text-colors",
                               "COLLECTOR_PAPER_GLOBAL_LOGGING_USE_RGB_FOR_NAMED_TEXT_COLORS",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 19, 4)),
            ]
        ))
        self.add_section(CollectorSection(
            "Messages",
            [
                CollectorInput("messages/kick/authentication-servers-down",
                               "COLLECTOR_PAPER_GLOBAL_MESSAGES_KICK_AUTHENTICATION_SERVERS_DOWN",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/kick/connection-throttle",
                               "COLLECTOR_PAPER_GLOBAL_MESSAGES_KICK_CONNECTION_THROTTLE",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/kick/flying-player", "COLLECTOR_PAPER_GLOBAL_MESSAGES_KICK_FLYING_PLAYER",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/kick/flying-vehicle", "COLLECTOR_PAPER_GLOBAL_MESSAGES_KICK_FLYING_VEHICLE",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/no-permission", "COLLECTOR_PAPER_GLOBAL_MESSAGES_NO_PERMISSION",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/use-display-name-in-quit-message",
                               "COLLECTOR_PAPER_GLOBAL_MESSAGES_USE_DISPLAY_NAME_IN_QUIT_MESSAGE",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Misc",
            [
                CollectorInput("misc/chat-threads/chat-executor-core-size",
                               "COLLECTOR_PAPER_GLOBAL_MISC_CHAT_THREADS_CHAT_EXECUTOR_CORE_SIZE",
                               CollectorInputType.INT, Version(1, 19, 2), LATEST_VERSION),
                CollectorInput("misc/chat-threads/chat-executor-max-size",
                               "COLLECTOR_PAPER_GLOBAL_MISC_CHAT_THREADS_CHAT_EXECUTOR_MAX_SIZE",
                               CollectorInputType.INT, Version(1, 19, 2), LATEST_VERSION),
                CollectorInput("misc/client-interaction-leniency-distance",
                               "COLLECTOR_PAPER_GLOBAL_MISC_CLIENT_INTERACTION_LENIENCY_DISTANCE",
                               CollectorInputType.INT, Version(1, 21), LATEST_VERSION),
                CollectorInput("misc/compression-level", "COLLECTOR_PAPER_GLOBAL_MISC_COMPRESSION_LEVEL",
                               CollectorInputType.STRING, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("misc/fix-entity-position-desync",
                               "COLLECTOR_PAPER_GLOBAL_MISC_FIX_ENTITY_POSITION_DESYNC",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 21, 4)),
                CollectorInput("misc/lag-compensate-block-breaking",
                               "COLLECTOR_PAPER_GLOBAL_MISC_LAG_COMPENSATE_BLOCK_BREAKING",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 20)),
                CollectorInput("misc/load-permissions-yml-before-plugins",
                               "COLLECTOR_PAPER_GLOBAL_MISC_LOAD_PERMISSIONS_YML_BEFORE_PLUGINS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/max-joins-per-tick", "COLLECTOR_PAPER_GLOBAL_MISC_MAX_JOINS_PER_TICK",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/prevent-negative-villager-demand",
                               "COLLECTOR_PAPER_GLOBAL_MISC_PREVENT_NEGATIVE_VILLAGER_DEMAND",
                               CollectorInputType.BOOL, Version(1, 21, 6), LATEST_VERSION),
                CollectorInput("misc/region-file-cache-size", "COLLECTOR_PAPER_GLOBAL_MISC_REGION_FILE_CACHE_SIZE",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/send-full-pos-for-item-entities",
                               "COLLECTOR_PAPER_GLOBAL_MISC_SEND_FULL_POS_FOR_ITEM_ENTITIES",
                               CollectorInputType.BOOL, Version(1, 21, 6), LATEST_VERSION),
                CollectorInput("misc/strict-advancement-dimension-check",
                               "COLLECTOR_PAPER_GLOBAL_MISC_STRICT_ADVANCEMENT_DIMENSION_CHECK",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/use-alternative-luck-formula",
                               "COLLECTOR_PAPER_GLOBAL_MISC_USE_ALTERNATIVE_LUCK_FORMULA",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/use-dimension-type-for-custom-spawners",
                               "COLLECTOR_PAPER_GLOBAL_MISC_USE_DIMENSION_TYPE_FOR_CUSTOM_SPAWNERS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/xp-orb-groups-per-area", "COLLECTOR_PAPER_GLOBAL_MISC_XP_ORB_GROUPS_PER_AREA",
                               CollectorInputType.INT, Version(1, 21, 6), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Packet Limiter",
            [
                CollectorInput("packet-limiter/all-packets/action",
                               "COLLECTOR_PAPER_GLOBAL_PACKET_LIMITER_ALL_PACKETS_ACTION",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("packet-limiter/all-packets/interval",
                               "COLLECTOR_PAPER_GLOBAL_PACKET_LIMITER_ALL_PACKETS_INTERVAL",
                               CollectorInputType.FLOAT, Version(1, 19), LATEST_VERSION),
                CollectorInput("packet-limiter/all-packets/max-packet-rate",
                               "COLLECTOR_PAPER_GLOBAL_PACKET_LIMITER_ALL_PACKETS_MAX_PACKET_RATE",
                               CollectorInputType.FLOAT, Version(1, 19), LATEST_VERSION),
                CollectorInput("packet-limiter/kick-message",
                               "COLLECTOR_PAPER_GLOBAL_PACKET_LIMITER_ALL_PACKETS_KICK_MESSAGE",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("packet-limiter/overrides",
                               "COLLECTOR_PAPER_GLOBAL_PACKET_LIMITER_ALL_PACKETS_OVERRIDES",
                               CollectorInputType.STRING_LIST, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Player Auto-save",
            [
                CollectorInput("player-auto-save/max-per-tick", "COLLECTOR_PAPER_GLOBAL_PLAYER_AUTO_SAVE_MAX_PER_TICK",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("player-auto-save/rate", "COLLECTOR_PAPER_GLOBAL_PLAYER_AUTO_SAVE_RATE",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Proxies",
            [
                CollectorInput("proxies/bungee-cord/online-mode",
                               "COLLECTOR_PAPER_GLOBAL_PROXIES_BUNGEE_CORD_ONLINE_MODE",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("proxies/proxy-protocol", "COLLECTOR_PAPER_GLOBAL_PROXIES_PROXY_PROTOCOL",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("proxies/velocity/enabled", "COLLECTOR_PAPER_GLOBAL_PROXIES_VELOCITY_ENABLED",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("proxies/velocity/online-mode", "COLLECTOR_PAPER_GLOBAL_PROXIES_VELOCITY_ONLINE_MODE",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("proxies/velocity/secret", "COLLECTOR_PAPER_GLOBAL_PROXIES_VELOCITY_SECRET",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Scoreboards",
            [
                CollectorInput("scoreboards/save-empty-scoreboard-teams",
                               "COLLECTOR_PAPER_GLOBAL_SCOREBOARDS_SAVE_EMPTY_SCOREBOARD_TEAMS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("scoreboards/track-plugin-scoreboards",
                               "COLLECTOR_PAPER_GLOBAL_SCOREBOARDS_TRACK_PLUGIN_SCOREBOARDS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spam Limiter",
            [
                CollectorInput("spam-limiter/incoming-packet-threshold",
                               "COLLECTOR_PAPER_GLOBAL_SPAM_LIMITER_INCOMING_PACKET_THRESHOLD",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("spam-limiter/recipe-spam-increment",
                               "COLLECTOR_PAPER_GLOBAL_SPAM_LIMITER_RECIPE_SPAM_INCREMENT",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("spam-limiter/recipe-spam-limit",
                               "COLLECTOR_PAPER_GLOBAL_SPAM_LIMITER_RECIPE_SPAM_LIMIT",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("spam-limiter/tab-spam-increment",
                               "COLLECTOR_PAPER_GLOBAL_SPAM_LIMITER_TAB_SPAM_INCREMENT",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("spam-limiter/tab-spam-limit", "COLLECTOR_PAPER_GLOBAL_SPAM_LIMITER_TAB_SPAM_LIMIT",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spark",
            [
                CollectorInput("spark/enable-immediately", "COLLECTOR_PAPER_GLOBAL_SPARK_ENABLE_IMMEDIATELY",
                               CollectorInputType.BOOL, Version(1, 21), LATEST_VERSION),
                CollectorInput("spark/enabled", "COLLECTOR_PAPER_GLOBAL_SPARK_ENABLED",
                               CollectorInputType.BOOL, Version(1, 21), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Timings",
            [
                CollectorInput("timings/enabled", "COLLECTOR_PAPER_GLOBAL_TIMINGS_ENABLED",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("timings/hidden-config-entries", "COLLECTOR_PAPER_GLOBAL_TIMINGS_HIDDEN_CONFIG_ENTRIES",
                               CollectorInputType.STRING_LIST, Version(1, 19), LATEST_VERSION),
                CollectorInput("timings/history-interval", "COLLECTOR_PAPER_GLOBAL_TIMINGS_HISTORY_INTERVAL",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("timings/history-length", "COLLECTOR_PAPER_GLOBAL_TIMINGS_HISTORY_LENGTH",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("timings/server-name", "COLLECTOR_PAPER_GLOBAL_TIMINGS_SERVER_NAME",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("timings/server-name-privacy", "COLLECTOR_PAPER_GLOBAL_TIMINGS_SERVER_NAME_PRIVACY",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("timings/url", "COLLECTOR_PAPER_GLOBAL_TIMINGS_URL",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("timings/verbose", "COLLECTOR_PAPER_GLOBAL_TIMINGS_VERBOSE",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Unsupported (Legacy) Settings",
            [
                CollectorInput("unsupported-settings/allow-grindstone-overstacking",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_ALLOW_GRINDSTONE_OVERSTACKING",
                               CollectorInputType.BOOL, Version(1, 19, 2), Version(1, 20, 4)),
                CollectorInput("unsupported-settings/allow-headless-pistons",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_ALLOW_HEADLESS_PISTONS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("unsupported-settings/allow-permanent-block-break-exploits",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_ALLOW_PERMANENT_BLOCK_BREAK_EXPLOITS",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("unsupported-settings/allow-piston-duplication",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_ALLOW_PISTON_DUPLICATION",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("unsupported-settings/allow-tripwire-disarming-exploits",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_ALLOW_TRIPWIRE_DISARMING_EXPLOITS",
                               CollectorInputType.BOOL, Version(1, 20, 4), Version(1, 21, 1)),
                CollectorInput("unsupported-settings/allow-unsafe-end-portal-teleportation",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_ALLOW_UNSAFE_END_PORTAL_TELEPORTATION",
                               CollectorInputType.BOOL, Version(1, 20, 4), LATEST_VERSION),
                CollectorInput("unsupported-settings/compression-format",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_COMPRESSION_FORMAT",
                               CollectorInputType.STRING, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("unsupported-settings/perform-username-validation",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_PERFORM_USERNAME_VALIDATION",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("unsupported-settings/simplify-remote-item-matching",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_SIMPLIFY_REMOTE_ITEM_MATCHING",
                               CollectorInputType.BOOL, Version(1, 21, 1), Version(1, 21, 4)),
                CollectorInput("unsupported-settings/skip-tripwire-hook-placement-validation",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_SKIP_TRIPWIRE_HOOK_PLACEMENT_VALIDATION",
                               CollectorInputType.BOOL, Version(1, 21, 4), LATEST_VERSION),
                CollectorInput("unsupported-settings/skip-vanilla-damage-tick-when-shield-blocked",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_SKIP_VANILLA_DAMAGE_TICK_WHEN_SHIELD_BLOCKED",
                               CollectorInputType.BOOL, Version(1, 20, 6), LATEST_VERSION),
                CollectorInput("unsupported-settings/update-equipment-on-player-actions",
                               "COLLECTOR_PAPER_GLOBAL_UNSUPPORTED_SETTINGS_UPDATE_EQUIPMENT_ON_PLAYER_ACTIONS",
                               CollectorInputType.BOOL, Version(1, 21, 4), LATEST_VERSION),
            ],
            "COLLECTOR_HEADER_DEFAULT_RECOMMENDED"
        ))
        self.add_section(CollectorSection(
            "Watchdog",
            [
                CollectorInput("watchdog/early-warning-delay", "COLLECTOR_PAPER_GLOBAL_WATCHDOG_EARLY_WARNING_DELAY",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("watchdog/early-warning-every", "COLLECTOR_PAPER_GLOBAL_WATCHDOG_EARLY_WARNING_EVERY",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
            ]
        ))
