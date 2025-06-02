from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.configs import ServerPropertiesConfig, BukkitConfig, SpigotConfig, PaperConfig, PaperGlobalConfig, \
    StartScript, PaperWorldDefaultsConfig
from mcup.cli.ui.components import ServerPropertiesCollector, BukkitCollector, SpigotCollector, PaperCollector, \
    StartScriptCollector
from mcup.core.utils.version import Version


class ServerConfigsCollector:
    @staticmethod
    def collect_configurations(server_version, configs) -> AssemblerLinkerConfig:
        version = Version.from_string(server_version)

        assembler_linker_config = AssemblerLinkerConfig()

        server_properties = ServerPropertiesConfig()
        collector = ServerPropertiesCollector()
        output = collector.start_collector(version)
        server_properties.set_configuration_properties(output, version)
        assembler_linker_config.add_configuration_file(server_properties)

        if "bukkit" in configs:
            bukkit_config = BukkitConfig()
            bukkit_collector = BukkitCollector()
            output = bukkit_collector.start_collector(version)
            bukkit_config.set_configuration_properties(output, version)
            assembler_linker_config.add_configuration_file(bukkit_config)

        if "spigot" in configs:
            spigot_config = SpigotConfig()
            spigot_collector = SpigotCollector()
            output = spigot_collector.start_collector(version)
            spigot_config.set_configuration_properties(output, version)
            assembler_linker_config.add_configuration_file(spigot_config)

        if "paper" in configs:
            paper_config = PaperConfig()
            paper_collector = PaperCollector()
            output = paper_collector.start_collector(version)
            paper_config.set_configuration_properties(output, version)
            assembler_linker_config.add_configuration_file(paper_config)

        if "paper-global" in configs:
            paper_global_config = PaperGlobalConfig()
            paper_global_config.set_configuration_default_property("_version", version)
            assembler_linker_config.add_configuration_file(paper_global_config)

        if "paper-world-defaults" in configs:
            paper_world_defaults_config = PaperWorldDefaultsConfig()
            paper_world_defaults_config.set_configuration_default_property("_version", version)
            assembler_linker_config.add_configuration_file(paper_world_defaults_config)

        create_start_script = input("Create start script? (Y/n): ").strip().lower() in ["y", ""]
        if create_start_script:
            start_script_config = StartScript()
            start_script_collector = StartScriptCollector()
            output = start_script_collector.start_collector(version)
            start_script_config.set_configuration_properties(output, version)
            assembler_linker_config.add_configuration_file(start_script_config)

        return assembler_linker_config
