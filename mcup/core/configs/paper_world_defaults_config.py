from mcup.core.configs import ConfigFile


class PaperWorldDefaultsConfig(ConfigFile):
    """Class representing a paper-world-defaults.yml Minecraft server configuration file."""
    def __init__(self):
        """Initialize the paper-world-defaults.yml configuration with default values."""
        self.config_file_name = "paper-world-defaults.yml"
        self.config_file_path = "."

        self.configuration = {
            "_version": None,  # <--- This needs to be changed based on the server version.
            "anticheat": {
                "anti-xray": {
                    "enabled": None,
                    "engine-mode": None,
                    "hidden-blocks": None,
                    "lava-obscures": None,
                    "max-block-height": None,
                    "replacement-blocks": None,
                    "update-radius": None,
                    "use-permission": None
                },
                "obfuscation": {
                    "items": {
                        "hide-durability": None,
                        "hide-itemmeta": None
                    }
                }
            },
            "chunks": {
                "auto-save-interval": None,
                "delay-chunk-unloads-by": None,
                "entity-per-chunk-save-limit": {
                    "arrow": None,
                    "ender_pearl": None,
                    "experience_orb": None,
                    "fireball": None,
                    "small_fireball": None,
                    "snowball": None
                },
                "fixed-chunk-inhabited-time": None,
                "max-auto-save-chunks-per-tick": None,
                "prevent-moving-into-unloaded-chunks": None
            },
            "collisions": {
                "allow-player-cramming-damage": None,
                "allow-vehicle-collisions": None,
                "fix-climbing-bypassing-cramming-rule": None,
                "max-entity-collisions": None,
                "only-players-collide": None
            },
            "entities": {
                "armor-stands": {
                    "do-collision-entity-lookups": None,
                    "tick": None
                },
                "behavior": {
                    "baby-zombie-movement-modifier": None,
                    "disable-chest-cat-detection": None,
                    "disable-creeper-lingering-effect": None,
                    "disable-player-crits": None,
                    "door-breaking-difficulty": {
                        "husk": None,
                        "vindicator": None,
                        "zombie": None,
                        "zombie_villager": None,
                        "zombified_piglin": None
                    },
                    "ender-dragons-death-always-places-dragon-egg": None,
                    "experience-merge-max-value": None,
                    "mobs-can-always-pick-up-loot": {
                        "skeletons": None,
                        "zombies": None
                    },
                    "nerf-pigmen-from-nether-portals": None,
                    "parrots-are-unaffected-by-player-movement": None,
                    "phantoms-do-not-spawn-on-creative-players": None,
                    "phantoms-only-attack-insomniacs": None,
                    "piglins-guard-chests": None,
                    "pillager-patrols": {
                        "disable": None,
                        "spawn-chance": None,
                        "spawn-delay": {
                            "per-player": None,
                            "ticks": None
                        },
                        "start": {
                            "day": None,
                            "per-player": None
                        }
                    },
                    "should-remove-dragon": None,
                    "spawner-nerfed-mobs-should-jump": None,
                    "zombie-villager-infection-chance": None,
                    "zombies-target-turtle-eggs": None
                },
                "entities-target-with-follow-range": None,
                "mob-effects": {
                    "immune-to-wither-effect": {
                        "wither": None,
                        "wither-skeleton": None
                    },
                    "spiders-immune-to-poison-effect": None,
                    "undead-immune-to-certain-effects": None
                },
                "spawning": {
                    "all-chunks-are-slime-chunks": None,
                    "alt-item-despawn-rate": {
                        "enabled": None,
                        "items": {
                            "cobblestone": None
                        }
                    },
                    "count-all-mobs-for-spawning": None,
                    "creative-arrow-despawn-rate": "default",
                    "despawn-ranges": {
                        "ambient": {
                            "hard": 128,
                            "soft": 32
                        },
                        "axolotls": {
                            "hard": 128,
                            "soft": 32
                        },
                        "creature": {
                            "hard": 128,
                            "soft": 32
                        },
                        "misc": {
                            "hard": 128,
                            "soft": 32
                        },
                        "monster": {
                            "hard": 128,
                            "soft": 32
                        },
                        "underground_water_creature": {
                            "hard": 128,
                            "soft": 32
                        },
                        "water_ambient": {
                            "hard": 64,
                            "soft": 32
                        },
                        "water_creature": {
                            "hard": 128,
                            "soft": 32
                        }
                    },
                    "disable-mob-spawner-spawn-egg-transformation": None,
                    "duplicate-uuid": {
                        "mode": None,
                        "safe-regen-delete-range": None
                    },
                    "filter-nbt-data-from-spawn-eggs-and-related": None,
                    "iron-golems-can-spawn-in-air": None,
                    "monster-spawn-max-light-level": None,
                    "non-player-arrow-despawn-rate": None,
                    "per-player-mob-spawns": None,
                    "scan-for-legacy-ender-dragon": None,
                    "skeleton-horse-thunder-spawn-chance": None,
                    "slime-spawn-height": {
                        "slime-chunk": {
                            "maximum": None
                        },
                        "surface-biome": {
                            "maximum": None,
                            "minimum": None
                        }
                    },
                    "spawn-limits": {
                        "ambient": None,
                        "axolotls": None,
                        "creature": None,
                        "monster": None,
                        "underground_water_creature": None,
                        "water_ambient": None,
                        "water_creature": None
                    },
                    "wandering-trader": {
                        "spawn-chance-failure-increment": None,
                        "spawn-chance-max": None,
                        "spawn-chance-min": None,
                        "spawn-day-length": None,
                        "spawn-minute-length": None
                    },
                    "wateranimal-spawn-height": {
                        "maximum": None,
                        "minimum": None
                    }
                }
            },
            "environment": {
                "disable-explosion-knockback": None,
                "disable-ice-and-snow": None,
                "disable-teleportation-suffocation-check": None,
                "disable-thunder": None,
                "frosted-ice": {
                    "delay": {
                        "max": None,
                        "min": None
                    },
                    "enabled": None
                },
                "generate-flat-bedrock": None,
                "nether-ceiling-void-damage-height": None,
                "optimize-explosions": None,
                "portal-create-radius": None,
                "portal-search-radius": None,
                "portal-search-vanilla-dimension-scaling": None,
                "treasure-maps": {
                    "enabled": None,
                    "find-already-discovered": {
                        "loot-tables": None,
                        "villager-trade": None
                    }
                },
                "water-over-lava-flow-speed": None
            },
            "feature-seeds": {
                "generate-random-seeds-for-all": None
            },
            "fishing-time-range": {
                "maximum": None,
                "minimum": None
            },
            "fixes": {
                "disable-unloaded-chunk-enderpearl-exploit": None,
                "falling-block-height-nerf": None,
                "fix-curing-zombie-villager-discount-exploit": None,
                "fix-items-merging-through-walls": None,
                "prevent-tnt-from-moving-in-water": None,
                "split-overstacked-loot": None,
                "tnt-entity-height-nerf": None
            },
            "hopper": {
                "cooldown-when-full": None,
                "disable-move-event": None,
                "ignore-occluding-blocks": None
            },
            "lootables": {
                "auto-replenish": None,
                "max-refills": None,
                "refresh-max": None,
                "refresh-min": None,
                "reset-seed-on-fill": None,
                "restrict-player-reloot": None
            },
            "maps": {
                "item-frame-cursor-limit": None,
                "item-frame-cursor-update-interval": None
            },
            "max-growth-height": {
                "bamboo": {
                    "max": None,
                    "min": None
                },
                "cactus": None,
                "reeds": None
            },
            "misc": {
                "disable-end-credits": None,
                "disable-relative-projectile-velocity": None,
                "disable-sprint-interruption-on-attack": None,
                "light-queue-size": None,
                "max-leash-distance": None,
                "redstone-implementation": None,
                "shield-blocking-delay": None,
                "show-sign-click-command-failure-msgs-to-player": None,
                "update-pathfinding-on-block-update": None
            },
            "scoreboards": {
                "allow-non-player-entities-on-scoreboards": None,
                "use-vanilla-world-scoreboard-name-coloring": None
            },
            "spawn": {
                "allow-using-signs-inside-spawn-protection": None,
                "keep-spawn-loaded": None,
                "keep-spawn-loaded-range": None
            },
            "tick-rates": {
                "behavior": {
                    "villager": {
                        "validatenearbypoi": None
                    }
                },
                "container-update": None,
                "grass-spread": None,
                "mob-spawner": None,
                "sensor": {
                    "villager": {
                        "secondarypoisensor": None
                    }
                }
            },
            "unsupported-settings": {
                "fix-invulnerable-end-crystal-exploit": None
            }
        }

        self.default_configuration = {
            "_version": 28,
            "anticheat": {
                "anti-xray": {
                    "enabled": False,
                    "engine-mode": 1,
                    "hidden-blocks": [
                        "copper_ore", "deepslate_copper_ore", "gold_ore", "deepslate_gold_ore",
                        "iron_ore", "deepslate_iron_ore", "coal_ore", "deepslate_coal_ore",
                        "lapis_ore", "deepslate_lapis_ore", "mossy_cobblestone", "obsidian",
                        "chest", "diamond_ore", "deepslate_diamond_ore", "redstone_ore",
                        "deepslate_redstone_ore", "clay", "emerald_ore", "deepslate_emerald_ore",
                        "ender_chest"
                    ],
                    "lava-obscures": False,
                    "max-block-height": 64,
                    "replacement-blocks": ["stone", "oak_planks", "deepslate"],
                    "update-radius": 2,
                    "use-permission": False
                },
                "obfuscation": {
                    "items": {
                        "hide-durability": False,
                        "hide-itemmeta": False
                    }
                }
            },
            "chunks": {
                "auto-save-interval": "default",
                "delay-chunk-unloads-by": "10s",
                "entity-per-chunk-save-limit": {
                    "arrow": -1,
                    "ender_pearl": -1,
                    "experience_orb": -1,
                    "fireball": -1,
                    "small_fireball": -1,
                    "snowball": -1
                },
                "fixed-chunk-inhabited-time": -1,
                "max-auto-save-chunks-per-tick": 24,
                "prevent-moving-into-unloaded-chunks": False
            },
            "collisions": {
                "allow-player-cramming-damage": False,
                "allow-vehicle-collisions": True,
                "fix-climbing-bypassing-cramming-rule": False,
                "max-entity-collisions": 8,
                "only-players-collide": False
            },
            "entities": {
                "armor-stands": {
                    "do-collision-entity-lookups": True,
                    "tick": True
                },
                "behavior": {
                    "baby-zombie-movement-modifier": 0.5,
                    "disable-chest-cat-detection": False,
                    "disable-creeper-lingering-effect": False,
                    "disable-player-crits": False,
                    "door-breaking-difficulty": {
                        "husk": ["HARD"],
                        "vindicator": ["NORMAL", "HARD"],
                        "zombie": ["HARD"],
                        "zombie_villager": ["HARD"],
                        "zombified_piglin": ["HARD"]
                    },
                    "ender-dragons-death-always-places-dragon-egg": False,
                    "experience-merge-max-value": -1,
                    "mobs-can-always-pick-up-loot": {
                        "skeletons": False,
                        "zombies": False
                    },
                    "nerf-pigmen-from-nether-portals": False,
                    "parrots-are-unaffected-by-player-movement": False,
                    "phantoms-do-not-spawn-on-creative-players": True,
                    "phantoms-only-attack-insomniacs": True,
                    "piglins-guard-chests": True,
                    "pillager-patrols": {
                        "disable": False,
                        "spawn-chance": 0.2,
                        "spawn-delay": {
                            "per-player": False,
                            "ticks": 12000
                        },
                        "start": {
                            "day": 5,
                            "per-player": False
                        }
                    },
                    "should-remove-dragon": False,
                    "spawner-nerfed-mobs-should-jump": False,
                    "zombie-villager-infection-chance": -1.0,
                    "zombies-target-turtle-eggs": True
                },
                "entities-target-with-follow-range": False,
                "mob-effects": {
                    "immune-to-wither-effect": {
                        "wither": True,
                        "wither-skeleton": True
                    },
                    "spiders-immune-to-poison-effect": True,
                    "undead-immune-to-certain-effects": True
                },
                "spawning": {
                    "all-chunks-are-slime-chunks": False,
                    "alt-item-despawn-rate": {
                        "enabled": False,
                        "items": {
                            "cobblestone": 300
                        }
                    },
                    "count-all-mobs-for-spawning": False,
                    "creative-arrow-despawn-rate": "default",
                    "despawn-ranges": {
                        "ambient": {
                            "hard": 128,
                            "soft": 32
                        },
                        "axolotls": {
                            "hard": 128,
                            "soft": 32
                        },
                        "creature": {
                            "hard": 128,
                            "soft": 32
                        },
                        "misc": {
                            "hard": 128,
                            "soft": 32
                        },
                        "monster": {
                            "hard": 128,
                            "soft": 32
                        },
                        "underground_water_creature": {
                            "hard": 128,
                            "soft": 32
                        },
                        "water_ambient": {
                            "hard": 64,
                            "soft": 32
                        },
                        "water_creature": {
                            "hard": 128,
                            "soft": 32
                        }
                    },
                    "disable-mob-spawner-spawn-egg-transformation": False,
                    "duplicate-uuid": {
                        "mode": "SAFE_REGEN",
                        "safe-regen-delete-range": 32
                    },
                    "filter-nbt-data-from-spawn-eggs-and-related": True,
                    "iron-golems-can-spawn-in-air": False,
                    "monster-spawn-max-light-level": -1,
                    "non-player-arrow-despawn-rate": "default",
                    "per-player-mob-spawns": True,
                    "scan-for-legacy-ender-dragon": True,
                    "skeleton-horse-thunder-spawn-chance": "default",
                    "slime-spawn-height": {
                        "slime-chunk": {
                            "maximum": 40.0
                        },
                        "surface-biome": {
                            "maximum": 70.0,
                            "minimum": 50.0
                        }
                    },
                    "spawn-limits": {
                        "ambient": -1,
                        "axolotls": -1,
                        "creature": -1,
                        "monster": -1,
                        "underground_water_creature": -1,
                        "water_ambient": -1,
                        "water_creature": -1
                    },
                    "wandering-trader": {
                        "spawn-chance-failure-increment": 25,
                        "spawn-chance-max": 75,
                        "spawn-chance-min": 25,
                        "spawn-day-length": 24000,
                        "spawn-minute-length": 1200
                    },
                    "wateranimal-spawn-height": {
                        "maximum": "default",
                        "minimum": "default"
                    }
                }
            },
            "environment": {
                "disable-explosion-knockback": False,
                "disable-ice-and-snow": False,
                "disable-teleportation-suffocation-check": False,
                "disable-thunder": False,
                "frosted-ice": {
                    "delay": {
                        "max": 40,
                        "min": 20
                    },
                    "enabled": True
                },
                "generate-flat-bedrock": False,
                "nether-ceiling-void-damage-height": 0,
                "optimize-explosions": False,
                "portal-create-radius": 16,
                "portal-search-radius": 128,
                "portal-search-vanilla-dimension-scaling": True,
                "treasure-maps": {
                    "enabled": True,
                    "find-already-discovered": {
                        "loot-tables": "default",
                        "villager-trade": False
                    }
                },
                "water-over-lava-flow-speed": 5
            },
            "feature-seeds": {
                "generate-random-seeds-for-all": False
            },
            "fishing-time-range": {
                "maximum": 600,
                "minimum": 100
            },
            "fixes": {
                "disable-unloaded-chunk-enderpearl-exploit": True,
                "falling-block-height-nerf": 0,
                "fix-curing-zombie-villager-discount-exploit": True,
                "fix-items-merging-through-walls": False,
                "prevent-tnt-from-moving-in-water": False,
                "split-overstacked-loot": True,
                "tnt-entity-height-nerf": 0
            },
            "hopper": {
                "cooldown-when-full": True,
                "disable-move-event": False,
                "ignore-occluding-blocks": False
            },
            "lootables": {
                "auto-replenish": False,
                "max-refills": -1,
                "refresh-max": "2d",
                "refresh-min": "12h",
                "reset-seed-on-fill": True,
                "restrict-player-reloot": True
            },
            "maps": {
                "item-frame-cursor-limit": 128,
                "item-frame-cursor-update-interval": 10
            },
            "max-growth-height": {
                "bamboo": {
                    "max": 16,
                    "min": 11
                },
                "cactus": 3,
                "reeds": 3
            },
            "misc": {
                "disable-end-credits": False,
                "disable-relative-projectile-velocity": False,
                "disable-sprint-interruption-on-attack": False,
                "light-queue-size": 20,
                "max-leash-distance": 10.0,
                "redstone-implementation": "VANILLA",
                "shield-blocking-delay": 5,
                "show-sign-click-command-failure-msgs-to-player": False,
                "update-pathfinding-on-block-update": True
            },
            "scoreboards": {
                "allow-non-player-entities-on-scoreboards": False,
                "use-vanilla-world-scoreboard-name-coloring": False
            },
            "spawn": {
                "allow-using-signs-inside-spawn-protection": False,
                "keep-spawn-loaded": True,
                "keep-spawn-loaded-range": 10
            },
            "tick-rates": {
                "behavior": {
                    "villager": {
                        "validatenearbypoi": -1
                    }
                },
                "container-update": 1,
                "grass-spread": 1,
                "mob-spawner": 1,
                "sensor": {
                    "villager": {
                        "secondarypoisensor": 40
                    }
                }
            },
            "unsupported-settings": {
                "fix-invulnerable-end-crystal-exploit": True
            }
        }
