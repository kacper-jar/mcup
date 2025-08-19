import json
import logging
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

    def __init__(self):
        """Initialize the template handler."""
        self.logger = logging.getLogger(__name__)

    def create_template(self, template_name: str, server_type: str, server_version: str, locker_entry: dict,
                        assembler_linker_conf: AssemblerLinkerConfig) -> Iterator[Status]:
        self.logger.info(f"Creating template: {template_name} (type={server_type}, version={server_version})")
        self.logger.debug(f"Locker entry: {locker_entry}")

        try:
            template = Template(
                template_name,
                server_type,
                server_version,
                locker_entry,
                assembler_linker_conf
            )

            TemplateManager.save_template(template)

            self.logger.info(f"Template '{template_name}' created successfully")
            yield Status(StatusCode.SUCCESS)
        except Exception as e:
            self.logger.error(f"Failed to create template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_WRITE_FAILED, str(e))
            return

    def import_template(self, path: str) -> Iterator[Status]:
        self.logger.info(f"Importing template from: {path}")

        if not os.path.exists(path):
            self.logger.error(f"Template file not found: {path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        try:
            self.logger.debug(f"Reading template file: {path}")
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

            self.logger.debug(
                f"Template data - name: {template_name}, type: {template_server_type}, version: {template_server_version}")

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
            self.logger.info(f"Template '{template_name}' imported successfully from {path}")
            yield Status(StatusCode.SUCCESS)
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format in template file '{path}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, path)
        except Exception as e:
            self.logger.error(f"Failed to import template from '{path}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_IMPORT_FAILED, str(e))

    def export_template(self, template_name: str, destination: str) -> Iterator[Status]:
        self.logger.info(f"Exporting template '{template_name}' to: {destination}")

        path_provider = PathProvider()
        template_path = f"{path_provider.get_templates_path()}/{template_name}.json"

        if not os.path.exists(template_path):
            self.logger.error(f"Template '{template_name}' not found at: {template_path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        try:
            destination_dir = os.path.dirname(destination)
            if destination_dir and not os.path.exists(destination_dir):
                self.logger.debug(f"Creating destination directory: {destination_dir}")
                os.makedirs(destination_dir)

            self.logger.debug(f"Reading template from: {template_path}")
            with open(template_path, 'r') as src_file:
                template_data = json.load(src_file)

            self.logger.debug(f"Writing template to: {destination}")
            with open(destination, 'w') as dest_file:
                json.dump(template_data, dest_file, indent=4)

            self.logger.info(f"Template '{template_name}' exported successfully to {destination}")
            yield Status(StatusCode.SUCCESS)
        except Exception as e:
            self.logger.error(f"Failed to export template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_EXPORT_FAILED, str(e))
            return

    def delete_template(self, template_name: str) -> Iterator[Status]:
        self.logger.info(f"Deleting template: {template_name}")

        path_provider = PathProvider()
        template_path = f"{path_provider.get_templates_path()}/{template_name}.json"

        if os.path.exists(template_path):
            self.logger.info(f"Template '{template_name}' deleted successfully")
            os.remove(f"{path_provider.get_templates_path()}/{template_name}.json")
            yield Status(StatusCode.SUCCESS)
        else:
            self.logger.error(f"Template '{template_name}' not found at: {template_path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)

    def use_template(self, template_name: str, server_path: str | Path) -> Iterator[Status]:
        self.logger.info(f"Using template '{template_name}' to create server at: {server_path}")

        assembler_linker_conf = AssemblerLinkerConfig()
        path_provider = PathProvider()
        template_path = f"{path_provider.get_templates_path()}/{template_name}.json"

        if not os.path.exists(f"{path_provider.get_templates_path()}/{template_name}.json"):
            self.logger.error(f"Template '{template_name}' not found at: {template_path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return


        print(f"Creating a Minecraft server in: {server_path} (from template: {template_name})")

        try:
            self.logger.debug(f"Reading template from: {template_path}")
            path = f"{path_provider.get_templates_path()}/{template_name}.json"

            with open(path, 'r') as file:
                template_data = json.load(file)

            server_type = template_data.get("template_server_type")
            server_version = template_data.get("template_server_version")
            locker_entry = template_data.get("template_locker_entry")
            linker_config_data = template_data.get("template_linker_config")

            self.logger.debug(f"Template data - type: {server_type}, version: {server_version}")

            if not all([server_type, server_version, linker_config_data]):
                self.logger.error("Template missing required fields")
                yield Status(StatusCode.ERROR_TEMPLATE_MISSING_DATA, path)
                return

            assembler_linker_conf.from_dict(linker_config_data)
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format in template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, path)
            return
        except Exception as e:
            self.logger.error(f"Failed to read template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_READ_FAILED, str(e))
            return

        server = ServerHandler()
        self.logger.info(f"Creating server using template data")
        for status in server.create(server_path, server_type, server_version, locker_entry, assembler_linker_conf):
            yield status

    def list_templates(self) -> Iterator[Status]:
        self.logger.info("Listing available templates")

        templates = []
        for template_file in os.listdir(PathProvider().get_templates_path()):
            templates.append(template_file.split(".")[0])

        self.logger.info(f"Found {len(templates)} templates")
        yield Status(StatusCode.SUCCESS, templates)

    def refresh_template(self, template_name) -> Iterator[Status]:
        self.logger.info(f"Refreshing template: {template_name}")

        locker_manager = LockerUpdater()
        path_provider = PathProvider()
        template_path = f"{path_provider.get_templates_path()}/{template_name}.json"


        if not os.path.exists(template_path):
            self.logger.error(f"Template '{template_name}' not found at: {template_path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        self.logger.debug("Loading locker data")
        for status in locker_manager.load_locker():
            if status.status_code != StatusCode.SUCCESS:
                yield status
            else:
                locker_data = status.status_details
                break

        try:
            self.logger.debug(f"Reading template from: {template_path}")
            with open(template_path, 'r') as file:
                template_data = json.load(file)

            template_name = template_data.get("template_name")
            template_server_type = template_data.get("template_server_type")
            template_server_version = template_data.get("template_server_version")
            template_linker_config_data = template_data.get("template_linker_config")

            self.logger.debug(
                f"Template data - name: {template_name}, type: {template_server_type}, version: {template_server_version}")

            if not all([template_name, template_server_type, template_server_version, template_linker_config_data]):
                self.logger.error(f"Template missing required fields")
                yield Status(StatusCode.ERROR_TEMPLATE_MISSING_DATA, template_name)
                return

            assembler_linker_config = AssemblerLinkerConfig()
            assembler_linker_config.from_dict(template_linker_config_data)

            for version in locker_data["servers"][template_server_type]:
                if version["version"] == template_server_version:
                    template_locker_entry = version
                    self.logger.debug(
                        f"Found updated locker entry for {template_server_type} {template_server_version}")
                    break

            template = Template(
                template_name,
                template_server_type,
                template_server_version,
                template_locker_entry,
                assembler_linker_config
            )

            TemplateManager.save_template(template)

            self.logger.info(f"Template '{template_name}' refreshed successfully")
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format in template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, template_name)
        except Exception as e:
            self.logger.error(f"Failed to refresh template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_REFRESH_FAILED, str(e))
