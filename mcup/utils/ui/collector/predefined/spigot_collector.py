from mcup.utils.ui.collector import Collector, CollectorSection, CollectorInput
from mcup.utils.version import Version, LATEST_VERSION


class SpigotCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Spigot - General Settings",
            [
                CollectorInput("settings/debug", "Enable debug mode", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/save-user-cache-on-stop-only", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/filter-creative-items", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/moved-wrongly-threshold", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/moved-too-quickly-threshold", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/bungeecord", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/late-bind", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/sample-count", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/player-shuffle", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/user-cache-size", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/int-cache-limit", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/timeout-time", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/restart-on-crash", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/restart-script", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/netty-threadst", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/maxHealth", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/movementSpeed", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/attackDamage", "", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Commands",
            [
                CollectorInput("commands/silent-commandblock-console", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/log", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/spam-exclusions", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/replace-commands", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/tab-complete", "", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Messages",
            [
                CollectorInput("messages/restart", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/whitelist", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/unknown-command", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/server-full", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/outdated-client", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/outdated-server", "", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Statistics",
            [
                CollectorInput("stats/disable-saving", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("stats/forced-stats", "", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        # TODO: Implement needed functionality to handle correctly lists, etc.
        print("Warning: Spigot World Settings aren't fully supported. It's better to use default configuration "
              "and if any edits are needed, edit the file manually.")
        self.add_section(CollectorSection(
            "Spigot - World Settings",
            [
                CollectorInput("world-settings/default/verbose", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/enable-zombie-pigmen-portal-spawns", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/wither-spawn-sound-radius", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/zombie-aggressive-towards-villager", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hanging-tick-frequency", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/dragon-death-sound-radius", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/mob-spawn-range", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/enabled", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/engine-mode", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/hide-blocks", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/replace-blocks", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/nerf-spawner-mobs", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/cactus-modifier", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/cane-modifier", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/melon-modifier", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/mushroom-modifier", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/pumpkin-modifier", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/sapling-modifier", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/wheat-modifier", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/animals", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/monsters", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/misc", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/players", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/animals", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/monsters", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/misc", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/other", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hopper-alt-ticking", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/ticks-per/hopper-transfer", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/ticks-per/hopper-check", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hopper-amount", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/random-light-updates", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/save-structure-info", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-bulk-chunks", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-entity-collisions", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/seed-village", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/seed-feature", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/walk-exhaustion", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/sprint-exhaustion", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/combat-exhaustion", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/regen-exhaustion", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tnt-per-tick", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tick-time/tile", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tick-time/entity", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/item-despawn-rate", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/merge-radius/item", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/merge-radius/exp", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/arrow-despawn-rate", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/view-distance", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/chunks-per-tick", "", Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/clear-tick-list", "", Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
