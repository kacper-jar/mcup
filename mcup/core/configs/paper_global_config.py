from mcup.core.configs import ConfigFile
from mcup.core.utils.version import VersionDependantVariablePicker, VersionDependantVariable, Version, LATEST_VERSION


class PaperGlobalConfig(ConfigFile):
    """Class representing a paper-global.yml Minecraft server configuration file."""
    def __init__(self):
        """Initialize the paper-global.yml configuration with default values."""
        self.config_file_name = "paper-global.yml"
        self.config_file_path = "/config"

        self.configuration = {
            "_version": None,  # <--- This needs to be changed based on the server version.
            "anticheat": {  # 1.21.4+
                "obfuscation": {
                    "items": {
                        "all-models": {
                            "also-obfuscate": None,
                            "dont-obfuscate": None,
                            "sanitize-count": None
                        },
                        "enable-item-obfuscation": None,
                        "model-overrides": {
                            "minecraft:elytra": {
                                "also-obfuscate": None,
                                "dont-obfuscate": None,
                                "sanitize-count": None
                            }
                        }
                    }
                }
            },
            "block-updates": {  # 1.20.1+
                "disable-chorus-plant-updates": None,
                "disable-mushroom-block-updates": None,
                "disable-noteblock-updates": None,
                "disable-tripwire-updates": None
            },
            "async-chunks": {  # 1.19-1.19.1
                "threads": None
            },
            "chunk-loading": {  # 1.19-1.19.4
                "autoconfig-send-distance": None,
                "enable-frustum-priority": None,
                "global-max-chunk-load-rate": None,
                "global-max-chunk-send-rate": None,
                "global-max-concurrent-loads": None,
                "max-concurrent-sends": None,
                "min-load-radius": None,
                "player-max-chunk-load-rate": None,
                "player-max-concurrent-loads": None,
                "target-player-chunk-send-rate": None
            },
            "chunk-loading-advanced": {  # 1.20+
                "auto-config-send-distance": None,
                "player-max-concurrent-chunk-generates": None,
                "player-max-concurrent-chunk-loads": None
            },
            "chunk-loading-basic": {  # 1.20+
                "player-max-chunk-generate-rate": None,
                "player-max-chunk-load-rate": None,
                "player-max-chunk-send-rate": None
            },
            "chunk-system": {  # 1.19.2+
                "gen-parallelism": None,
                "io-threads": None,
                "worker-threads": None
            },
            "collisions": {
                "enable-player-collisions": None,
                "send-full-pos-for-hard-colliding-entities": None
            },
            "commands": {
                "fix-target-selector-tag-completion": None,  # 1.19-1.21.3
                "ride-command-allow-player-as-vehicle": None,  # 1.21.4+
                "suggest-player-names-when-null-tab-completions": None,
                "time-command-affects-all-worlds": None
            },
            "console": {
                "enable-brigadier-completions": None,
                "enable-brigadier-highlighting": None,
                "has-all-permissions": None
            },
            "item-validation": {
                "book": {
                    "author": None,
                    "page": None,
                    "title": None
                },
                "book-size": {
                    "page-max": None,
                    "total-multiplier": None
                },
                "display-name": None,
                "lore-line": None,
                "resolve-selectors-in-books": None
            },
            "logging": {
                "deobfuscate-stacktraces": None,
                "log-player-ip-addresses": None,  # 1.19-1.20.1
                "use-rgb-for-named-text-colors": None  # 1.19-1.19.4
            },
            "messages": {
                "kick": {
                    "authentication-servers-down": None,
                    "connection-throttle": None,
                    "flying-player": None,
                    "flying-vehicle": None
                },
                "no-permission": None,
                "use-display-name-in-quit-message": None
            },
            "misc": {
                "chat-threads": {  # 1.19.2+
                    "chat-executor-core-size": None,
                    "chat-executor-max-size": None
                },
                "client-interaction-leniency-distance": None,  # 1.21+
                "compression-level": None,  # 1.20.1+
                "fix-entity-position-desync": None,
                "lag-compensate-block-breaking": None,  # 1.19-1.20
                "load-permissions-yml-before-plugins": None,
                "max-joins-per-tick": None,
                "region-file-cache-size": None,
                "strict-advancement-dimension-check": None,
                "use-alternative-luck-formula": None,
                "use-dimension-type-for-custom-spawners": None
            },
            "packet-limiter": {
                "all-packets": {
                    "action": None,
                    "interval": None,
                    "max-packet-rate": None
                },
                "kick-message": None,
                "overrides": None
            },
            "player-auto-save": {
                "max-per-tick": None,
                "rate": None
            },
            "proxies": {
                "bungee-cord": {
                    "online-mode": None
                },
                "proxy-protocol": None,
                "velocity": {
                    "enabled": None,
                    "online-mode": None,
                    "secret": None
                }
            },
            "scoreboards": {
                "save-empty-scoreboard-teams": None,
                "track-plugin-scoreboards": None
            },
            "spam-limiter": {
                "incoming-packet-threshold": None,
                "recipe-spam-increment": None,
                "recipe-spam-limit": None,
                "tab-spam-increment": None,
                "tab-spam-limit": None
            },
            "spark": {  # 1.21+
                "enable-immediately": None,
                "enabled": None
            },
            "timings": {
                "enabled": None,
                "hidden-config-entries": [
                    None
                ],
                "history-interval": None,
                "history-length": None,
                "server-name": None,
                "server-name-privacy": None,
                "url": None,
                "verbose": None
            },
            "unsupported-settings": {
                "allow-grindstone-overstacking": None,  # 1.19.2-1.20.4
                "allow-headless-pistons": None,
                "allow-permanent-block-break-exploits": None,
                "allow-piston-duplication": None,
                "allow-tripwire-disarming-exploits": None,  # 1.20.4-1.21.1
                "allow-unsafe-end-portal-teleportation": None,  # 1.20.4+
                "compression-format": None,  # 1.20.1+
                "perform-username-validation": None,
                "simplify-remote-item-matching": None,  # 1.21.1+
                "skip-tripwire-hook-placement-validation": None,  # 1.21.4+
                "skip-vanilla-damage-tick-when-shield-blocked": None,  # 1.20.6+
                "update-equipment-on-player-actions": None  # 1.21.4+
            },
            "watchdog": {
                "early-warning-delay": None,
                "early-warning-every": None
            }
        }

        self.default_configuration = {
            "_version": VersionDependantVariablePicker([
                VersionDependantVariable(Version(1, 19), Version(1, 20, 1), 28),
                VersionDependantVariable(Version(1, 20, 2), LATEST_VERSION, 29)
            ]),
            "anticheat": {
                "obfuscation": {
                    "items": {
                        "all-models": {
                            "also-obfuscate": [],
                            "dont-obfuscate": [
                                "minecraft:lodestone_tracker"
                            ],
                            "sanitize-count": True
                        },
                        "enable-item-obfuscation": False,
                        "model-overrides": {
                            "minecraft:elytra": {
                                "also-obfuscate": [],
                                "dont-obfuscate": [
                                    "minecraft:damage"
                                ],
                                "sanitize-count": True
                            }
                        }
                    }
                }
            },
            "block-updates": {
                "disable-chorus-plant-updates": False,
                "disable-mushroom-block-updates": False,
                "disable-noteblock-updates": False,
                "disable-tripwire-updates": False
            },
            "async-chunks": {
                "threads": -1
            },
            "chunk-loading": {
                "autoconfig-send-distance": True,
                "enable-frustum-priority": False,
                "global-max-chunk-load-rate": -1.0,
                "global-max-chunk-send-rate": -1.0,
                "global-max-concurrent-loads": 500.0,
                "max-concurrent-sends": 2,
                "min-load-radius": 2,
                "player-max-chunk-load-rate": -1.0,
                "player-max-concurrent-loads": 20.0,
                "target-player-chunk-send-rate": 100.0
            },
            "chunk-loading-advanced": {
                "auto-config-send-distance": True,
                "player-max-concurrent-chunk-generates": 0,
                "player-max-concurrent-chunk-loads": 0
            },
            "chunk-loading-basic": {
                "player-max-chunk-generate-rate": -1.0,
                "player-max-chunk-load-rate": 100.0,
                "player-max-chunk-send-rate": 75.0
            },
            "chunk-system": {
                "gen-parallelism": True,
                "io-threads": -1,
                "worker-threads": -1
            },
            "collisions": {
                "enable-player-collisions": True,
                "send-full-pos-for-hard-colliding-entities": True
            },
            "commands": {
                "fix-target-selector-tag-completion": True,
                "ride-command-allow-player-as-vehicle": False,
                "suggest-player-names-when-null-tab-completions": True,
                "time-command-affects-all-worlds": False
            },
            "console": {
                "enable-brigadier-completions": True,
                "enable-brigadier-highlighting": True,
                "has-all-permissions": False
            },
            "item-validation": {
                "book": {
                    "author": 8192,
                    "page": 16384,
                    "title": 8192
                },
                "book-size": {
                    "page-max": 2560,
                    "total-multiplier": 0.98
                },
                "display-name": 8192,
                "lore-line": 8192,
                "resolve-selectors-in-books": False
            },
            "logging": {
                "deobfuscate-stacktraces": True,
                "log-player-ip-addresses": True,
                "use-rgb-for-named-text-colors": True
            },
            "messages": {
                "kick": {
                    "authentication-servers-down": "<lang:multiplayer.disconnect.authservers_down>",
                    "connection-throttle": "Connection throttled! Please wait before reconnecting.",
                    "flying-player": "<lang:multiplayer.disconnect.flying>",
                    "flying-vehicle": "<lang:multiplayer.disconnect.flying>"
                },
                "no-permission": (
                    "<red>I'm sorry, but you do not have permission to perform this command.\n"
                    "Please contact the server administrators if you believe that this is in error."
                ),
                "use-display-name-in-quit-message": False
            },
            "misc": {
                "chat-threads": {
                    "chat-executor-core-size": -1,
                    "chat-executor-max-size": -1
                },
                "client-interaction-leniency-distance": "default",
                "compression-level": "default",
                "fix-entity-position-desync": True,
                "lag-compensate-block-breaking": True,
                "load-permissions-yml-before-plugins": True,
                "max-joins-per-tick": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 19, 2), 3),
                    VersionDependantVariable(Version(1, 19, 3), LATEST_VERSION, 5)
                ]),
                "region-file-cache-size": 256,
                "strict-advancement-dimension-check": False,
                "use-alternative-luck-formula": False,
                "use-dimension-type-for-custom-spawners": False
            },
            "packet-limiter": {
                "all-packets": {
                    "action": "KICK",
                    "interval": 7.0,
                    "max-packet-rate": 500.0
                },
                "kick-message": "<red><lang:disconnect.exceeded_packet_rate>",
                "overrides": []
            },
            "player-auto-save": {
                "max-per-tick": -1,
                "rate": -1
            },
            "proxies": {
                "bungee-cord": {
                    "online-mode": True
                },
                "proxy-protocol": False,
                "velocity": {
                    "enabled": False,
                    "online-mode": VersionDependantVariablePicker([
                        VersionDependantVariable(Version(1, 19), Version(1, 20, 3), False),
                        VersionDependantVariable(Version(1, 20, 4), LATEST_VERSION, True)
                    ]),
                    "secret": ""
                }
            },
            "scoreboards": {
                "save-empty-scoreboard-teams": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 20, 5), False),
                    VersionDependantVariable(Version(1, 20, 5), LATEST_VERSION, True)
                ]),
                "track-plugin-scoreboards": False
            },
            "spam-limiter": {
                "incoming-packet-threshold": 300,
                "recipe-spam-increment": 1,
                "recipe-spam-limit": 20,
                "tab-spam-increment": 1,
                "tab-spam-limit": 500
            },
            "spark": {
                "enable-immediately": False,
                "enabled": True
            },
            "timings": {
                "enabled": VersionDependantVariablePicker([
                    VersionDependantVariable(Version(1, 19), Version(1, 20, 6), True),
                    VersionDependantVariable(Version(1, 21), LATEST_VERSION, False),
                ]),
                "hidden-config-entries": [
                    "database",
                    "proxies.velocity.secret"
                ],
                "history-interval": 300,
                "history-length": 3600,
                "server-name": "Unknown Server",
                "server-name-privacy": False,
                "url": "https://timings.aikar.co/",
                "verbose": True
            },
            "unsupported-settings": {
                "allow-grindstone-overstacking": False,
                "allow-headless-pistons": False,
                "allow-permanent-block-break-exploits": False,
                "allow-piston-duplication": False,
                "allow-tripwire-disarming-exploits": False,
                "allow-unsafe-end-portal-teleportation": False,
                "compression-format": "ZLIB",
                "perform-username-validation": True,
                "simplify-remote-item-matching": False,
                "skip-tripwire-hook-placement-validation": False,
                "skip-vanilla-damage-tick-when-shield-blocked": False,
                "update-equipment-on-player-actions": True
            },
            "watchdog": {
                "early-warning-delay": 10000,
                "early-warning-every": 5000
            }
        }
