from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.configs import ServerPropertiesConfig, BukkitConfig, SpigotConfig, PaperConfig, PaperGlobalConfig, \
    StartScript, PaperWorldDefaultsConfig
from mcup.cli.ui.components import ServerPropertiesCollector, BukkitCollector, SpigotCollector, PaperCollector, \
    StartScriptCollector, PaperGlobalCollector, PaperWorldDefaultsCollector
from mcup.core.utils.version import Version


class ServerConfigsCollector:
    @staticmethod
    def collect_configurations(server_version, configs, no_configs: bool = False,
                               all_defaults: bool = False) -> AssemblerLinkerConfig:
        version = Version.from_string(server_version)

        assembler_linker_config = AssemblerLinkerConfig()

        if no_configs:
            return assembler_linker_config

        server_properties = ServerPropertiesConfig()
        if not all_defaults:
            collector = ServerPropertiesCollector()
            output = collector.start_collector(version)
            server_properties.set_configuration_properties(output, version)
        else:
            server_properties.set_configuration_default_all_properties(version)
        assembler_linker_config.add_configuration_file(server_properties)

        if "bukkit" in configs:
            bukkit_config = BukkitConfig()
            if not all_defaults:
                bukkit_collector = BukkitCollector()
                output = bukkit_collector.start_collector(version)
                bukkit_config.set_configuration_properties(output, version)
            else:
                bukkit_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(bukkit_config)

        if "spigot" in configs:
            spigot_config = SpigotConfig()
            if not all_defaults:
                spigot_collector = SpigotCollector()
                output = spigot_collector.start_collector(version)
                spigot_config.set_configuration_properties(output, version)
            else:
                spigot_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(spigot_config)

        if "paper" in configs:
            paper_config = PaperConfig()
            if not all_defaults:
                paper_collector = PaperCollector()
                output = paper_collector.start_collector(version)
                paper_config.set_configuration_properties(output, version)
            else:
                paper_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_config)

        if "paper-global" in configs:
            paper_global_config = PaperGlobalConfig()
            if not all_defaults:
                paper_global_config.set_configuration_default_property("_version", version)
                paper_global_config_collector = PaperGlobalCollector()
                output = paper_global_config_collector.start_collector(version)
                paper_global_config.set_configuration_properties(output, version)
            else:
                paper_global_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_global_config)

        if "paper-world-defaults" in configs:
            paper_world_defaults_config = PaperWorldDefaultsConfig()
            if not all_defaults:
                paper_world_defaults_config.set_configuration_default_property("_version", version)
                paper_world_defaults_config_collector = PaperWorldDefaultsCollector()
                output = paper_world_defaults_config_collector.start_collector(version)
                paper_world_defaults_config.set_configuration_properties(output, version)
            else:
                paper_world_defaults_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_world_defaults_config)

        create_start_script = True if all_defaults else (input("Create start script? (Y/n): ").strip().lower()
                                                         in ["y", ""])
        if create_start_script:
            start_script_config = StartScript()
            if not all_defaults:
                start_script_collector = StartScriptCollector()
                output = start_script_collector.start_collector(version)
                start_script_config.set_configuration_properties(output, version)
            else:
                start_script_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(start_script_config)

        return assembler_linker_config
