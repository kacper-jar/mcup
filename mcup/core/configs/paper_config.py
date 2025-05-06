from mcup.core.configs import ConfigFile


class PaperConfig(ConfigFile):
    """Class representing a paper.yml Minecraft server configuration file."""
    def __init__(self):
        """Initialize the paper.yml configuration with default values."""
        self.config_file_name = "paper.yml"
        self.config_file_path = "."

        self.configuration = {
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
                "limit-player-interactions": None
            },
            "warnWhenSettingExcessiveVelocity": None,
            "data-value-allowed-items": None,
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
                        "reeds": None
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
                        "hard": None
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
                        "disable-end-credits": None
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
                        "flat-bedrock": None
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
                    "disable-teleportation-suffocation-check": None
                }
            }
        }

        self.default_configuration = {
            "config-version": 9,
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
                "limit-player-interactions": True
            },
            "warnWhenSettingExcessiveVelocity": True,
            "data-value-allowed-items": [],
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
                        "maximum": 63.0
                    },
                    "tnt-explosion-volume": 4.0,
                    "max-growth-height": {
                        "cactus": 3,
                        "reeds": 3
                    },
                    "fishing-time-range": {
                        "MinimumTicks": 100,
                        "MaximumTicks": 900
                    },
                    "player-exhaustion": {
                        "block-break": 0.02500000037252903,
                        "swimming": 0.014999999664723873
                    },
                    "despawn-ranges": {
                        "soft": 32,
                        "hard": 128
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
                        "disable-end-credits": False
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
                        "flat-bedrock": False
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
                    "disable-teleportation-suffocation-check": False
                }
            }
        }
