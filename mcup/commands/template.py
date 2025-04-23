import os
import json

from mcup.config_assemblers import AssemblerLinkerConfig
from mcup.configs import ServerPropertiesConfig, BukkitConfig, SpigotConfig, PaperConfig
from mcup.template import Template, TemplateManager
from mcup.utils.locker import LockerManager
from mcup.utils.ui.collector.predefined import ServerPropertiesCollector
from mcup.utils.version import Version


class TemplateCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup template create <template_name>' command."""
        template_name = args.template_name

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
        """Handles 'mcup template import <path>' command."""
        path = args.path

        if not os.path.exists(path):
            print(f"Error: File not found at path: {path}")
            return

        try:
            with open(path, 'r') as file:
                template_data = json.load(file)

            template_name = template_data.get("template_name")
            template_server_type = template_data.get("template_server_type")
            template_server_version = template_data.get("template_server_version")
            template_linker_config_data = template_data.get("template_linker_config")

            if not all([template_name, template_server_type, template_server_version, template_linker_config_data]):
                print(f"Error: Invalid template file format at path: {path}")
                return

            assembler_linker_config = AssemblerLinkerConfig()
            assembler_linker_config.from_dict(template_linker_config_data)

            template = Template(
                template_name,
                template_server_type,
                template_server_version,
                assembler_linker_config
            )

            TemplateManager.save_template(template)

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file at path: {path}")
        except Exception as e:
            print(f"Error importing template: {str(e)}")

    @staticmethod
    def export_template(args):
        """Handles 'mcup template export <template_name> <destination>' command."""
        template_name = args.template_name
        destination = args.destination

        template_path = f".templates/{template_name}.json"

        if not os.path.exists(template_path):
            print(f"Error: Template '{template_name}' not found.")
            return

        try:
            destination_dir = os.path.dirname(destination)
            if destination_dir and not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            with open(template_path, 'r') as src_file:
                template_data = json.load(src_file)

            with open(destination, 'w') as dest_file:
                json.dump(template_data, dest_file, indent=4)

            print(f"Template '{template_name}' exported successfully to '{destination}'.")

        except Exception as e:
            print(f"Error exporting template: {str(e)}")

    @staticmethod
    def delete(args):
        """Handles 'mcup template delete <template_name>' command."""
        template_name = args.template_name
        if os.path.exists(f".templates/{template_name}.json"):
            os.remove(f".templates/{template_name}.json")
            print(f"Deleted template '{template_name}'")
        else:
            print(f"Template '{template_name}' not found.")

    @staticmethod
    def use(args):
        """Handles 'mcup template use <template_name> [path]' command."""
        print(f"[TODO] Using template '{args.template_name}' at {args.path}")
