import os
from pathlib import Path

from mcup.core.config_assemblers import Assembler
from mcup.core.configs import EulaFile
from mcup.core.status import StatusCode, Status


class EulaAssembler(Assembler):
    """Class representing eula file assembler."""

    @staticmethod
    def assemble(path: Path, config: EulaFile) -> Status:
        """Assemble eula file at the specified path."""
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

            content = "#By changing the setting below to TRUE you are indicating your agreement to Minecraft EULA (https://aka.ms/MinecraftEULA).\neula=true"

            full_path = Path(os.path.join(full_dir, config.config_file_name))
            return Assembler.safe_write_file(full_path, content)

        except Exception as e:
            return Status(StatusCode.ERROR_CONFIG_ASSEMBLY_FAILED, [config.get_file_name(), str(e)])
