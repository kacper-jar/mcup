from pathlib import Path
from typing import TYPE_CHECKING, Optional, Dict

from mcup.core.status import StatusCode, Status

if TYPE_CHECKING:
    from mcup.core.config_assemblers import AssemblerLinkerConfig, Assembler
    from mcup.core.configs import ConfigFile


class AssemblerLinker:
    """Links configuration files with their appropriate assemblers."""

    def __init__(self, configuration: "AssemblerLinkerConfig" = None):
        """Initialize the assembler linker with optional configuration."""
        self.configuration = configuration
        self.linked_files: Dict[str, "Assembler"] = {}

    def set_configuration(self, configuration: "AssemblerLinkerConfig") -> None:
        """Set the configuration for the assembler linker."""
        self.configuration = configuration

    def get_configuration(self) -> "AssemblerLinkerConfig":
        """Get the current configuration of the assembler linker."""
        return self.configuration

    def add_configuration_file(self, configuration_file: "ConfigFile") -> Status:
        """Add a configuration file to the current configuration."""
        try:
            if self.configuration is None:
                return Status(StatusCode.ERROR_CONFIG_VALIDATION_FAILED, "No configuration set")
            self.configuration.add_configuration_file(configuration_file)
            return Status(StatusCode.SUCCESS)
        except Exception as e:
            return Status(StatusCode.ERROR_CONFIG_LINKING_FAILED, str(e))

    def _get_assembler_for_file(self, filename: str) -> Optional["Assembler"]:
        """Get appropriate assembler for filename."""
        from mcup.core.config_assemblers import (
            ServerPropertiesAssembler, YmlAssembler, BashStartScriptAssembler,
            BatchStartScriptAssembler, EulaAssembler
        )

        if filename == "server.properties":
            return ServerPropertiesAssembler()

        if filename in ["bukkit.yml", "spigot.yml", "paper.yml", "paper-global.yml", "paper-world-defaults.yml"]:
            return YmlAssembler()

        if filename == "start.sh":
            return BashStartScriptAssembler()

        if filename == "start.bat":
            return BatchStartScriptAssembler()

        if filename == "eula.txt":
            return EulaAssembler()

        return None

    def link(self) -> Status:
        """Link configuration files with their appropriate assemblers."""
        try:
            if self.configuration is None:
                return Status(StatusCode.ERROR_CONFIG_VALIDATION_FAILED, "No configuration set")

            self.linked_files.clear()
            unsupported_files = []

            for config_file in self.configuration.get_configuration_files():
                filename = config_file.get_file_name()
                assembler = self._get_assembler_for_file(filename)

                if assembler is None:
                    unsupported_files.append(filename)
                else:
                    self.linked_files[filename] = assembler

            if unsupported_files:
                return Status(StatusCode.ERROR_ASSEMBLER_NOT_FOUND, unsupported_files)

            return Status(StatusCode.SUCCESS)

        except Exception as e:
            return Status(StatusCode.ERROR_CONFIG_LINKING_FAILED, str(e))

    def get_linked_files(self) -> Dict[str, "Assembler"]:
        """Get all linked files with their assemblers."""
        return self.linked_files

    def get_linked_file_count(self) -> int:
        """Get the count of linked files."""
        return len(self.linked_files)

    def drop_linked_files(self) -> None:
        """Clear all linked files."""
        self.linked_files.clear()

    def _find_config_file_by_name(self, filename: str) -> Optional["ConfigFile"]:
        """Find configuration file by filename."""
        if self.configuration is None:
            return None

        for config_file in self.configuration.get_configuration_files():
            if config_file.get_file_name() == filename:
                return config_file
        return None

    def assemble_linked_files(self, path: Path) -> Status:
        """Assemble all linked configuration files at the specified path."""
        try:
            if not path or not isinstance(path, Path):
                return Status(StatusCode.ERROR_CONFIG_PATH_INVALID, path)

            if not self.linked_files:
                return Status(StatusCode.SUCCESS)

            for filename, assembler in self.linked_files.items():
                config_file = self._find_config_file_by_name(filename)
                if config_file is None:
                    return Status(StatusCode.ERROR_CONFIG_VALIDATION_FAILED, f"Config file not found: {filename}")

                status = assembler.assemble(path, config_file)
                if status.status_code != StatusCode.SUCCESS:
                    return status

            return Status(StatusCode.SUCCESS)

        except Exception as e:
            return Status(StatusCode.ERROR_CONFIG_ASSEMBLY_FAILED, [path, str(e)])
