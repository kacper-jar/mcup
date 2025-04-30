from mcup.utils.ui.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.utils.version import Version, LATEST_VERSION


class SpigotCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Spigot - General Settings",
            [
                CollectorInput("settings/debug", "Enable debug mode", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/save-user-cache-on-stop-only", "Save user cache on stop", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/filter-creative-items", "Filter creative items", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/moved-wrongly-threshold", "Moved wrongly warning threshold", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/moved-too-quickly-threshold", "Moved too quickly warning threshold", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/bungeecord", "Use Bungeecord", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/late-bind", "Delay players from entering server untill all plugins are loaded", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/sample-count", "Amount of player names displayed on server list", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/player-shuffle", "Shuffle players on relog", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/user-cache-size", "User cache size", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/int-cache-limit", "Int cache limit", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/timeout-time", "Timeout time", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/restart-on-crash", "Automatically restart on server crash", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/restart-script", "Restart crash", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/netty-threads", "Netty threads", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/maxHealth", "Max health", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/movementSpeed", "Max movement speed", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("settings/attribute/attackDamage", "Max attack damage", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Commands",
            [
                CollectorInput("commands/silent-commandblock-console", "Send command block output to console", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/log", "Send player commands to console", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/spam-exclusions", "Commands excepted from chat spam filter", CollectorInputType.STRING_LIST, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/replace-commands", "Commands to use vanilla implementations", CollectorInputType.STRING_LIST, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("commands/tab-complete", "Amount of letters before TAB completes", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Messages",
            [
                CollectorInput("messages/restart", "Message for server restart", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/whitelist", "Message for player not whitelisted", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/unknown-command", "Message for unknown command", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/server-full", "Message for full server", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/outdated-client", "Message for outdated client", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("messages/outdated-server", "Message for outdated server", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - Statistics",
            [
                CollectorInput("stats/disable-saving", "Disable achievement saving", CollectorInputType.STRING, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("stats/forced-stats", "Forced statistics", CollectorInputType.STRING_LIST, Version(1, 8, 0), LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Spigot - World Settings",
            [
                CollectorInput("world-settings/default/verbose", "Show detailed report in console", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/enable-zombie-pigmen-portal-spawns", "Spawn zombie pigmen in portals", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/wither-spawn-sound-radius", "Wither spawn sound radius", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/zombie-aggressive-towards-villager", "Zombie aggressive towards villagers", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hanging-tick-frequency", "Tick update interval for hanging entities", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/dragon-death-sound-radius", "Dragon death sound radius", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/mob-spawn-range", "Mob spawn range in chunks", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/enabled", "Enable anti-xray", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/engine-mode", "Anti-Xray engine version", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/hide-blocks", "Block IDs to hide using anti-xray", CollectorInputType.INT_LIST, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/anti-xray/replace-blocks", "Block IDs to replace using anti-xray", CollectorInputType.INT_LIST, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/nerf-spawner-mobs", "Nerf spawner mobs", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/cactus-modifier", "Cactus growth modifier", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/cane-modifier", "Cane growth modifier", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/melon-modifier", "Melon growth modifier", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/mushroom-modifier", "Mushroom growth modifier", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/pumpkin-modifier", "Pumpkin growth modifier", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/sapling-modifier", "Sapling growth modifier", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/growth/wheat-modifier", "Wheat growth modifier", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/animals", "Animals activation range", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/monsters", "Monsters activation range", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-activation-range/misc", "Misc entities activation range", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/players", "Players tracking range", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/animals", "Animals tracking range", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/monsters", "Monsters tracking range", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/misc", "Misc entities tracking range", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/entity-tracking-range/other", "other entities tracking range", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hopper-alt-ticking", "Hopper alt ticking", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/ticks-per/hopper-transfer", "Ticks per hopper transfer", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/ticks-per/hopper-check", "Ticks per hopper check", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hopper-amount", "Max items transferred via hoppers on single tick", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/random-light-updates", "Random light updates", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/save-structure-info", "Save structure info", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-bulk-chunks", "Amount of chunks sent per packet", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-entity-collisions", "Max entity collisions per tick", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/seed-village", "Villages seed", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/seed-feature", "Structures seed", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/walk-exhaustion", "Hunger points taken on walk", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/sprint-exhaustion", "Hunger points taken on sprint", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/combat-exhaustion", "Hunger points taken on combat", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/hunger/regen-exhaustion", "Hunger points taken on regen", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tnt-per-tick", "Max TNT per tick", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tick-time/tile", "Max tick time for tile", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/max-tick-time/entity", "Max tick time for entity", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/item-despawn-rate", "Item despawn rate", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/merge-radius/item", "Item merge radius", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/merge-radius/exp", "Exp merge radius", CollectorInputType.FLOAT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/arrow-despawn-rate", "Arrow despawn rate", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/view-distance", "View distance", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/chunks-per-tick", "Chunks updated for growth per tick", CollectorInputType.INT, Version(1, 8, 0), LATEST_VERSION),
                CollectorInput("world-settings/default/clear-tick-list", "Clear tick list", CollectorInputType.BOOL, Version(1, 8, 0), LATEST_VERSION),
            ],
            "Warning: It's recommended to leave all these settings as default"
        ))
