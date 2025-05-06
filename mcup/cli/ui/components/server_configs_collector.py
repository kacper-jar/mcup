from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.configs import ServerPropertiesConfig, BukkitConfig, SpigotConfig, PaperConfig
from mcup.cli.ui.components import ServerPropertiesCollector, BukkitCollector, SpigotCollector, PaperCollector
from mcup.core.utils.version import Version


class ServerConfigsCollector:
    @staticmethod
    def collect_configurations(server_version, configs) -> AssemblerLinkerConfig:
        version = Version.from_string(server_version)

        assembler_linker_config = AssemblerLinkerConfig()

        server_properties = ServerPropertiesConfig()
        collector = ServerPropertiesCollector()
        output = collector.start_collector(version)
        server_properties.set_configuration_properties(output)

        if "bukkit" in configs:
            bukkit_config = BukkitConfig()
            bukkit_collector = BukkitCollector()
            output = bukkit_collector.start_collector(version)
            bukkit_config.set_configuration_properties(output)
            assembler_linker_config.add_configuration_file(bukkit_config)

        if "spigot" in configs:
            spigot_config = SpigotConfig()
            spigot_collector = SpigotCollector()
            output = spigot_collector.start_collector(version)
            spigot_config.set_configuration_properties(output)
            assembler_linker_config.add_configuration_file(spigot_config)

        if "paper" in configs:
            paper_config = PaperConfig()
            paper_collector = PaperCollector()
            output = paper_collector.start_collector(version)
            paper_config.set_configuration_properties(output)
            assembler_linker_config.add_configuration_file(paper_config)

        assembler_linker_config.add_configuration_file(server_properties)

        return assembler_linker_config
