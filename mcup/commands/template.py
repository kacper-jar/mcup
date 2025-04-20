from mcup.config_assemblers import AssemblerLinkerConfig
from mcup.configs import ServerPropertiesConfig, BukkitConfig, SpigotConfig, PaperConfig
from mcup.template import Template, TemplateManager
from mcup.utils.locker import LockerManager
from mcup.utils.ui.collector.predefined import ServerPropertiesCollector
from mcup.utils.version import Version


class TemplateCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup template create' command."""
        locker = LockerManager()
        locker_data = locker.load_locker()

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
                    url = version["url"]
                elif source == "BUILDTOOLS":
                    target = version["target"]
                configs = version["configs"]
                break
        if not is_valid_server_version:
            print(f"Invalid or unsupported server version: {server_version}")
            return

        template_name = input("Template name: ")

        version = Version.from_string(server_version)

        assembler_linker_conf = AssemblerLinkerConfig()

        server_properties = ServerPropertiesConfig()
        collector = ServerPropertiesCollector()
        output = collector.start_collector(version)
        server_properties.set_configuration_properties(output)

        if "bukkit" in configs:
            bukkit_config = BukkitConfig()
            assembler_linker_conf.add_configuration_file(bukkit_config)

        if "spigot" in configs:
            spigot_config = SpigotConfig()
            assembler_linker_conf.add_configuration_file(spigot_config)

        if "paper" in configs:
            paper_config = PaperConfig()
            assembler_linker_conf.add_configuration_file(paper_config)

        assembler_linker_conf.add_configuration_file(server_properties)

        template = Template(
            template_name,
            server_type,
            server_version,
            assembler_linker_conf
        )

        TemplateManager.save_template(template)

    @staticmethod
    def import_template(args):
        """Handles 'mcup template import' command."""
        print("[TODO] Importing template")

    @staticmethod
    def export_template(args):
        """Handles 'mcup template export' command."""
        print("[TODO] Exporting template")

    @staticmethod
    def delete(args):
        """Handles 'mcup template delete' command."""
        print("[TODO] Deleting template")

    @staticmethod
    def use(args):
        """Handles 'mcup template use <template_name> [path]' command."""
        print(f"[TODO] Using template '{args.template_name}' at {args.path}")
