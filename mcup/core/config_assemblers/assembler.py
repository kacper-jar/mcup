import os
from dataclasses import dataclass
from pathlib import Path

from mcup.core.configs import ConfigFile
from mcup.core.status import StatusCode, Status


@dataclass
class Assembler:
    """Base class for configuration file assemblers with safety features."""

    @staticmethod
    def validate_path(path: Path) -> Status:
        """Validate if path is writable."""
        if not path or not isinstance(path, Path):
            return Status(StatusCode.ERROR_CONFIG_PATH_INVALID, path)

        try:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

            test_file = os.path.join(path, '.mcup_test_write')
            try:
                with open(test_file, 'w') as f:
                    f.write('test')
                os.remove(test_file)
            except (OSError, IOError):
                return Status(StatusCode.ERROR_CONFIG_PATH_NOT_WRITABLE, path)

        except Exception as e:
            return Status(StatusCode.ERROR_CONFIG_PATH_INVALID, path)

        return Status(StatusCode.SUCCESS)

    @staticmethod
    def validate_config(config: ConfigFile) -> Status:
        """Validate configuration structure."""
        if not config:
            return Status(StatusCode.ERROR_CONFIG_VALIDATION_FAILED, "Config object is None")

        if not hasattr(config, 'config_file_name') or not config.config_file_name:
            return Status(StatusCode.ERROR_CONFIG_VALIDATION_FAILED, "Missing config_file_name")

        if not hasattr(config, 'config_file_path'):
            return Status(StatusCode.ERROR_CONFIG_VALIDATION_FAILED, "Missing config_file_path")

        return Status(StatusCode.SUCCESS)

    @staticmethod
    def safe_write_file(filepath: Path, content: str) -> Status:
        """Safely write content to file with error handling."""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return Status(StatusCode.SUCCESS)
        except (OSError, IOError, UnicodeError) as e:
            return Status(StatusCode.ERROR_CONFIG_FILE_WRITE_FAILED, [filepath, str(e)])

    @staticmethod
    def create_directory_if_needed(path: Path) -> Status:
        """Create directory structure if it doesn't exist."""
        try:
            os.makedirs(path, exist_ok=True)
            return Status(StatusCode.SUCCESS)
        except (OSError, IOError) as e:
            return Status(StatusCode.ERROR_CONFIG_DIRECTORY_CREATE_FAILED, [path, str(e)])

    @staticmethod
    def assemble(path: Path, config: ConfigFile) -> Status:
        """Assemble configuration file at the specified path."""
        return Status(StatusCode.SUCCESS)
