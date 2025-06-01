from mcup.core.configs import ConfigFile
from mcup.core.utils.version import VersionDependantVariablePicker, VersionDependantVariable, Version, LATEST_VERSION


class PaperWorldDefaultsConfig(ConfigFile):
    """Class representing a paper-world-defaults.yml Minecraft server configuration file."""
    def __init__(self):
        """Initialize the paper-world-defaults.yml configuration with default values."""
        self.config_file_name = "paper-world-defaults.yml"
        self.config_file_path = "/config"

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
                        "hide-durability": None,  # 1.19-1.21.3
                        "hide-itemmeta": None,  # 1.19-1.21.3
                        "hide-itemmeta-with-visual-effects": None,  # 1.19.2-1.21.3
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
                "flush-regions-on-save": None,  # 1.19.4+
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
            "command-blocks": {  # 1.20.4+
                "force-follow-perm-level": None,
                "permissions-level": None
            },
            "entities": {
                "armor-stands": {
                    "do-collision-entity-lookups": None,
                    "tick": None
                },
                "behavior": {
                    "allow-spider-world-border-climbing": None,  # 1.19.3+
                    "baby-zombie-movement-modifier": None,
                    "cooldown-failed-beehive-releases": None,  # 1.21.4+
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
                    "only-merge-items-horizontally": None,  # 1.21.1+
                    "parrots-are-unaffected-by-player-movement": None,
                    "phantoms-do-not-spawn-on-creative-players": None,
                    "phantoms-only-attack-insomniacs": None,
                    "phantoms-spawn-attempt-max-seconds": None,  # 1.19.2+
                    "phantoms-spawn-attempt-min-seconds": None,  # 1.19.2+
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
                    "player-insomnia-start-ticks": None,  # 1.19.2+
                    "should-remove-dragon": None,
                    "spawner-nerfed-mobs-should-jump": None,
                    "zombie-villager-infection-chance": None,
                    "zombies-target-turtle-eggs": None
                },
                "entities-target-with-follow-range": None,  # 1.19-1.21.2
                "markers": {
                    "tick": None  # 1.19.4+
                },
                "mob-effects": {
                    "immune-to-wither-effect": {
                        "wither": None,
                        "wither-skeleton": None
                    },
                    "spiders-immune-to-poison-effect": None,
                    "undead-immune-to-certain-effects": None  # 1.19-1.20.4
                },
                "sniffer": {  # 1.20.1+
                    "boosted-hatch-time": None,
                    "hatch-time": None
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
                    "creative-arrow-despawn-rate": None,
                    "despawn-range-shape": None,  # 1.21.1+
                    "despawn-ranges": {
                        "ambient": {
                            "hard": None,
                            "soft": None
                        },
                        "axolotls": {
                            "hard": None,
                            "soft": None
                        },
                        "creature": {
                            "hard": None,
                            "soft": None
                        },
                        "misc": {
                            "hard": None,
                            "soft": None
                        },
                        "monster": {
                            "hard": None,
                            "soft": None
                        },
                        "underground_water_creature": {
                            "hard": None,
                            "soft": None
                        },
                        "water_ambient": {
                            "hard": None,
                            "soft": None
                        },
                        "water_creature": {
                            "hard": None,
                            "soft": None
                        }
                    },
                    "despawn-time": {  # 1.21.3+
                        "llama_spit": None,
                        "snowball": None
                    },
                    "disable-mob-spawner-spawn-egg-transformation": None,
                    "duplicate-uuid": {
                        "mode": None,
                        "safe-regen-delete-range": None
                    },
                    "filter-bad-tile-entity-nbt-from-falling-blocks": None,  # 1.19.3+
                    "filtered-entity-tag-nbt-paths": None,  # 1.19.3+
                    "filter-nbt-data-from-spawn-eggs-and-related": None,  # 1.19-1.19.3
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
                    "ticks-per-spawn": {  # 1.20.4+
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
                },
                "tracking-range-y": {  # 1.20.1+
                    "animal": None,
                    "display": None,
                    "enabled": None,
                    "misc": None,
                    "monster": None,
                    "other": None,
                    "player": None
                }
            },
            "environment": {
                "disable-explosion-knockback": None,
                "disable-ice-and-snow": None,
                "disable-teleportation-suffocation-check": None,  # 1.19-1.21.4
                "disable-thunder": None,
                "fire-tick-delay": None,  # 1.19.2+
                "frosted-ice": {
                    "delay": {
                        "max": None,
                        "min": None
                    },
                    "enabled": None
                },
                "generate-flat-bedrock": None,
                "locate-structures-outside-world-border": None,  # 1.20.4+
                "max-block-ticks": None,  # 1.20.4+
                "max-fluid-ticks": None,  # 1.20.4+
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
                "void-damage-amount": None,  # 1.21.1+
                "void-damage-min-build-height-offset": None,  # 1.21.1+
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
                "restrict-player-reloot": None,
                "restrict-player-reloot-time": None,  # 1.20.1+
                "retain-unlooted-shulker-box-loot-table-on-non-player-break": None  # 1.20.1+
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
                "alternate-current-update-order": None,  # 1.21.1+
                "disable-end-credits": None,
                "disable-relative-projectile-velocity": None,
                "disable-sprint-interruption-on-attack": None,
                "legacy-ender-pearl-behavior": None,  # 1.21.3+
                "light-queue-size": None,  # 1.19-1.21.4
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
                "keep-spawn-loaded": None,  # 1.19-1.20.4
                "keep-spawn-loaded-range": None  # 1.19-1.20.4
            },
            "tick-rates": {
                "behavior": {
                    "villager": {
                        "validatenearbypoi": None
                    }
                },
                "container-update": None,
                "dry-farmland": None,  # 1.20.2+
                "grass-spread": None,
                "mob-spawner": None,
                "sensor": {
                    "villager": {
                        "secondarypoisensor": None
                    }
                },
                "wet-farmland": None  # 1.20.2+
            },
            "unsupported-settings": {
                "disable-world-ticking-when-empty": None,  # 1.20.4+
                "fix-invulnerable-end-crystal-exploit": None
            }
        }

        self.default_configuration = {
            "_version": VersionDependantVariablePicker([
                VersionDependantVariable(Version(1, 19), Version(1, 19, 1), 28),
                VersionDependantVariable(Version(1, 19, 2), Version(1, 19, 2), 29),
                VersionDependantVariable(Version(1, 19, 3), Version(1, 20, 4), 30),
                VersionDependantVariable(Version(1, 20, 6), LATEST_VERSION, 31),
            ]),
            "anticheat": {
                "anti-xray": {
                    "enabled": False,
                    "engine-mode": 1,
                    "hidden-blocks": VersionDependantVariablePicker([
                        VersionDependantVariable(Version(1, 19), Version(1, 20, 1), [
                            "copper_ore", "deepslate_copper_ore", "gold_ore", "deepslate_gold_ore",
                            "iron_ore", "deepslate_iron_ore", "coal_ore", "deepslate_coal_ore",
                            "lapis_ore", "deepslate_lapis_ore", "mossy_cobblestone", "obsidian",
                            "chest", "diamond_ore", "deepslate_diamond_ore", "redstone_ore",
                            "deepslate_redstone_ore", "clay", "emerald_ore", "deepslate_emerald_ore",
                            "ender_chest"
                        ]),
                        VersionDependantVariable(Version(1, 20, 2), LATEST_VERSION, [
                            "copper_ore", "deepslate_copper_ore", "raw_copper_block", "gold_ore", "deepslate_gold_ore",
                            "iron_ore", "deepslate_iron_ore", "raw_iron_block", "coal_ore", "deepslate_coal_ore",
                            "lapis_ore", "deepslate_lapis_ore", "mossy_cobblestone", "obsidian", "chest",
                            "diamond_ore", "deepslate_diamond_ore", "redstone_ore", "deepslate_redstone_ore", "clay",
                            "emerald_ore", "deepslate_emerald_ore", "ender_chest"
                        ])
                    ]),
                    "lava-obscures": False,
                    "max-block-height": 64,
                    "replacement-blocks": ["stone", "oak_planks", "deepslate"],
                    "update-radius": 2,
                    "use-permission": False
                },
                "obfuscation": {
                    "items": {
                        "hide-durability": False,
                        "hide-itemmeta": False,
                        "hide-itemmeta-with-visual-effects": False
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
                "flush-regions-on-save": False,
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
            "command-blocks": {
                "force-follow-perm-level": True,
                "permissions-level": 2
            },
            "entities": {
                "armor-stands": {
                    "do-collision-entity-lookups": True,
                    "tick": True
                },
                "behavior": {
                    "allow-spider-world-border-climbing": True,
                    "baby-zombie-movement-modifier": 0.5,
                    "cooldown-failed-beehive-releases": True,
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
                    "only-merge-items-horizontally": False,
                    "parrots-are-unaffected-by-player-movement": False,
                    "phantoms-do-not-spawn-on-creative-players": True,
                    "phantoms-only-attack-insomniacs": True,
                    "phantoms-spawn-attempt-max-seconds": 119,
                    "phantoms-spawn-attempt-min-seconds": 60,
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
                    "player-insomnia-start-ticks": 72000,
                    "should-remove-dragon": False,
                    "spawner-nerfed-mobs-should-jump": False,
                    "zombie-villager-infection-chance": VersionDependantVariablePicker([
                        VersionDependantVariable(Version(1, 19), Version(1, 20, 1), -1.0),
                        VersionDependantVariable(Version(1, 20, 2), LATEST_VERSION, "default")
                    ]),
                    "zombies-target-turtle-eggs": True
                },
                "entities-target-with-follow-range": False,
                "markers": {
                    "tick": True
                },
                "mob-effects": {
                    "immune-to-wither-effect": {
                        "wither": True,
                        "wither-skeleton": True
                    },
                    "spiders-immune-to-poison-effect": True,
                    "undead-immune-to-certain-effects": True
                },
                "sniffer": {
                    "boosted-hatch-time": "default",
                    "hatch-time": "default"
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
                    "despawn-range-shape": "ELLIPSOID",
                    "despawn-ranges": {
                        "ambient": {
                            "hard": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 128),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ]),
                            "soft": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 32),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ])
                        },
                        "axolotls": {
                            "hard": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 128),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ]),
                            "soft": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 32),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ])
                        },
                        "creature": {
                            "hard": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 128),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ]),
                            "soft": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 32),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ])
                        },
                        "misc": {
                            "hard": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 128),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ]),
                            "soft": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 32),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ])
                        },
                        "monster": {
                            "hard": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 128),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ]),
                            "soft": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 32),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ])
                        },
                        "underground_water_creature": {
                            "hard": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 128),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ]),
                            "soft": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 32),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ])
                        },
                        "water_ambient": {
                            "hard": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 128),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ]),
                            "soft": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 32),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ])
                        },
                        "water_creature": {
                            "hard": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 128),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ]),
                            "soft": VersionDependantVariablePicker([
                                VersionDependantVariable(Version(1, 19), Version(1, 21), 32),
                                VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                            ])
                        }
                    },
                    "despawn-time": {
                        "llama_spit": "disabled",
                        "snowball": "disabled"
                    },
                    "disable-mob-spawner-spawn-egg-transformation": False,
                    "duplicate-uuid": {
                        "mode": "SAFE_REGEN",
                        "safe-regen-delete-range": 32
                    },
                    "filter-bad-tile-entity-nbt-from-falling-blocks": True,
                    "filtered-entity-tag-nbt-paths": ['Pos', 'Motion', 'SleepingX', 'SleepingY', 'SleepingZ'],
                    "filter-nbt-data-from-spawn-eggs-and-related": True,
                    "iron-golems-can-spawn-in-air": False,
                    "monster-spawn-max-light-level": VersionDependantVariablePicker([
                        VersionDependantVariable(Version(1, 19), Version(1, 20, 1), -1),
                        VersionDependantVariable(Version(1, 20, 2), LATEST_VERSION, "default")
                    ]),
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
                    "ticks-per-spawn": {
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
                },
                "tracking-range-y": {
                    "animal": "default",
                    "display": "default",
                    "enabled": False,
                    "misc": "default",
                    "monster": "default",
                    "other": "default",
                    "player": "default"
                }
            },
            "environment": {
                "disable-explosion-knockback": False,
                "disable-ice-and-snow": False,
                "disable-teleportation-suffocation-check": False,
                "disable-thunder": False,
                "fire-tick-delay": 30,
                "frosted-ice": {
                    "delay": {
                        "max": 40,
                        "min": 20
                    },
                    "enabled": True
                },
                "generate-flat-bedrock": False,
                "locate-structures-outside-world-border": False,
                "max-block-ticks": 65536,
                "max-fluid-ticks": 65536,
                "nether-ceiling-void-damage-height": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 19, 1), 0),
                    VersionDependantVariable(Version(1, 19, 2), LATEST_VERSION, "disabled")
                ]),
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
                "void-damage-amount": 4.0,
                "void-damage-min-build-height-offset": -64.0,
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
                "disable-unloaded-chunk-enderpearl-exploit": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 21, 2), True),
                    VersionDependantVariable(Version(1, 21, 3), LATEST_VERSION, False)
                ]),
                "falling-block-height-nerf": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 19, 1), 0),
                    VersionDependantVariable(Version(1, 19, 2), LATEST_VERSION, "disabled")
                ]),
                "fix-curing-zombie-villager-discount-exploit": True,  # 1.19-1.20.1
                "fix-items-merging-through-walls": False,
                "prevent-tnt-from-moving-in-water": False,
                "split-overstacked-loot": True,
                "tnt-entity-height-nerf": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 19, 1), 0),
                    VersionDependantVariable(Version(1, 19, 2), LATEST_VERSION, "disabled")
                ])
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
                "restrict-player-reloot": True,
                "restrict-player-reloot-time": "disabled",
                "retain-unlooted-shulker-box-loot-table-on-non-player-break": True
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
                "alternate-current-update-order": "HORIZONTAL_FIRST_OUTWARD",
                "disable-end-credits": False,
                "disable-relative-projectile-velocity": False,
                "disable-sprint-interruption-on-attack": False,
                "legacy-ender-pearl-behavior": False,
                "light-queue-size": 20,
                "max-leash-distance": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 21), 10.0),
                    VersionDependantVariable(Version(1, 21, 1), LATEST_VERSION, "default")
                ]),
                "redstone-implementation": "VANILLA",
                "shield-blocking-delay": 5,
                "show-sign-click-command-failure-msgs-to-player": False,
                "update-pathfinding-on-block-update": True
            },
            "scoreboards": {
                "allow-non-player-entities-on-scoreboards": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 19, 3), False),
                    VersionDependantVariable(Version(1, 19, 4), LATEST_VERSION, True)
                ]),
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
                "dry-farmland": 1,
                "grass-spread": 1,
                "mob-spawner": 1,
                "sensor": {
                    "villager": {
                        "secondarypoisensor": 40
                    }
                },
                "wet-farmland": 1
            },
            "unsupported-settings": {
                "disable-world-ticking-when-empty": False,
                "fix-invulnerable-end-crystal-exploit": True
            }
        }
