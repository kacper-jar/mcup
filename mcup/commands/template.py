import os
import json
from pathlib import Path

from mcup.server import ServerManager
from mcup.config_assemblers import AssemblerLinkerConfig
from mcup.template import Template, TemplateManager
from mcup.utils.locker import LockerManager
from mcup.ui.components import ServerInfoPrompt, ServerConfigsCollector


class TemplateCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup template create <template_name>' command."""
        template_name = args.template_name
        locker = LockerManager()

        try:
            server_info_prompt = ServerInfoPrompt()
            server_type, server_version, source, target, configs = server_info_prompt.get_server_info(locker)
        except Exception as e:
            print(e)
            return

        assembler_linker_conf = ServerConfigsCollector.collect_configurations(server_version, configs)

        template = Template(
            template_name,
            server_type,
            server_version,
            source,
            target,
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
        template_name = args.template_name
        server_path = Path(args.path)
        locker = LockerManager()
        assembler_linker_conf = AssemblerLinkerConfig()

        if not os.path.exists(f".templates/{template_name}.json"):
            print(f"Error: Template '{template_name}' not found.")
            return

        print(f"Creating a Minecraft server in: {server_path} (from template: {template_name})")

        try:
            path = f".templates/{template_name}.json"

            with open(path, 'r') as file:
                template_data = json.load(file)

            server_type = template_data.get("template_server_type")
            server_version = template_data.get("template_server_version")
            source = template_data.get("template_server_source")
            target = template_data.get("template_server_target")
            linker_config_data = template_data.get("template_linker_config")

            if not all([server_type, server_version, linker_config_data]):
                print(f"Error: Missing data inside template file at path: {path}")
                return

            assembler_linker_conf.from_dict(linker_config_data)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file at path: {path}")
        except Exception as e:
            print(f"Error reading template: {str(e)}")

        server = ServerManager()
        server.create(server_path, server_version, source, target, assembler_linker_conf)
