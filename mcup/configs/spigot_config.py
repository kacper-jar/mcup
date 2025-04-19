from mcup.configs import ConfigFile


class SpigotConfig(ConfigFile):
    """Class representing a spigot.yml Minecraft server configuration file."""
    def __init__(self):
        """Initialize the spigot.yml configuration with default values."""
        self.config_file_name = "spigot.yml"
        self.config_file_path = "."

        self.configuration = {
            "config-version": None,
            "settings": {
                "debug": None,
                "save-user-cache-on-stop-only": None,
                "filter-creative-items": None,
                "moved-wrongly-threshold": None,
                "moved-too-quickly-threshold": None,
                "bungeecord": None,
                "late-bind": None,
                "sample-count": None,
                "player-shuffle": None,
                "user-cache-size": None,
                "int-cache-limit": None,
                "timeout-time": None,
                "restart-on-crash": None,
                "restart-script": None,
                "netty-threads": None,
                "attribute": {
                    "maxHealth": {"max": None},
                    "movementSpeed": {"max": None},
                    "attackDamage": {"max": None}
                }
            },
            "commands": {
                "silent-commandblock-console": None,
                "log": None,
                "spam-exclusions": None,
                "replace-commands": None,
                "tab-complete": None
            },
            "messages": {
                "restart": None,
                "whitelist": None,
                "unknown-command": None,
                "server-full": None,
                "outdated-client": None,
                "outdated-server": None
            },
            "stats": {
                "disable-saving": None,
                "forced-stats": None
            },
            "world-settings": {
                "default": {
                    "verbose": None,
                    "enable-zombie-pigmen-portal-spawns": None,
                    "wither-spawn-sound-radius": None,
                    "zombie-aggressive-towards-villager": None,
                    "hanging-tick-frequency": None,
                    "dragon-death-sound-radius": None,
                    "mob-spawn-range": None,
                    "anti-xray": {
                        "enabled": None,
                        "engine-mode": None,
                        "hide-blocks": None,
                        "replace-blocks": None
                    },
                    "nerf-spawner-mobs": None,
                    "growth": {
                        "cactus-modifier": None,
                        "cane-modifier": None,
                        "melon-modifier": None,
                        "mushroom-modifier": None,
                        "pumpkin-modifier": None,
                        "sapling-modifier": None,
                        "wheat-modifier": None
                    },
                    "entity-activation-range": {
                        "animals": None,
                        "monsters": None,
                        "misc": None
                    },
                    "entity-tracking-range": {
                        "players": None,
                        "animals": None,
                        "monsters": None,
                        "misc": None,
                        "other": None
                    },
                    "hopper-alt-ticking": None,
                    "ticks-per": {
                        "hopper-transfer": None,
                        "hopper-check": None
                    },
                    "hopper-amount": None,
                    "random-light-updates": None,
                    "save-structure-info": None,
                    "max-bulk-chunks": None,
                    "max-entity-collisions": None,
                    "seed-village": None,
                    "seed-feature": None,
                    "hunger": {
                        "walk-exhaustion": None,
                        "sprint-exhaustion": None,
                        "combat-exhaustion": None,
                        "regen-exhaustion": None
                    },
                    "max-tnt-per-tick": None,
                    "max-tick-time": {
                        "tile": None,
                        "entity": None
                    },
                    "item-despawn-rate": None,
                    "merge-radius": {
                        "item": None,
                        "exp": None
                    },
                    "arrow-despawn-rate": None,
                    "view-distance": None,
                    "chunks-per-tick": None,
                    "clear-tick-list": None
                }
            }
        }

        self.default_configuration = {
            "config-version": 8,
            "settings": {
                "debug": False,
                "save-user-cache-on-stop-only": False,
                "filter-creative-items": True,
                "moved-wrongly-threshold": 0.0625,
                "moved-too-quickly-threshold": 100.0,
                "bungeecord": False,
                "late-bind": False,
                "sample-count": 12,
                "player-shuffle": 0,
                "user-cache-size": 1000,
                "int-cache-limit": 1024,
                "timeout-time": 60,
                "restart-on-crash": True,
                "restart-script": "./start.sh",
                "netty-threads": 4,
                "attribute": {
                    "maxHealth": {"max": 2048.0},
                    "movementSpeed": {"max": 2048.0},
                    "attackDamage": {"max": 2048.0}
                }
            },
            "commands": {
                "silent-commandblock-console": False,
                "log": True,
                "spam-exclusions": ["/skill"],
                "replace-commands": ["setblock", "summon", "testforblock", "tellraw"],
                "tab-complete": 0
            },
            "messages": {
                "restart": "Server is restarting",
                "whitelist": "You are not whitelisted on this server!",
                "unknown-command": 'Unknown command. Type "/help" for help.',
                "server-full": "The server is full!",
                "outdated-client": "Outdated client! Please use {0}",
                "outdated-server": "Outdated server! I'm still on {0}"
            },
            "stats": {
                "disable-saving": False,
                "forced-stats": {}
            },
            "world-settings": {
                "default": {
                    "verbose": True,
                    "enable-zombie-pigmen-portal-spawns": True,
                    "wither-spawn-sound-radius": 0,
                    "zombie-aggressive-towards-villager": True,
                    "hanging-tick-frequency": 100,
                    "dragon-death-sound-radius": 0,
                    "mob-spawn-range": 4,
                    "anti-xray": {
                        "enabled": True,
                        "engine-mode": 1,
                        "hide-blocks": [14, 15, 16, 21, 48, 49, 54, 56, 73, 74, 82, 129, 130],
                        "replace-blocks": [1, 5]
                    },
                    "nerf-spawner-mobs": False,
                    "growth": {
                        "cactus-modifier": 100,
                        "cane-modifier": 100,
                        "melon-modifier": 100,
                        "mushroom-modifier": 100,
                        "pumpkin-modifier": 100,
                        "sapling-modifier": 100,
                        "wheat-modifier": 100
                    },
                    "entity-activation-range": {
                        "animals": 32,
                        "monsters": 32,
                        "misc": 16
                    },
                    "entity-tracking-range": {
                        "players": 48,
                        "animals": 48,
                        "monsters": 48,
                        "misc": 32,
                        "other": 64
                    },
                    "hopper-alt-ticking": False,
                    "ticks-per": {
                        "hopper-transfer": 8,
                        "hopper-check": 8
                    },
                    "hopper-amount": 1,
                    "random-light-updates": False,
                    "save-structure-info": True,
                    "max-bulk-chunks": 10,
                    "max-entity-collisions": 8,
                    "seed-village": 10387312,
                    "seed-feature": 14357617,
                    "hunger": {
                        "walk-exhaustion": 0.2,
                        "sprint-exhaustion": 0.8,
                        "combat-exhaustion": 0.3,
                        "regen-exhaustion": 3.0
                    },
                    "max-tnt-per-tick": 100,
                    "max-tick-time": {
                        "tile": 50,
                        "entity": 50
                    },
                    "item-despawn-rate": 6000,
                    "merge-radius": {
                        "item": 2.5,
                        "exp": 3.0
                    },
                    "arrow-despawn-rate": 1200,
                    "view-distance": 10,
                    "chunks-per-tick": 650,
                    "clear-tick-list": False
                }
            }
        }
