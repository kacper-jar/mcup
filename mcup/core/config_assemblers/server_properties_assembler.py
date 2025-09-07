import os
from pathlib import Path

from mcup.core.config_assemblers import Assembler
from mcup.core.configs import ServerPropertiesConfig
from mcup.core.status import StatusCode, Status


class ServerPropertiesAssembler(Assembler):
    """Class representing server.properties configuration file assembler."""

    @staticmethod
    def assemble(path: Path, config: ServerPropertiesConfig) -> Status:
        """Assemble server.properties configuration file at the specified path."""
        path_status = Assembler.validate_path(path)
        if path_status.status_code != StatusCode.SUCCESS:
            return path_status

        config_status = Assembler.validate_config(config)
        if config_status.status_code != StatusCode.SUCCESS:
            return config_status

        try:
            full_dir = Path(os.path.join(path, config.config_file_path))
            status = Assembler.create_directory_if_needed(full_dir)
            if status.status_code != StatusCode.SUCCESS:
                return status

            lines = []
            configuration = config.get_configuration()
            if configuration:
                for var, key in configuration.items():
                    if key is not None:
                        lines.append(f"{var}={key}")

            content = "\n".join(lines) + "\n" if lines else ""

            full_path = Path(os.path.join(full_dir, config.config_file_name))
            return Assembler.safe_write_file(full_path, content)

        except Exception as e:
            return Status(StatusCode.ERROR_CONFIG_ASSEMBLY_FAILED, [config.get_file_name(), str(e)])
