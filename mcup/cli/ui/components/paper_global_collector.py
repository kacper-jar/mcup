from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.core.utils.version import Version, LATEST_VERSION


class PaperGlobalCollector(Collector):
    def __init__(self):
        super().__init__()

        # TODO: implement collector section for anticheat

        self.add_section(CollectorSection(
            "Paper (Global) - Block Updates",
            [
                CollectorInput("block-updates/disable-chorus-plant-updates", "Disable block updates for chorus plants",
                               CollectorInputType.BOOL, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("block-updates/disable-mushroom-block-updates",
                               "Disable block updates for mushroom blocks",
                               CollectorInputType.BOOL, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("block-updates/disable-noteblock-updates", "Disable block updates for noteblocks",
                               CollectorInputType.BOOL, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("block-updates/disable-tripwire-updates", "Disable block updates for tripwires",
                               CollectorInputType.BOOL, Version(1, 20, 1), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Chunk System & Chunk Loading",
            [
                CollectorInput("async-chunks/threads", "Async chunks loading threads", CollectorInputType.INT,
                               Version(1, 19), Version(1, 19, 1)),
                CollectorInput("chunk-loading/autoconfig-send-distance", "Auto config chunk send distance",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/enable-frustum-priority", "", CollectorInputType.BOOL,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/global-max-chunk-load-rate", "", CollectorInputType.INT,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/global-max-chunk-send-rate", "", CollectorInputType.INT,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/global-max-concurrent-loads", "", CollectorInputType.INT,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/min-load-radius", "", CollectorInputType.INT,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/player-max-chunk-load-rate", "", CollectorInputType.INT,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/player-max-concurrent-loads", "", CollectorInputType.INT,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading/target-player-chunk-send-rate", "", CollectorInputType.INT,
                               Version(1, 19), Version(1, 19, 4)),
                CollectorInput("chunk-loading-advanced/auto-config-send-distance", "Auto config chunk send distance",
                               CollectorInputType.BOOL, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-advanced/player-max-concurrent-chunk-generates", "",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-advanced/player-max-concurrent-chunk-loads", "",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-basic/player-max-chunk-generate-rate", "",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-basic/player-max-chunk-load-rate", "",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-loading-basic/player-max-chunk-send-rate", "",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-system/gen-parallelism", "",
                               CollectorInputType.BOOL, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-system/io-threads", "",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
                CollectorInput("chunk-system/worker-threads", "",
                               CollectorInputType.INT, Version(1, 20), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Collisions",
            [
                CollectorInput("collisions/enable-player-collisions", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("collisions/send-full-pos-for-hard-colliding-entities", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION)
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Commands",
            [
                CollectorInput("commands/fix-target-selector-tag-completion", "",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 21, 3)),
                CollectorInput("commands/ride-command-allow-player-as-vehicle", "",
                               CollectorInputType.BOOL, Version(1, 21, 4), LATEST_VERSION),
                CollectorInput("commands/suggest-player-names-when-null-tab-completions", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("commands/time-command-affects-all-worlds", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Console",
            [
                CollectorInput("console/enable-brigadier-completions", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("console/enable-brigadier-highlighting", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("console/has-all-permissions", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Item Validation",
            [
                CollectorInput("item-validation/book/author", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/book/page", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/book/title", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/book-size/page-max", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/book-size/total-multiplier", "",
                               CollectorInputType.FLOAT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/display-name", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/lore-line", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("item-validation/resolve-selectors-in-books", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Logging",
            [
                CollectorInput("logging/deobfuscate-stacktraces", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("logging/log-player-ip-addresses", "",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 20, 1)),
                CollectorInput("logging/use-rgb-for-named-text-colors", "",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 19, 4)),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Messages",
            [
                CollectorInput("messages/kick/authentication-servers-down", "",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/kick/connection-throttle", "",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/kick/flying-player", "",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/kick/flying-vehicle", "",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/no-permission", "",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
                CollectorInput("messages/use-display-name-in-quit-message", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Misc",
            [
                CollectorInput("misc/chat-threads/chat-executor-core-size", "",
                               CollectorInputType.INT, Version(1, 19, 2), LATEST_VERSION),
                CollectorInput("misc/chat-threads/chat-executor-max-size", "",
                               CollectorInputType.INT, Version(1, 19, 2), LATEST_VERSION),
                CollectorInput("misc/client-interaction-leniency-distance", "",
                               CollectorInputType.INT, Version(1, 21), LATEST_VERSION),
                CollectorInput("misc/compression-level", "",
                               CollectorInputType.STRING, Version(1, 20, 1), LATEST_VERSION),
                CollectorInput("misc/fix-entity-position-desync", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/lag-compensate-block-breaking", "",
                               CollectorInputType.BOOL, Version(1, 19), Version(1, 20)),
                CollectorInput("misc/load-permissions-yml-before-plugins", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/max-joins-per-tick", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/region-file-cache-size", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/strict-advancement-dimension-check", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/use-alternative-luck-formula", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("misc/use-dimension-type-for-custom-spawners", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        # TODO: implement collector section for packet-limiter
        self.add_section(CollectorSection(
            "Paper (Global) - Player Auto-save",
            [
                CollectorInput("player-auto-save/max-per-tick", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("player-auto-save/rate", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Proxies",
            [
                CollectorInput("proxies/bungee-cord/online-mode", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("proxies/proxy-protocol", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("proxies/velocity/enabled", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("proxies/velocity/online-mode", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("proxies/velocity/secret", "",
                               CollectorInputType.STRING, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Scoreboards",
            [
                CollectorInput("scoreboards/save-empty-scoreboard-teams", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
                CollectorInput("scoreboards/track-plugin-scoreboards", "",
                               CollectorInputType.BOOL, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Spam Limiter",
            [
                CollectorInput("spam-limiter/incoming-packet-threshold", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("spam-limiter/recipe-spam-increment", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("spam-limiter/recipe-spam-limit", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("spam-limiter/tab-spam-increment", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
                CollectorInput("spam-limiter/tab-spam-limit", "",
                               CollectorInputType.INT, Version(1, 19), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Spark",
            [
                CollectorInput("spark/enable-immediately", "",
                               CollectorInputType.BOOL, Version(1, 21), LATEST_VERSION),
                CollectorInput("spark/enabled", "",
                               CollectorInputType.BOOL, Version(1, 21), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Timings",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Unsupported (Legacy) Settings",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Watchdog",
            [

            ]
        ))
