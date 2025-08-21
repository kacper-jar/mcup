import sys

from mcup.cli.language import Language
from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.configs import ServerPropertiesConfig, BukkitConfig, SpigotConfig, PaperConfig, PaperGlobalConfig, \
    PaperWorldDefaultsConfig, BashStartScript, BatchStartScript
from mcup.cli.ui.components import ServerPropertiesCollector, BukkitCollector, SpigotCollector, PaperCollector, \
    StartScriptCollector, PaperGlobalCollector, PaperWorldDefaultsCollector, ServerConfigsCollectorFlags
from mcup.core.status import StatusCode
from mcup.core.user_config import UserConfig
from mcup.core.utils.version import Version


class ServerConfigsCollector:
    @staticmethod
    def collect_configurations(server_version, configs,
                               flags=ServerConfigsCollectorFlags.NONE) -> AssemblerLinkerConfig:
        language = Language()
        user_config = UserConfig()

        version = Version.from_string(server_version)

        assembler_linker_config = AssemblerLinkerConfig()

        if flags == ServerConfigsCollectorFlags.NO_CONFIGS:
            return assembler_linker_config

        configs_to_collect = configs

        no_defaults = flags == ServerConfigsCollectorFlags.NO_DEFAULTS

        for status in user_config.get_configuration("advancedmode.enabled", default="false"):
            if status.status_code == StatusCode.SUCCESS:
                advanced_mode_enabled = str(status.status_details).lower() == "true"
                break
            else:
                advanced_mode_enabled = False
                break

        if not advanced_mode_enabled:
            print(language.get_string("INFO_ADVANCED_MODE_DISABLED"))

        server_properties = ServerPropertiesConfig()
        if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
            if not advanced_mode_enabled:
                server_properties.set_configuration_default_all_properties(version)
            collector = ServerPropertiesCollector()
            output = collector.start_collector(version, no_defaults, advanced_mode_enabled)
            server_properties.set_configuration_properties(output, version)
        else:
            server_properties.set_configuration_default_all_properties(version)
        assembler_linker_config.add_configuration_file(server_properties)

        if "bukkit" in configs:
            bukkit_config = BukkitConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                if not advanced_mode_enabled:
                    bukkit_config.set_configuration_default_all_properties(version)
                bukkit_collector = BukkitCollector()
                output = bukkit_collector.start_collector(version, no_defaults, advanced_mode_enabled)
                bukkit_config.set_configuration_properties(output, version)
            else:
                bukkit_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(bukkit_config)
            configs_to_collect.remove("bukkit")

        if "spigot" in configs:
            spigot_config = SpigotConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                if not advanced_mode_enabled:
                    spigot_config.set_configuration_default_all_properties(version)
                spigot_collector = SpigotCollector()
                output = spigot_collector.start_collector(version, no_defaults, advanced_mode_enabled)
                spigot_config.set_configuration_properties(output, version)
            else:
                spigot_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(spigot_config)
            configs_to_collect.remove("spigot")

        if "paper" in configs:
            paper_config = PaperConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                if not advanced_mode_enabled:
                    paper_config.set_configuration_default_all_properties(version)
                paper_collector = PaperCollector()
                output = paper_collector.start_collector(version, no_defaults, advanced_mode_enabled)
                paper_config.set_configuration_properties(output, version)
            else:
                paper_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_config)
            configs_to_collect.remove("paper")

        if "paper-global" in configs:
            paper_global_config = PaperGlobalConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                if not advanced_mode_enabled:
                    paper_global_config.set_configuration_default_all_properties(version)
                paper_global_config.set_configuration_default_property("_version", version)
                paper_global_config_collector = PaperGlobalCollector()
                output = paper_global_config_collector.start_collector(version, no_defaults, advanced_mode_enabled)
                paper_global_config.set_configuration_properties(output, version)
            else:
                paper_global_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_global_config)
            configs_to_collect.remove("paper-global")

        if "paper-world-defaults" in configs:
            paper_world_defaults_config = PaperWorldDefaultsConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                if not advanced_mode_enabled:
                    paper_world_defaults_config.set_configuration_default_all_properties(version)
                paper_world_defaults_config.set_configuration_default_property("_version", version)
                paper_world_defaults_config_collector = PaperWorldDefaultsCollector()
                output = paper_world_defaults_config_collector.start_collector(version, no_defaults,
                                                                               advanced_mode_enabled)
                paper_world_defaults_config.set_configuration_properties(output, version)
            else:
                paper_world_defaults_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_world_defaults_config)
            configs_to_collect.remove("paper-world-defaults")

        if configs_to_collect:
            print(language.get_string("INFO_CONFIGS_NOT_SUPPORTED", ', '.join(configs_to_collect)))

        create_start_script = True if flags == ServerConfigsCollectorFlags.ALL_DEFAULTS \
            else (input("Create start script? (Y/n): ").strip().lower() in ["y", ""])
        if create_start_script:
            if sys.platform == "win32":
                start_script_config = BatchStartScript()
            else:
                start_script_config = BashStartScript()

            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                if not advanced_mode_enabled:
                    start_script_config.set_configuration_default_all_properties(version)
                start_script_collector = StartScriptCollector()
                output = start_script_collector.start_collector(version, no_defaults, advanced_mode_enabled)
                start_script_config.set_configuration_properties(output, version)
            else:
                start_script_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(start_script_config)

        return assembler_linker_config
