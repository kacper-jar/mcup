from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInputType, CollectorInput
from mcup.core.utils.version import Version, LATEST_VERSION


class PaperWorldDefaultsCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Paper (World Defaults) - Anticheat",
            [
                CollectorInput("anticheat/anti-xray/enabled", "", CollectorInputType.BOOL,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("anticheat/anti-xray/engine-mode", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("anticheat/anti-xray/hidden-blocks", "", CollectorInputType.STRING_LIST,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("anticheat/anti-xray/lava-obscures", "", CollectorInputType.BOOL,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("anticheat/anti-xray/max-block-height", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("anticheat/anti-xray/replacement-blocks", "", CollectorInputType.STRING_LIST,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("anticheat/anti-xray/update-radius", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("anticheat/anti-xray/use-permission", "", CollectorInputType.BOOL,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("anticheat/obfuscation/items/hide-durability", "", CollectorInputType.BOOL,
                               Version(1, 19), Version(1, 21, 3)),
                CollectorInput("anticheat/obfuscation/items/hide-itemmeta", "", CollectorInputType.BOOL,
                               Version(1, 19), Version(1, 21, 3)),
                CollectorInput("anticheat/obfuscation/items/hide-itemmeta-with-visual-effects", "",
                               CollectorInputType.BOOL, Version(1, 19, 2), Version(1, 21, 3))
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (World Defaults) - Chunks",
            [
                CollectorInput("chunks/auto-save-interval", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/delay-chunk-unloads-by", "", CollectorInputType.STRING,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/entity-per-chunk-save-limit/arrow", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/entity-per-chunk-save-limit/ender_pearl", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/entity-per-chunk-save-limit/experience_orb", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/entity-per-chunk-save-limit/fireball", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/entity-per-chunk-save-limit/small_fireball", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/entity-per-chunk-save-limit/snowball", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/fixed-chunk-inhabited-time", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/flush-regions-on-save", "", CollectorInputType.BOOL,
                               Version(1, 19, 4), LATEST_VERSION),
                CollectorInput("chunks/max-auto-save-chunks-per-tick", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("chunks/prevent-moving-into-unloaded-chunks", "", CollectorInputType.BOOL,
                               Version(1, 19), LATEST_VERSION)
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (World Defaults) - Collisions",
            [
                CollectorInput("collisions/allow-player-cramming-damage", "", CollectorInputType.BOOL,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("collisions/allow-vehicle-collisions", "", CollectorInputType.BOOL,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("collisions/fix-climbing-bypassing-cramming-rule", "", CollectorInputType.BOOL,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("collisions/max-entity-collisions", "", CollectorInputType.INT,
                               Version(1, 19), LATEST_VERSION),
                CollectorInput("collisions/only-players-collide", "", CollectorInputType.BOOL,
                               Version(1, 19), LATEST_VERSION)
            ]
        ))
        self.add_section(CollectorSection(
            "Paper (World Defaults) - Command Blocks",
            [
                CollectorInput("command-blocks/force-follow-perm-level", "", CollectorInputType.BOOL,
                               Version(1, 20, 4), LATEST_VERSION),
                CollectorInput("command-blocks/permissions-level", "", CollectorInputType.INT,
                               Version(1, 20, 4), LATEST_VERSION)
            ]
        ))
