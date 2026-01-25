import json
import logging
import os
from pathlib import Path
from typing import Iterator, Dict, Any, Tuple, Optional

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
        self.path_provider = PathProvider()

    def create_template(self, template_name: str, server_type: str, server_version: str, locker_entry: dict,
                        assembler_linker_conf: AssemblerLinkerConfig) -> Iterator[Status]:
        """Create a new template with the provided configuration."""
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

    def import_template(self, path: str) -> Iterator[Status]:
        """Import a template from a file."""
        self.logger.info(f"Importing template from: {path}")

        if not os.path.exists(path):
            self.logger.error(f"Template file not found: {path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        template_data = self._read_template_file(path)
        if template_data is None:
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, path)
            return

        validation_result = self._validate_template_data(template_data, path)
        if validation_result is not None:
            yield validation_result
            return

        try:
            template = self._create_template_from_data(template_data)
            TemplateManager.save_template(template)

            self.logger.info(f"Template '{template_data['template_name']}' imported successfully from {path}")
            yield Status(StatusCode.SUCCESS)
        except Exception as e:
            self.logger.error(f"Failed to import template from '{path}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_IMPORT_FAILED, str(e))

    def export_template(self, template_name: str, destination: str) -> Iterator[Status]:
        """Export a template to a file."""
        self.logger.info(f"Exporting template '{template_name}' to: {destination}")

        template_path = self._get_template_path(template_name)
        if not os.path.exists(template_path):
            self.logger.error(f"Template '{template_name}' not found at: {template_path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        try:
            self._ensure_destination_directory(destination)
            template_data = self._read_template_file(template_path)

            if template_data is None:
                yield Status(StatusCode.ERROR_TEMPLATE_READ_FAILED, template_name)
                return

            self._write_template_file(destination, template_data)
            self.logger.info(f"Template '{template_name}' exported successfully to {destination}")
            yield Status(StatusCode.SUCCESS)
        except Exception as e:
            self.logger.error(f"Failed to export template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_EXPORT_FAILED, str(e))

    def delete_template(self, template_name: str) -> Iterator[Status]:
        """Delete a template."""
        self.logger.info(f"Deleting template: {template_name}")

        template_path = self._get_template_path(template_name)
        if os.path.exists(template_path):
            os.remove(template_path)
            self.logger.info(f"Template '{template_name}' deleted successfully")
            yield Status(StatusCode.SUCCESS)
        else:
            self.logger.error(f"Template '{template_name}' not found at: {template_path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)

    def use_template(self, template_name: str, server_path: str | Path) -> Iterator[Status]:
        """Use a template to create a server."""
        self.logger.info(f"Using template '{template_name}' to create server at: {server_path}")
        print(f"Creating a Minecraft server in: {server_path} (from template: {template_name})")

        template_path = self._get_template_path(template_name)
        if not os.path.exists(template_path):
            self.logger.error(f"Template '{template_name}' not found at: {template_path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        template_config = yield from self._load_template_for_use(template_name)
        if template_config is None:
            return

        server_type, server_version, locker_entry, assembler_linker_conf = template_config

        server = ServerHandler()
        self.logger.info("Creating server using template data")
        yield from server.create(server_path, server_type, server_version, locker_entry, assembler_linker_conf)

    def list_templates(self) -> Iterator[Status]:
        """List all available templates."""
        self.logger.info("Listing available templates")

        templates = []
        templates_path = self.path_provider.get_templates_path()

        for template_file in os.listdir(templates_path):
            if template_file.endswith('.json'):
                templates.append(template_file.split(".")[0])

        self.logger.info(f"Found {len(templates)} templates")
        yield Status(StatusCode.SUCCESS, templates)

    def refresh_template(self, template_name: str) -> Iterator[Status]:
        """Refresh a template with updated locker data."""
        self.logger.info(f"Refreshing template: {template_name}")

        template_path = self._get_template_path(template_name)
        if not os.path.exists(template_path):
            self.logger.error(f"Template '{template_name}' not found at: {template_path}")
            yield Status(StatusCode.ERROR_TEMPLATE_NOT_FOUND)
            return

        locker_data = yield from self._load_locker_data()
        if locker_data is None:
            return

        template_data = self._read_template_file(template_path)
        if template_data is None:
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, template_name)
            return

        validation_result = self._validate_template_data_for_refresh(template_data, template_name)
        if validation_result is not None:
            yield validation_result
            return

        try:
            updated_locker_entry = self._find_updated_locker_entry(
                locker_data, template_data["template_server_type"], template_data["template_server_version"]
            )

            if updated_locker_entry is None:
                self.logger.error(
                    f"No locker entry found for {template_data['template_server_type']} {template_data['template_server_version']}")
                yield Status(StatusCode.ERROR_TEMPLATE_REFRESH_FAILED, f"Locker entry not found")
                return

            assembler_linker_config = AssemblerLinkerConfig()
            assembler_linker_config.from_dict(template_data["template_linker_config"])

            template = Template(
                template_data["template_name"],
                template_data["template_server_type"],
                template_data["template_server_version"],
                updated_locker_entry,
                assembler_linker_config
            )

            TemplateManager.save_template(template)
            self.logger.info(f"Template '{template_name}' refreshed successfully")
            yield Status(StatusCode.SUCCESS)
        except Exception as e:
            self.logger.error(f"Failed to refresh template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_REFRESH_FAILED, str(e))

    def _read_template_file(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Read and parse a template JSON file."""
        try:
            self.logger.debug(f"Reading template file: {file_path}")
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format in file '{file_path}': {e}")
            return None
        except Exception as e:
            self.logger.error(f"Failed to read template file '{file_path}': {e}")
            return None

    def _write_template_file(self, file_path: str, template_data: Dict[str, Any]) -> None:
        """Write template data to a JSON file."""
        self.logger.debug(f"Writing template to: {file_path}")
        with open(file_path, 'w') as dest_file:
            json.dump(template_data, dest_file, indent=4)

    def _validate_template_data(self, template_data: Dict[str, Any], source_path: str) -> Optional[Status]:
        """Validate that template data contains all required fields."""
        required_fields = ["template_name", "template_server_type", "template_server_version",
                           "template_locker_entry", "template_linker_config"]

        if not all(template_data.get(field) for field in required_fields):
            self.logger.error(f"Template missing required fields in {source_path}")
            return Status(StatusCode.ERROR_TEMPLATE_MISSING_DATA, source_path)

        self.logger.debug(
            f"Template data - name: {template_data['template_name']}, "
            f"type: {template_data['template_server_type']}, "
            f"version: {template_data['template_server_version']}"
        )
        return None

    def _validate_template_data_for_refresh(self, template_data: Dict[str, Any], template_name: str) -> Optional[
        Status]:
        """Validate template data for refresh operation."""
        required_fields = ["template_name", "template_server_type", "template_server_version", "template_linker_config"]

        if not all(template_data.get(field) for field in required_fields):
            self.logger.error("Template missing required fields")
            return Status(StatusCode.ERROR_TEMPLATE_MISSING_DATA, template_name)

        self.logger.debug(
            f"Template data - name: {template_data['template_name']}, "
            f"type: {template_data['template_server_type']}, "
            f"version: {template_data['template_server_version']}"
        )
        return None

    def _create_template_from_data(self, template_data: Dict[str, Any]) -> Template:
        """Create a Template object from template data."""
        assembler_linker_config = AssemblerLinkerConfig()
        assembler_linker_config.from_dict(template_data["template_linker_config"])

        return Template(
            template_data["template_name"],
            template_data["template_server_type"],
            template_data["template_server_version"],
            template_data["template_locker_entry"],
            assembler_linker_config
        )

    def _get_template_path(self, template_name: str) -> str:
        """Get the full path to a template file."""
        return f"{self.path_provider.get_templates_path()}/{template_name}.json"

    def _ensure_destination_directory(self, destination: str) -> None:
        """Ensure the destination directory exists."""
        destination_dir = os.path.dirname(destination)
        if destination_dir and not os.path.exists(destination_dir):
            self.logger.debug(f"Creating destination directory: {destination_dir}")
            os.makedirs(destination_dir)

    def _load_template_for_use(self, template_name: str) -> Optional[Tuple[str, str, dict, AssemblerLinkerConfig]]:
        """Load template data for server creation."""
        template_path = self._get_template_path(template_name)

        try:
            template_data = self._read_template_file(template_path)
            if template_data is None:
                return None

            server_type = template_data.get("template_server_type")
            server_version = template_data.get("template_server_version")
            locker_entry = template_data.get("template_locker_entry")
            linker_config_data = template_data.get("template_linker_config")

            self.logger.debug(f"Template data - type: {server_type}, version: {server_version}")

            if not all([server_type, server_version, linker_config_data]):
                self.logger.error("Template missing required fields")
                yield Status(StatusCode.ERROR_TEMPLATE_MISSING_DATA, template_path)
                return None

            assembler_linker_conf = AssemblerLinkerConfig()
            assembler_linker_conf.from_dict(linker_config_data)

            return server_type, server_version, locker_entry, assembler_linker_conf

        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format in template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT, template_path)
            return None
        except Exception as e:
            self.logger.error(f"Failed to read template '{template_name}': {e}")
            yield Status(StatusCode.ERROR_TEMPLATE_READ_FAILED, str(e))
            return None

    def _load_locker_data(self) -> Iterator[Optional[Dict[str, Any]]]:
        """Load locker data for template refresh."""
        locker_manager = LockerUpdater()
        self.logger.debug("Loading locker data")

        for status in locker_manager.load_locker():
            if status.status_code != StatusCode.SUCCESS:
                yield status
                return
            else:
                locker_data = status.status_details
                return locker_data

    def _find_updated_locker_entry(self, locker_data: Dict[str, Any], server_type: str,
                                   server_version: str) -> Optional[Dict[str, Any]]:
        """Find the updated locker entry for a specific server type and version."""
        servers = locker_data.get("servers", {})
        server_versions = servers.get(server_type, [])

        for version in server_versions:
            if version.get("version") == server_version:
                self.logger.debug(f"Found updated locker entry for {server_type} {server_version}")
                return version

        self.logger.warning(f"No locker entry found for {server_type} {server_version}")
        return None
