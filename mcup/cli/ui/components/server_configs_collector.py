from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.configs import ServerPropertiesConfig, BukkitConfig, SpigotConfig, PaperConfig, PaperGlobalConfig, \
    StartScript, PaperWorldDefaultsConfig
from mcup.cli.ui.components import ServerPropertiesCollector, BukkitCollector, SpigotCollector, PaperCollector, \
    StartScriptCollector, PaperGlobalCollector, PaperWorldDefaultsCollector, ServerConfigsCollectorFlags
from mcup.core.utils.version import Version


class ServerConfigsCollector:
    @staticmethod
    def collect_configurations(server_version, configs,
                               flags=ServerConfigsCollectorFlags.NONE) -> AssemblerLinkerConfig:
        version = Version.from_string(server_version)

        assembler_linker_config = AssemblerLinkerConfig()

        if flags == ServerConfigsCollectorFlags.NO_CONFIGS:
            return assembler_linker_config

        no_defaults = flags == ServerConfigsCollectorFlags.NO_DEFAULTS

        server_properties = ServerPropertiesConfig()
        if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
            collector = ServerPropertiesCollector()
            output = collector.start_collector(version, no_defaults)
            server_properties.set_configuration_properties(output, version)
        else:
            server_properties.set_configuration_default_all_properties(version)
        assembler_linker_config.add_configuration_file(server_properties)

        if "bukkit" in configs:
            bukkit_config = BukkitConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                bukkit_collector = BukkitCollector()
                output = bukkit_collector.start_collector(version, no_defaults)
                bukkit_config.set_configuration_properties(output, version)
            else:
                bukkit_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(bukkit_config)

        if "spigot" in configs:
            spigot_config = SpigotConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                spigot_collector = SpigotCollector()
                output = spigot_collector.start_collector(version, no_defaults)
                spigot_config.set_configuration_properties(output, version)
            else:
                spigot_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(spigot_config)

        if "paper" in configs:
            paper_config = PaperConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                paper_collector = PaperCollector()
                output = paper_collector.start_collector(version, no_defaults)
                paper_config.set_configuration_properties(output, version)
            else:
                paper_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_config)

        if "paper-global" in configs:
            paper_global_config = PaperGlobalConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                paper_global_config.set_configuration_default_property("_version", version)
                paper_global_config_collector = PaperGlobalCollector()
                output = paper_global_config_collector.start_collector(version, no_defaults)
                paper_global_config.set_configuration_properties(output, version)
            else:
                paper_global_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_global_config)

        if "paper-world-defaults" in configs:
            paper_world_defaults_config = PaperWorldDefaultsConfig()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                paper_world_defaults_config.set_configuration_default_property("_version", version)
                paper_world_defaults_config_collector = PaperWorldDefaultsCollector()
                output = paper_world_defaults_config_collector.start_collector(version, no_defaults)
                paper_world_defaults_config.set_configuration_properties(output, version)
            else:
                paper_world_defaults_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(paper_world_defaults_config)

        create_start_script = True if flags == ServerConfigsCollectorFlags.ALL_DEFAULTS \
            else (input("Create start script? (Y/n): ").strip().lower() in ["y", ""])
        if create_start_script:
            start_script_config = StartScript()
            if flags != ServerConfigsCollectorFlags.ALL_DEFAULTS:
                start_script_collector = StartScriptCollector()
                output = start_script_collector.start_collector(version, no_defaults)
                start_script_config.set_configuration_properties(output, version)
            else:
                start_script_config.set_configuration_default_all_properties(version)
            assembler_linker_config.add_configuration_file(start_script_config)

        return assembler_linker_config
