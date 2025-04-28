from mcup.utils.ui.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.utils.version import Version, LATEST_VERSION


class SpigotCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Spigot - General Settings",
            [
                CollectorInput("settings/debug", "Enable debug mode", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/save-user-cache-on-stop-only", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/filter-creative-items", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/moved-wrongly-threshold", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/moved-too-quickly-threshold", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/bungeecord", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/late-bind", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/sample-count", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/player-shuffle", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/user-cache-size", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/int-cache-limit", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/timeout-time", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/restart-on-crash", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/restart-script", "", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/netty-threads", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/maxHealth", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/movementSpeed", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/attackDamage", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Commands",
            [
                CollectorInput("commands/silent-commandblock-console", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/log", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/spam-exclusions", "", CollectorInputType.STRING_LIST, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/replace-commands", "", CollectorInputType.STRING_LIST, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/tab-complete", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Messages",
            [
                CollectorInput("messages/restart", "", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/whitelist", "", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/unknown-command", "", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/server-full", "", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/outdated-client", "", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/outdated-server", "", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Statistics",
            [
                CollectorInput("stats/disable-saving", "", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("stats/forced-stats", "", CollectorInputType.STRING_LIST, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        # TODO: Implement needed functionality to handle correctly lists, etc.
        self.add_section(CollectorSection(
            "Spigot - World Settings",
            [
                CollectorInput("world-settings/default/verbose", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/enable-zombie-pigmen-portal-spawns", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/wither-spawn-sound-radius", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/zombie-aggressive-towards-villager", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hanging-tick-frequency", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/dragon-death-sound-radius", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/mob-spawn-range", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/enabled", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/engine-mode", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/hide-blocks", "", CollectorInputType.INT_LIST, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/replace-blocks", "", CollectorInputType.INT_LIST, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/nerf-spawner-mobs", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/cactus-modifier", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/cane-modifier", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/melon-modifier", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/mushroom-modifier", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/pumpkin-modifier", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/sapling-modifier", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/wheat-modifier", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/animals", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/monsters", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/misc", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/players", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/animals", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/monsters", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/misc", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/other", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hopper-alt-ticking", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/ticks-per/hopper-transfer", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/ticks-per/hopper-check", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hopper-amount", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/random-light-updates", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/save-structure-info", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-bulk-chunks", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-entity-collisions", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/seed-village", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/seed-feature", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/walk-exhaustion", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/sprint-exhaustion", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/combat-exhaustion", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/regen-exhaustion", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tnt-per-tick", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tick-time/tile", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tick-time/entity", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/item-despawn-rate", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/merge-radius/item", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/merge-radius/exp", "", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/arrow-despawn-rate", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/view-distance", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/chunks-per-tick", "", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/clear-tick-list", "", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
            ],
            "Warning: Spigot World Settings aren't fully supported. It's better to use default configuration "
              "and if any edits are needed, edit the file manually."
        ))
