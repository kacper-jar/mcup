import json
import os
from pathlib import Path

from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.handlers import ServerHandler
from mcup.core.status import Status
from mcup.core.template import Template, TemplateManager
from mcup.core.utils.path import PathProvider


class TemplateHandler:
    """Class for handling template-related actions."""

    # TODO: move CLI UI elements to proper place, instead of tasks we should use some kind of status code

    def create_template(self, template_name: str, server_type: str, server_version: str, source: str, target: str,
               assembler_linker_conf: AssemblerLinkerConfig):
        template = Template(
            template_name,
            server_type,
            server_version,
            source,
            target,
            assembler_linker_conf
        )

        TemplateManager.save_template(template)

    def import_template(self, path: str):
        if not os.path.exists(path):
            print(f"Error: File not found at path: {path}")
            return

        try:
            with open(path, 'r') as file:
                template_data = json.load(file)

            template_name = template_data.get("template_name")
            template_server_type = template_data.get("template_server_type")
            template_server_version = template_data.get("template_server_version")
            template_source = template_data.get("template_server_source")
            template_target = template_data.get("template_server_target")
            template_linker_config_data = template_data.get("template_linker_config")

            if not all([template_name, template_server_type, template_server_version, template_source,
                        template_target, template_linker_config_data]):
                print(f"Error: Invalid template file format at path: {path}")
                return

            assembler_linker_config = AssemblerLinkerConfig()
            assembler_linker_config.from_dict(template_linker_config_data)

            template = Template(
                template_name,
                template_server_type,
                template_server_version,
                template_source,
                template_target,
                assembler_linker_config
            )

            TemplateManager.save_template(template)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file at path: {path}")
        except Exception as e:
            print(f"Error importing template: {str(e)}")

    def export_template(self, template_name: str, destination: str):
        path_provider = PathProvider()

        template_path = f"{path_provider.get_templates_path()}/{template_name}.json"

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

    def delete_template(self, template_name: str):
        path_provider = PathProvider()

        if os.path.exists(f"{path_provider.get_templates_path()}/{template_name}.json"):
            os.remove(f"{path_provider.get_templates_path()}/{template_name}.json")
            print(f"Deleted template '{template_name}'")
        else:
            print(f"Template '{template_name}' not found.")

    def use_template(self, template_name: str, server_path: str | Path):
        assembler_linker_conf = AssemblerLinkerConfig()
        path_provider = PathProvider()

        if not os.path.exists(f"{path_provider.get_templates_path()}/{template_name}.json"):
            print(f"Error: Template '{template_name}' not found.")
            return

        print(f"Creating a Minecraft server in: {server_path} (from template: {template_name})")

        try:
            path = f"{path_provider.get_templates_path()}/{template_name}.json"

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

        server = ServerHandler()
        server.create(server_path, server_version, source, target, assembler_linker_conf)

    def list_templates(self):
        for template_file in os.listdir(PathProvider().get_templates_path()):
            print(template_file.split(".")[0])

    def refresh_template(self):
        pass
