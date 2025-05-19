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

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Console",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Item Validation",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Logging",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Messages",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Misc",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Packet Limiter",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Player Auto-save",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Proxies",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Scoreboards",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Spam Limiter",
            [

            ]
        ))
        self.add_section(CollectorSection(
            "Paper (Global) - Spark",
            [

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
