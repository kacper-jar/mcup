from mcup.core.configs import ConfigFile
from mcup.core.utils.version import Version, LATEST_VERSION, VersionDependantVariable


class PaperConfig(ConfigFile):
    """Class representing a paper.yml Minecraft server configuration file."""
    def __init__(self):
        """Initialize the paper.yml configuration with default values."""
        self.config_file_name = "paper.yml"
        self.config_file_path = "."

        self.configuration = {
            "messages": {
                "kick": {
                    "authentication-servers-down": None,
                    "connection-throttle": None,
                    "flying-player": None,
                    "flying-vehicle": None
                },
                "no-permission": None,
            },
            "timings": {
                "enabled": None,
                "verbose": None,
                "server-name": None,
                "server-name-privacy": None,
                "hidden-config-entries": None,
                "history-interval": None,
                "history-length": None,
                "url": None,
            },
            "config-version": None,
            "effect-modifiers": {
                "strength": None,
                "weakness": None
            },
            "stackable-buckets": {
                "lava": None,
                "water": None,
                "milk": None
            },
            "settings": {
                "baby-zombie-movement-speed": None,
                "limit-player-interactions": None,
                "book-size": {
                    "page-max": None,
                    "total-multiplier": None
                },
                "spam-limiter": {
                    "tab-spam-increment": None,
                    "tab-spam-limit": None,
                    "recipe-spam-increment": None,
                    "recipe-spam-limit": None
                },
                "watchdog": {
                    "early-warning-every": None,
                    "early-warning-delay": None
                },
                "async-chunks": {
                    "enable": None,
                    "generation": None,
                    "thread-per-world-generation": None,
                    "load-threads": None,
                    "threads": None
                },
                "velocity-support": {
                    "enabled": None,
                    "online-mode": None,
                    "secret": None
                },
                "console": {
                    "enable-brigadier-highlighting": None,
                    "enable-brigadier-completions": None
                },
                "item-validation": {
                    "display-name": None,
                    "loc-name": None,
                    "lore-line": None,
                    "book": {
                        "title": None,
                        "author": None,
                        "page": None
                    }
                },
                "chunk-loading": {
                    "min-load-radius": None,
                    "max-concurrent-sends": None,
                    "autoconfig-send-distance": None,
                    "target-player-chunk-send-rate": None,
                    "global-max-chunk-send-rate": None,
                    "enable-frustum-priority": None,
                    "global-max-chunk-load-rate": None,
                    "player-max-concurrent-loads": None,
                    "global-max-concurrent-loads": None,
                    "player-max-chunk-load-rate": None
                },
                "loggers": {
                    "deobfuscate-stacktraces": None,
                    "use-rgb-for-named-text-colors": None
                },
                "packet-limiter": {
                    "kick-message": None,
                    "limits": None
                },
                "unsupported-settings": {
                    "allow-piston-duplication": None,
                    "allow-permanent-block-break-exploits": None,
                    "allow-permanent-block-break-exploits-readme": None,
                    "allow-piston-duplication-readme": None,
                    "allow-headless-pistons": None,
                    "allow-headless-pistons-readme": None,
                    "perform-username-validation": None,
                    "fix-invulnerable-end-crystal-exploit": None
                },
                "player-auto-save-rate": None,
                "remove-invalid-statistics": None,
                "save-player-data": None,
                "suggest-player-names-when-null-tab-completions": None,
                "use-alternative-luck-formula": None,
                "use-versioned-world": None,
                "min-chunk-load-threads": None,
                "queue-light-updates-max-loss": None,
                "sleep-between-chunk-saves": None,
                "chunk-tasks-per-tick": None,
                "max-joins-per-tick": None,
                "console-has-all-permissions": None,
                "track-plugin-scoreboards": None,
                "fix-entity-position-desync": None,
                "use-display-name-in-quit-message": None,
                "lag-compensate-block-breaking": None,
                "log-player-ip-addresses": None,
                "send-full-pos-for-hard-colliding-entities": None,
                "fix-target-selector-tag-completion": None,
                "time-command-affects-all-worlds": None,
                "use-dimension-type-for-custom-spawners": None,
                "proxy-protocol": None,
                "resolve-selectors-in-books": None,
                "max-player-auto-save-per-tick": None
            },
            "warnWhenSettingExcessiveVelocity": None,
            "data-value-allowed-items": None,
            "verbose": None,
            "allow-perm-block-break-exploits": None,
            "use-display-name-in-quit-message": None,
            "world-settings": {
                "default": {
                    "verbose": None,
                    "use-hopper-check": None,
                    "disable-mood-sounds": None,
                    "fix-cannons": None,
                    "optimize-explosions": None,
                    "mob-spawner-tick-rate": None,
                    "cache-chunk-maps": None,
                    "squid-spawn-height": {
                        "minimum": None,
                        "maximum": None
                    },
                    "tnt-explosion-volume": None,
                    "max-growth-height": {
                        "cactus": None,
                        "reeds": None,
                        "bamboo": {
                            "max": None,
                            "min": None
                        }
                    },
                    "fishing-time-range": {
                        "MinimumTicks": None,
                        "MaximumTicks": None
                    },
                    "player-exhaustion": {
                        "block-break": None,
                        "swimming": None
                    },
                    "despawn-ranges": {
                        "soft": None,
                        "hard": None,
                        "ambient": {
                            "soft": None,
                            "hard": None
                        },
                        "creature": {
                            "soft": None,
                            "hard": None
                        },
                        "misc": {
                            "soft": None,
                            "hard": None
                        },
                        "monster": {
                            "soft": None,
                            "hard": None
                        },
                        "underground_water_creature": {
                            "soft": None,
                            "hard": None
                        },
                        "water_ambient": {
                            "soft": None,
                            "hard": None
                        },
                        "water_creature": {
                            "soft": None,
                            "hard": None
                        },
                        "axolotls": {
                            "soft": None,
                            "hard": None
                        }
                    },
                    "remove-unloaded": {
                        "enderpearls": None,
                        "tnt-entities": None,
                        "falling-blocks": None
                    },
                    "game-mechanics": {
                        "boats-drop-boats": None,
                        "disable-player-crits": None,
                        "disable-chest-cat-detection": None,
                        "disable-end-credits": None,
                        "allow-permanent-chunk-loaders": None,
                        "disable-sprint-interruption-on-attack": None,
                        "disable-unloaded-chunk-enderpearl-exploit": None,
                        "scan-for-legacy-ender-dragon": None,
                        "shield-blocking-delay": None,
                        "village-sieges-enabled": None,
                        "villages-load-chunks": None,
                        "disable-relative-projectile-velocity": None,
                        "disable-pillager-patrols": None,
                        "nerf-pigmen-from-nether-portals": None,
                        "pillager-patrols": {
                            "spawn-chance": None,
                            "spawn-delay": {
                                "per-player": None,
                                "ticks": None
                            },
                            "start": {
                                "per-player": None,
                                "day": None
                            }
                        },
                        "disable-mob-spawner-spawn-egg-transformation": None,
                        "fix-curing-zombie-villager-discount-exploit": None
                    },
                    "load-chunks": {
                        "enderpearls": None,
                        "tnt-entities": None,
                        "falling-blocks": None
                    },
                    "fast-drain": {
                        "lava": None,
                        "water": None
                    },
                    "lava-flow-speed": {
                        "normal": None,
                        "nether": None
                    },
                    "use-async-lighting": None,
                    "portal-search-radius": None,
                    "disable-thunder": None,
                    "disable-ice-and-snow": None,
                    "tick-next-tick-list-cap": None,
                    "tick-next-tick-list-cap-ignores-redstone": None,
                    "keep-spawn-loaded": None,
                    "generator-settings": {
                        "canyon": None,
                        "caves": None,
                        "dungeon": None,
                        "fortress": None,
                        "mineshaft": None,
                        "monument": None,
                        "stronghold": None,
                        "temple": None,
                        "village": None,
                        "flat-bedrock": None,
                        "disable-extreme-hills-emeralds": None,
                        "disable-extreme-hills-monster-eggs": None,
                        "disable-mesa-additional-gold": None
                    },
                    "remove-invalid-mob-spawner-tile-entities": None,
                    "player-blocking-damage-multiplier": None,
                    "falling-block-height-nerf": None,
                    "nether-ceiling-void-damage": None,
                    "all-chunks-are-slime-chunks": None,
                    "allow-undead-horse-leashing": None,
                    "container-update-tick-rate": None,
                    "falling-blocks-collide-with-signs": None,
                    "allow-block-location-tab-completion": None,
                    "disable-explosion-knockback": None,
                    "tnt-entity-height-nerf": None,
                    "water-over-lava-flow-speed": None,
                    "disable-teleportation-suffocation-check": None,
                    "armor-stands-do-collision-entity-lookups": None,
                    "enable-treasure-maps": None,
                    "max-entity-collisions": None,
                    "treasure-maps-return-already-discovered": None,
                    "anti-xray": {
                        "enabled": None,
                        "engine-mode": None,
                        "chunk-edge-mode": None,
                        "max-chunk-section-index": None,
                        "update-radius": None,
                        "hidden-blocks": None,
                        "replacement-blocks": None,
                        "lava-obscures": None,
                        "use-permission": None,
                        "max-block-height": None
                    },
                    "armor-stands-tick": None,
                    "bed-search-radius": None,
                    "disable-creeper-lingering-effect": None,
                    "duplicate-uuid-resolver": None,
                    "duplicate-uuid-saferegen-delete-range": None,
                    "experience-merge-max-value": None,
                    "hopper": {
                        "cooldown-when-full": None,
                        "disable-move-event": None,
                        "push-based": None,
                        "ignore-occluding-blocks": None
                    },
                    "max-chunk-gens-per-tick": None,
                    "max-chunk-sends-per-tick": None,
                    "parrots-are-unaffected-by-player-movement": None,
                    "prevent-moving-into-unloaded-chunks": None,
                    "prevent-tnt-from-moving-in-water": None,
                    "skip-entity-ticking-in-chunks-scheduled-for-unload": None,
                    "skeleton-horse-thunder-spawn-chance": None,
                    "creative-arrow-despawn-rate": None,
                    "villages-load-chunks": None,
                    "lightning-strike-distance-limit": {
                        "sound": None,
                        "impact-sound": None,
                        "flash": None
                    },
                    "count-all-mobs-for-spawning": None,
                    "fixed-chunk-inhabited-time": None,
                    "nether-ceiling-void-damage-height": None,
                    "use-chunk-inhabited-timer": None,
                    "use-faster-eigencraft-redstone": None,
                    "auto-save-interval": None,
                    "delay-chunk-unloads-by": None,
                    "keep-spawn-loaded-range": None,
                    "max-auto-save-chunks-per-tick": None,
                    "queue-light-updates": None,
                    "save-queue-limit-for-auto-save": None,
                    "fire-physics-event-for-redstone": None,
                    "alt-item-despawn-rate": {
                        "enabled": None,
                        "items": None
                    },
                    "baby-zombie-movement-modifier": None,
                    "fix-zero-tick-instant-grow-farms": None,
                    "per-player-mob-spawns": None,
                    "entities-target-with-follow-range": None,
                    "portal-create-radius": None,
                    "iron-golems-can-spawn-in-air": None,
                    "light-queue-size": None,
                    "phantoms-do-not-spawn-on-creative-players": None,
                    "phantoms-only-attack-insomniacs": None,
                    "seed-based-feature-search": None,
                    "viewdistances": {
                        "no-tick-view-distance": None
                    },
                    "zombie-villager-infection-chance": None,
                    "zombies-target-turtle-eggs": None,
                    "door-breaking-difficulty": {
                        "zombie": None,
                        "vindicator": None,
                        "husk": None,
                        "zombie_villager": None,
                        "zombified_piglin": None,
                    },
                    "entity-per-chunk-save-limit": {
                        "experience_orb": None,
                        "snowball": None,
                        "ender_pearl": None,
                        "arrow": None,
                        "fireball": None,
                        "small_fireball": None
                    },
                    "fix-climbing-bypassing-cramming-rule": None,
                    "mobs-can-always-pick-up-loot": {
                        "zombies": None,
                        "skeletons": None
                    },
                    "portal-search-vanilla-dimension-scaling": None,
                    "should-remove-dragon": None,
                    "wandering-trader": {
                        "spawn-minute-length": None,
                        "spawn-day-length": None,
                        "spawn-chance-failure-increment": None,
                        "spawn-chance-min": None,
                        "spawn-chance-max": None
                    },
                    "allow-using-signs-inside-spawn-protection": None,
                    "allow-vehicle-collisions": None,
                    "ender-dragons-death-always-places-dragon-egg": None,
                    "fix-items-merging-through-walls": None,
                    "fix-wither-targeting-bug": None,
                    "map-item-frame-cursor-limit": None,
                    "max-leash-distance": None,
                    "only-players-collide": None,
                    "seed-based-feature-search-loads-chunks": None,
                    "show-sign-click-command-failure-msgs-to-player": None,
                    "spawn-limits": {
                        "monsters": None,
                        "animals": None,
                        "water-animals": None,
                        "water-ambient": None,
                        "ambient": None,
                        "creature": None,
                        "monster": None,
                        "underground_water_creature": None,
                        "water_ambient": None,
                        "water_creature": None,
                        "axolotls": None
                    },
                    "update-pathfinding-on-block-update": None,
                    "allow-player-cramming-damage": None,
                    "feature-seeds": {
                        "generate-random-seeds-for-all": None
                    },
                    "map-item-frame-cursor-update-interval": None,
                    "mob-effects": {
                        "undead-immune-to-certain-effects": None,
                        "spiders-immune-to-poison-effect": None,
                        "immune-to-wither-effect": {
                            "wither": None,
                            "wither-skeleton": None
                        }
                    },
                    "piglins-guard-chests": None,
                    "split-overstacked-loot": None,
                    "tick-rates": {
                        "sensor": {
                            "villager": {
                                "secondarypoisensor": None
                            }
                        },
                        "behavior": {
                            "villager": {
                                "validatenearbypoi": None
                            }
                        }
                    },
                    "anticheat": {
                        "obfuscation": {
                            "items": {
                                "hide-itemmeta": None,
                                "hide-durability": None
                            }
                        }
                    },
                    "monster-spawn-max-light-level": None,
                    "slime-spawn-height": {
                        "swamp-biome": {
                            "maximum": None,
                            "minimum": None
                        },
                        "slime-chunk": {
                            "maximum": None
                        }
                    },
                    "wateranimal-spawn-height": {
                        "maximum": None,
                        "minimum": None
                    },
                    "redstone-implementation": None,
                    "treasure-maps-find-already-discovered": {
                        "villager-trade": None,
                        "loot-tables": None
                    }
                }
            }
        }


        self.default_configuration = {
            "messages": {
                "kick": {
                    "authentication-servers-down": "",
                    "connection-throttle": "Connection throttled! Please wait before reconnecting.",
                    "flying-player": "Flying is not enabled on this server",
                    "flying-vehicle": "Flying is not enabled on this server"
                },
                "no-permission": "&cI'm sorry, but you do not have permission to perform this command. Please contact the server administrators if you believe that this is in error.",
            },
            "timings": {
                "enabled": True,
                "verbose": True,
                "server-name": "Unknown Server",
                "server-name-privacy": False,
                "hidden-config-entries": [
                    VersionDependantVariable(Version(1, 8, 8), Version(1, 16, 2),
                                             ["database", "settings.bungeecord-addresses",
                                              "settings.velocity-support.secret"]),
                    VersionDependantVariable(Version(1, 16, 2), Version(1, 16, 3),
                                             ["database", "settings.bungeecord-addresses"]),
                    VersionDependantVariable(Version(1, 16, 3), LATEST_VERSION,
                                             ["database", "settings.bungeecord-addresses",
                                              "settings.velocity-support.secret"])
                ],
                "history-interval": 300,
                "history-length": 3600,
                "url": "https://timings.aikar.co/",
            },
            "config-version": 27,
            "effect-modifiers": {
                "strength": 1.3,
                "weakness": -0.5
            },
            "stackable-buckets": {
                "lava": False,
                "water": False,
                "milk": False
            },
            "settings": {
                "baby-zombie-movement-speed": 0.5,
                "limit-player-interactions": True,
                "book-size": {
                    "page-max": 2560,
                    "total-multiplier": 0.98
                },
                "spam-limiter": {
                    "tab-spam-increment": [
                        VersionDependantVariable(Version(1, 8, 8), Version(1, 13, 0), 10),
                        VersionDependantVariable(Version(1, 13, 0), Version(1, 13, 1), 2),
                        VersionDependantVariable(Version(1, 13, 1), LATEST_VERSION, 1)
                    ],
                    "tab-spam-limit": 500,
                    "recipe-spam-increment": 1,
                    "recipe-spam-limit": 20
                },
                "watchdog": {
                    "early-warning-every": 5000,
                    "early-warning-delay": 10000
                },
                "async-chunks": {
                    "enable": True,
                    "generation": True,
                    "thread-per-world-generation": True,
                    "load-threads": -1,
                    "threads": -1
                },
                "velocity-support": {
                    "enabled": False,
                    "online-mode": False,
                    "secret": ""
                },
                "console": {
                    "enable-brigadier-highlighting": True,
                    "enable-brigadier-completions": True
                },
                "item-validation": {
                    "display-name": 8192,
                    "loc-name": 8192,
                    "lore-line": 8192,
                    "book": {
                        "title": 8192,
                        "author": 8192,
                        "page": 16384
                    }
                },
                "chunk-loading": {
                    "min-load-radius": 2,
                    "max-concurrent-sends": 2,
                    "autoconfig-send-distance": True,
                    "target-player-chunk-send-rate": 100.0,
                    "global-max-chunk-send-rate": -1.0,
                    "enable-frustum-priority": False,
                    "global-max-chunk-load-rate": -1.0,
                    "player-max-concurrent-loads": [
                        VersionDependantVariable(Version(1, 8, 8), Version(1, 18, 1), 4.0),
                        VersionDependantVariable(Version(1, 18, 1), LATEST_VERSION, 20.0)
                    ],
                    "global-max-concurrent-loads": 500.0,
                    "player-max-chunk-load-rate": -1.0
                },
                "loggers": {
                    "deobfuscate-stacktraces": True,
                    "use-rgb-for-named-text-colors": True
                },
                "packet-limiter": {
                    "kick-message": "&cSent too many packets",
                    "limits": {
                        "all": {"interval": 7.0, "max-packet-rate": 500.0},
                        "PacketPlayInAutoRecipe": {"interval": 4.0, "max-packet-rate": 5.0, "action": "DROP"}
                    }
                },
                "unsupported-settings": {
                    "allow-piston-duplication": False,
                    "allow-permanent-block-break-exploits": False,
                    "allow-permanent-block-break-exploits-readme": "This setting controls if players should be able to break bedrock, end portals and other intended to be permanent blocks.",
                    "allow-piston-duplication-readme": "This setting controls if player should be able to use TNT duplication, but this also allows duplicating carpet, rails and potentially other items",
                    "allow-headless-pistons": False,
                    "allow-headless-pistons-readme": "This setting controls if players should be able to create headless pistons.",
                    "perform-username-validation": True,
                    "fix-invulnerable-end-crystal-exploit": True
                },
                "player-auto-save-rate": -1,
                "remove-invalid-statistics": False,
                "save-player-data": True,
                "suggest-player-names-when-null-tab-completions": True,
                "use-alternative-luck-formula": False,
                "use-versioned-world": False,
                "min-chunk-load-threads": 2,
                "queue-light-updates-max-loss": 10,
                "sleep-between-chunk-saves": False,
                "chunk-tasks-per-tick": 1000,
                "max-joins-per-tick": 3,
                "console-has-all-permissions": False,
                "track-plugin-scoreboards": False,
                "fix-entity-position-desync": True,
                "use-display-name-in-quit-message": False,
                "lag-compensate-block-breaking": True,
                "log-player-ip-addresses": True,
                "send-full-pos-for-hard-colliding-entities": True,
                "fix-target-selector-tag-completion": True,
                "time-command-affects-all-worlds": False,
                "use-dimension-type-for-custom-spawners": False,
                "proxy-protocol": False,
                "resolve-selectors-in-books": False,
                "max-player-auto-save-per-tick": -1
            },
            "warnWhenSettingExcessiveVelocity": True,
            "data-value-allowed-items": [],
            "verbose": False,
            "allow-perm-block-break-exploits": False,
            "use-display-name-in-quit-message": False,
            "world-settings": {
                "default": {
                    "verbose": True,
                    "use-hopper-check": False,
                    "disable-mood-sounds": False,
                    "fix-cannons": False,
                    "optimize-explosions": False,
                    "mob-spawner-tick-rate": 1,
                    "cache-chunk-maps": False,
                    "squid-spawn-height": {
                        "minimum": 45.0,
                        "maximum": [
                            VersionDependantVariable(Version(1, 8, 8), Version(1, 12, 2), 63.0),
                            VersionDependantVariable(Version(1, 12, 2), LATEST_VERSION, 0.0)
                        ]
                    },
                    "tnt-explosion-volume": 4.0,
                    "max-growth-height": {
                        "cactus": 3,
                        "reeds": 3,
                        "bamboo": {
                            "max": 16,
                            "min": 11
                        }
                    },
                    "fishing-time-range": {
                        "MinimumTicks": 100,
                        "MaximumTicks": [
                            VersionDependantVariable(Version(1, 8, 8), Version(1, 11, 2), 900),
                            VersionDependantVariable(Version(1, 11, 2), LATEST_VERSION, 600)
                        ]
                    },
                    "player-exhaustion": {
                        "block-break": 0.02500000037252903,
                        "swimming": 0.014999999664723873
                    },
                    "despawn-ranges": {
                        "soft": 32,
                        "hard": 128,
                        "ambient": {"soft": 32, "hard": 128},
                        "creature": {"soft": 32, "hard": 128},
                        "misc": {"soft": 32, "hard": 128},
                        "monster": {"soft": 32, "hard": 128},
                        "underground_water_creature": {"soft": 32, "hard": 128},
                        "water_ambient": {"soft": 32, "hard": 64},
                        "water_creature": {"soft": 32, "hard": 128},
                        "axolotls": {"soft": 32, "hard": 128}
                    },
                    "remove-unloaded": {
                        "enderpearls": True,
                        "tnt-entities": True,
                        "falling-blocks": True
                    },
                    "game-mechanics": {
                        "boats-drop-boats": False,
                        "disable-player-crits": False,
                        "disable-chest-cat-detection": False,
                        "disable-end-credits": False,
                        "allow-permanent-chunk-loaders": False,
                        "disable-sprint-interruption-on-attack": False,
                        "disable-unloaded-chunk-enderpearl-exploit": True,
                        "scan-for-legacy-ender-dragon": True,
                        "shield-blocking-delay": 5,
                        "village-sieges-enabled": True,
                        "villages-load-chunks": False,
                        "disable-relative-projectile-velocity": False,
                        "disable-pillager-patrols": False,
                        "nerf-pigmen-from-nether-portals": False,
                        "pillager-patrols": {
                            "spawn-chance": 0.2,
                            "spawn-delay": {
                                "per-player": False,
                                "ticks": 12000
                            },
                            "start": {
                                "per-player": False,
                                "day": 5
                            }
                        },
                        "disable-mob-spawner-spawn-egg-transformation": False,
                        "fix-curing-zombie-villager-discount-exploit": True
                    },
                    "load-chunks": {
                        "enderpearls": False,
                        "tnt-entities": False,
                        "falling-blocks": False
                    },
                    "fast-drain": {
                        "lava": False,
                        "water": False
                    },
                    "lava-flow-speed": {
                        "normal": 30,
                        "nether": 10
                    },
                    "use-async-lighting": False,
                    "portal-search-radius": 128,
                    "disable-thunder": False,
                    "disable-ice-and-snow": False,
                    "tick-next-tick-list-cap": 10000,
                    "tick-next-tick-list-cap-ignores-redstone": False,
                    "keep-spawn-loaded": True,
                    "generator-settings": {
                        "canyon": True,
                        "caves": True,
                        "dungeon": True,
                        "fortress": True,
                        "mineshaft": True,
                        "monument": True,
                        "stronghold": True,
                        "temple": True,
                        "village": True,
                        "flat-bedrock": False,
                        "disable-extreme-hills-emeralds": False,
                        "disable-extreme-hills-monster-eggs": False,
                        "disable-mesa-additional-gold": False
                    },
                    "remove-invalid-mob-spawner-tile-entities": True,
                    "player-blocking-damage-multiplier": 0.5,
                    "falling-block-height-nerf": 0,
                    "nether-ceiling-void-damage": False,
                    "all-chunks-are-slime-chunks": False,
                    "allow-undead-horse-leashing": False,
                    "container-update-tick-rate": 1,
                    "falling-blocks-collide-with-signs": False,
                    "allow-block-location-tab-completion": True,
                    "disable-explosion-knockback": False,
                    "tnt-entity-height-nerf": 0,
                    "water-over-lava-flow-speed": 5,
                    "disable-teleportation-suffocation-check": False,
                    "armor-stands-do-collision-entity-lookups": True,
                    "enable-treasure-maps": True,
                    "max-entity-collisions": 8,
                    "treasure-maps-return-already-discovered": False,
                    "anti-xray": {
                        "enabled": False,
                        "engine-mode": 1,
                        "chunk-edge-mode": [
                            VersionDependantVariable(Version(1, 8, 8), Version(1, 13, 2), 1),
                            VersionDependantVariable(Version(1, 13, 2), LATEST_VERSION, 2)
                        ],
                        "max-chunk-section-index": 3,
                        "update-radius": 2,
                        "hidden-blocks": [
                            VersionDependantVariable(Version(1, 8, 8), Version(1, 17, 1),
                                                     ['gold_ore', 'iron_ore', 'coal_ore', 'lapis_ore',
                                                      'mossy_cobblestone', 'obsidian', 'chest', 'diamond_ore',
                                                      'redstone_ore', 'clay', 'emerald_ore', 'ender_chest']),
                            VersionDependantVariable(Version(1, 17, 1), LATEST_VERSION,
                                                     ['copper_ore', 'deepslate_copper_ore', 'gold_ore',
                                                      'deepslate_gold_ore', 'iron_ore', 'deepslate_iron_ore',
                                                      'coal_ore', 'deepslate_coal_ore', 'lapis_ore',
                                                      'deepslate_lapis_ore', 'mossy_cobblestone', 'obsidian', 'chest',
                                                      'diamond_ore', 'deepslate_diamond_ore', 'redstone_ore',
                                                      'deepslate_redstone_ore', 'clay', 'emerald_ore',
                                                      'deepslate_emerald_ore', 'ender_chest'])
                        ],
                        "replacement-blocks": [
                            VersionDependantVariable(Version(1, 8, 8), Version(1, 17, 1), ['stone', 'oak_planks']),
                            VersionDependantVariable(Version(1, 17, 1), LATEST_VERSION,
                                                     ['stone', 'oak_planks', 'deepslate'])
                        ],
                        "lava-obscures": False,
                        "use-permission": False,
                        "max-block-height": 64
                    },
                    "armor-stands-tick": True,
                    "bed-search-radius": 1,
                    "disable-creeper-lingering-effect": False,
                    "duplicate-uuid-resolver": "saferegen",
                    "duplicate-uuid-saferegen-delete-range": 32,
                    "experience-merge-max-value": -1,
                    "hopper": {
                        "cooldown-when-full": True,
                        "disable-move-event": False,
                        "push-based": False,
                        "ignore-occluding-blocks": [
                            VersionDependantVariable(Version(1, 8, 8), Version(1, 18, 1), True),
                            VersionDependantVariable(Version(1, 18, 1), LATEST_VERSION, False)
                        ]
                    },
                    "max-chunk-gens-per-tick": 10,
                    "max-chunk-sends-per-tick": 81,
                    "parrots-are-unaffected-by-player-movement": False,
                    "prevent-moving-into-unloaded-chunks": False,
                    "prevent-tnt-from-moving-in-water": False,
                    "skip-entity-ticking-in-chunks-scheduled-for-unload": True,
                    "skeleton-horse-thunder-spawn-chance": [
                        VersionDependantVariable(Version(1, 8, 8), Version(1, 11, 2), -1.0),
                        VersionDependantVariable(Version(1, 11, 2), LATEST_VERSION, 0.01)
                    ],
                    "creative-arrow-despawn-rate": -1,
                    "villages-load-chunks": False,
                    "lightning-strike-distance-limit": {
                        "sound": -1,
                        "impact-sound": -1,
                        "flash": -1
                    },
                    "count-all-mobs-for-spawning": False,
                    "fixed-chunk-inhabited-time": -1,
                    "nether-ceiling-void-damage-height": 0,
                    "use-chunk-inhabited-timer": True,
                    "use-faster-eigencraft-redstone": False,
                    "auto-save-interval": -1,
                    "delay-chunk-unloads-by": "10s",
                    "keep-spawn-loaded-range": 10,
                    "max-auto-save-chunks-per-tick": 24,
                    "queue-light-updates": False,
                    "save-queue-limit-for-auto-save": 50,
                    "fire-physics-event-for-redstone": False,
                    "alt-item-despawn-rate": {
                        "enabled": False,
                        "items": {"COBBLESTONE": 300}
                    },
                    "baby-zombie-movement-modifier": 0.5,
                    "fix-zero-tick-instant-grow-farms": True,
                    "per-player-mob-spawns": [
                        VersionDependantVariable(Version(1, 8, 8), Version(1, 17, 1), False),
                        VersionDependantVariable(Version(1, 17, 1), LATEST_VERSION, True)
                    ],
                    "entities-target-with-follow-range": False,
                    "portal-create-radius": 16,
                    "iron-golems-can-spawn-in-air": False,
                    "light-queue-size": 20,
                    "phantoms-do-not-spawn-on-creative-players": True,
                    "phantoms-only-attack-insomniacs": True,
                    "seed-based-feature-search": True,
                    "viewdistances": {"no-tick-view-distance": -1},
                    "zombie-villager-infection-chance": -1.0,
                    "zombies-target-turtle-eggs": True,
                    "door-breaking-difficulty": {
                        "zombie": ["HARD"],
                        "vindicator": ["NORMAL", "HARD"],
                        "husk": ["HARD"],
                        "zombie_villager": ["HARD"],
                        "zombified_piglin": ["HARD"]
                    },
                    "entity-per-chunk-save-limit": {
                        "experience_orb": -1,
                        "snowball": -1,
                        "ender_pearl": -1,
                        "arrow": -1,
                        "fireball": -1,
                        "small_fireball": -1
                    },
                    "fix-climbing-bypassing-cramming-rule": False,
                    "mobs-can-always-pick-up-loot": {
                        "zombies": False,
                        "skeletons": False
                    },
                    "portal-search-vanilla-dimension-scaling": True,
                    "should-remove-dragon": False,
                    "wandering-trader": {
                        "spawn-minute-length": 1200,
                        "spawn-day-length": 24000,
                        "spawn-chance-failure-increment": 25,
                        "spawn-chance-min": 25,
                        "spawn-chance-max": 75
                    },
                    "allow-using-signs-inside-spawn-protection": False,
                    "allow-vehicle-collisions": True,
                    "ender-dragons-death-always-places-dragon-egg": False,
                    "fix-items-merging-through-walls": False,
                    "fix-wither-targeting-bug": False,
                    "map-item-frame-cursor-limit": 128,
                    "max-leash-distance": 10.0,
                    "only-players-collide": False,
                    "seed-based-feature-search-loads-chunks": True,
                    "show-sign-click-command-failure-msgs-to-player": False,
                    "spawn-limits": {
                        "monsters": -1,
                        "animals": -1,
                        "water-animals": -1,
                        "water-ambient": -1,
                        "ambient": -1,
                        "creature": -1,
                        "monster": -1,
                        "underground_water_creature": -1,
                        "water_ambient": -1,
                        "water_creature": -1,
                        "axolotls": -1
                    },
                    "update-pathfinding-on-block-update": True,
                    "allow-player-cramming-damage": False,
                    "feature-seeds": {"generate-random-seeds-for-all": False},
                    "map-item-frame-cursor-update-interval": 10,
                    "mob-effects": {
                        "undead-immune-to-certain-effects": True,
                        "spiders-immune-to-poison-effect": True,
                        "immune-to-wither-effect": {
                            "wither": True,
                            "wither-skeleton": True
                        }
                    },
                    "piglins-guard-chests": True,
                    "split-overstacked-loot": True,
                    "tick-rates": {
                        "sensor": {"villager": {"secondarypoisensor": 40}},
                        "behavior": {"villager": {"validatenearbypoi": -1}}
                    },
                    "anticheat": {
                        "obfuscation": {
                            "items": {
                                "hide-itemmeta": False,
                                "hide-durability": False
                            }
                        }
                    },
                    "monster-spawn-max-light-level": -1,
                    "slime-spawn-height": {
                        "swamp-biome": {"maximum": 70.0, "minimum": 50.0},
                        "slime-chunk": {"maximum": 40.0}
                    },
                    "wateranimal-spawn-height": {"maximum": "default", "minimum": "default"},
                    "redstone-implementation": "vanilla",
                    "treasure-maps-find-already-discovered": {
                        "villager-trade": False,
                        "loot-tables": "default"
                    }
                }
            }
        }
