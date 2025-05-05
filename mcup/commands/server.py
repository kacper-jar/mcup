import os
from pathlib import Path

from mcup.config_assemblers import AssemblerLinkerConfig, AssemblerLinker
from mcup.configs import ServerPropertiesConfig, BukkitConfig, SpigotConfig, PaperConfig
from mcup.server import ServerManager
from mcup.utils.locker import LockerManager
from mcup.utils.ui.collector.predefined import ServerPropertiesCollector, BukkitCollector, SpigotCollector
from mcup.utils.version import Version


class ServerCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup server create [path]' command."""
        server_path = Path(args.path).resolve()

        print(f"Creating a Minecraft server in: {server_path}")

        locker = LockerManager()
        locker_data = locker.load_locker()

        print("By creating Minecraft server you agree with Minecraft EULA available at https://aka.ms/MinecraftEULA")

        server_type = input("Server type (full list available at: ): ")
        is_valid_server_type = False
        for server in locker_data["servers"]:
            if server == server_type:
                is_valid_server_type = True
                break
        if not is_valid_server_type:
            print(f"Invalid or unsupported server type: {server_type}")
            return

        server_version = input(f"{server_type} server version (full list available at: ): ")
        is_valid_server_version = False
        for version in locker_data["servers"][server_type]:
            if version["version"] == server_version:
                is_valid_server_version = True
                source = version["source"]
                if source == "DOWNLOAD":
                    target = version["url"]
                elif source == "BUILDTOOLS":
                    target = version["target"]
                configs = version["configs"]
                break
        if not is_valid_server_version:
            print(f"Invalid or unsupported server version: {server_version}")
            return

        version = Version.from_string(server_version)

        assembler_linker_conf = AssemblerLinkerConfig()

        server_properties = ServerPropertiesConfig()
        collector = ServerPropertiesCollector()
        output = collector.start_collector(version)
        server_properties.set_configuration_properties(output)

        if "bukkit" in configs:
            bukkit_config = BukkitConfig()
            bukkit_collector = BukkitCollector()
            output = bukkit_collector.start_collector(version)
            bukkit_config.set_configuration_properties(output)
            assembler_linker_conf.add_configuration_file(bukkit_config)

        if "spigot" in configs:
            spigot_config = SpigotConfig()
            spigot_collector = SpigotCollector()
            output = spigot_collector.start_collector(version)
            spigot_config.set_configuration_properties(output)
            assembler_linker_conf.add_configuration_file(spigot_config)

        if "paper" in configs:
            paper_config = PaperConfig()
            assembler_linker_conf.add_configuration_file(paper_config)

        assembler_linker_conf.add_configuration_file(server_properties)

        server = ServerManager()
        server.create(server_path, server_version, source, target, assembler_linker_conf)
