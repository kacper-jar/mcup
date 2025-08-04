import json
import os
from pathlib import Path
from typing import Iterator

from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.handlers import ServerHandler
from mcup.core.status import Status, StatusCode
from mcup.core.template import Template, TemplateManager
from mcup.core.utils.locker import LockerUpdater
from mcup.core.utils.path import PathProvider


class TemplateHandler:
    """Class for handling template-related actions."""

    def create_template(self, template_name: str, server_type: str, server_version: str, locker_entry: dict,
                        assembler_linker_conf: AssemblerLinkerConfig) -> Iterator[Status]:
        template = Template(
            template_name,
            server_type,
            server_version,
            locker_entry,
            assembler_linker_conf
        )

        try:
            TemplateManager.save_template(template)
        except Exception as e:
            yield Status(StatusCode.ERROR_TEMPLATE_WRITE_FAILED, str(e))
            return
        yield Status(StatusCode.SUCCESS)

    def import_template(self, path: str) -> Iterator[Status]:
        if not os.path.exists(path):
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        try:
            with open(path, 'r') as file:
                template_data = json.load(file)

            template_name = template_data.get("template_name")
            template_server_type = template_data.get("template_server_type")
            template_server_version = template_data.get("template_server_version")
            template_locker_entry = template_data.get("template_locker_entry")
            template_linker_config_data = template_data.get("template_linker_config")

            if not all([template_name, template_server_type, template_server_version, template_locker_entry,
                        template_linker_config_data]):
                yield Status(StatusCode.ERROR_TEMPLATE_MISSING_DATA, path)
                return

            assembler_linker_config = AssemblerLinkerConfig()
            assembler_linker_config.from_dict(template_linker_config_data)

            template = Template(
                template_name,
                template_server_type,
                template_server_version,
                template_locker_entry,
                assembler_linker_config
            )

            TemplateManager.save_template(template)
        except json.JSONDecodeError:
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, path)
        except Exception as e:
            yield Status(StatusCode.ERROR_TEMPLATE_IMPORT_FAILED, str(e))

    def export_template(self, template_name: str, destination: str) -> Iterator[Status]:
        path_provider = PathProvider()

        template_path = f"{path_provider.get_templates_path()}/{template_name}.json"

        if not os.path.exists(template_path):
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        try:
            destination_dir = os.path.dirname(destination)
            if destination_dir and not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            with open(template_path, 'r') as src_file:
                template_data = json.load(src_file)

            with open(destination, 'w') as dest_file:
                json.dump(template_data, dest_file, indent=4)

            yield Status(StatusCode.SUCCESS)
        except Exception as e:
            yield Status(StatusCode.ERROR_TEMPLATE_EXPORT_FAILED, str(e))
            return

    def delete_template(self, template_name: str) -> Iterator[Status]:
        path_provider = PathProvider()

        if os.path.exists(f"{path_provider.get_templates_path()}/{template_name}.json"):
            os.remove(f"{path_provider.get_templates_path()}/{template_name}.json")
            yield Status(StatusCode.SUCCESS)
        else:
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)

    def use_template(self, template_name: str, server_path: str | Path) -> Iterator[Status]:
        assembler_linker_conf = AssemblerLinkerConfig()
        path_provider = PathProvider()

        if not os.path.exists(f"{path_provider.get_templates_path()}/{template_name}.json"):
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        print(f"Creating a Minecraft server in: {server_path} (from template: {template_name})")

        try:
            path = f"{path_provider.get_templates_path()}/{template_name}.json"

            with open(path, 'r') as file:
                template_data = json.load(file)

            server_type = template_data.get("template_server_type")
            server_version = template_data.get("template_server_version")
            locker_entry = template_data.get("template_locker_entry")
            linker_config_data = template_data.get("template_linker_config")

            if not all([server_type, server_version, linker_config_data]):
                yield Status(StatusCode.ERROR_TEMPLATE_MISSING_DATA, path)
                return

            assembler_linker_conf.from_dict(linker_config_data)
        except json.JSONDecodeError:
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, path)
            return
        except Exception as e:
            yield Status(StatusCode.ERROR_TEMPLATE_READ_FAILED, str(e))
            return

        server = ServerHandler()
        for status in server.create(server_path, server_type, server_version, locker_entry, assembler_linker_conf):
            yield status

    def list_templates(self) -> Iterator[Status]:
        templates = []
        for template_file in os.listdir(PathProvider().get_templates_path()):
            templates.append(template_file.split(".")[0])

        yield Status(StatusCode.SUCCESS, templates)

    def refresh_template(self, template_name) -> Iterator[Status]:
        path_provider = PathProvider()
        locker_manager = LockerUpdater()

        template_path = f"{path_provider.get_templates_path()}/{template_name}.json"

        if not os.path.exists(template_path):
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        for status in locker_manager.load_locker():
            if status.status_code != StatusCode.SUCCESS:
                yield status
            else:
                locker_data = status.status_details
                break

        try:
            with open(template_path, 'r') as file:
                template_data = json.load(file)

            template_name = template_data.get("template_name")
            template_server_type = template_data.get("template_server_type")
            template_server_version = template_data.get("template_server_version")
            template_linker_config_data = template_data.get("template_linker_config")

            if not all([template_name, template_server_type, template_server_version, template_linker_config_data]):
                yield Status(StatusCode.ERROR_TEMPLATE_MISSING_DATA, template_name)
                return

            assembler_linker_config = AssemblerLinkerConfig()
            assembler_linker_config.from_dict(template_linker_config_data)

            for version in locker_data["servers"][template_server_type]:
                if version["version"] == template_server_version:
                    template_locker_entry = version
                    break

            template = Template(
                template_name,
                template_server_type,
                template_server_version,
                template_locker_entry,
                assembler_linker_config
            )

            TemplateManager.save_template(template)
        except json.JSONDecodeError:
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, template_name)
        except Exception as e:
            yield Status(StatusCode.ERROR_TEMPLATE_REFRESH_FAILED, str(e))
