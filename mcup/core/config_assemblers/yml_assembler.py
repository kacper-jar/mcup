import os
from pathlib import Path

import yaml

from mcup.core.config_assemblers import Assembler
from mcup.core.configs import ConfigFile
from mcup.core.status import StatusCode, Status


class YmlAssembler(Assembler):
    """Class representing YAML configuration files assembler."""

    @staticmethod
    def clean_config(data):
        """Clean configuration data by removing empty values."""
        if isinstance(data, dict):
            cleaned_dict = {
                k: YmlAssembler.clean_config(v)
                for k, v in data.items()
                if v is not None
            }
            return {k: v for k, v in cleaned_dict.items() if v not in (None, {}, [])}
        elif isinstance(data, list):
            cleaned_list = [
                YmlAssembler.clean_config(item)
                for item in data
                if item is not None
            ]
            return [item for item in cleaned_list if item not in (None, {}, [])]
        return data

    @staticmethod
    def assemble(path: Path, config: ConfigFile) -> Status:
        """Assemble and write YAML configuration to the specified path."""
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

            configuration = config.get_configuration()
            if configuration:
                filtered_config = YmlAssembler.clean_config(configuration)
            else:
                filtered_config = {}

            try:
                full_path = os.path.join(full_dir, config.config_file_name)
                with open(full_path, 'w', encoding='utf-8') as config_file:
                    yaml.dump(
                        filtered_config,
                        config_file,
                        sort_keys=False,
                        default_flow_style=False,
                        default_style=None
                    )
                return Status(StatusCode.SUCCESS)

            except yaml.YAMLError as e:
                return Status(StatusCode.ERROR_CONFIG_ASSEMBLY_FAILED, [config.get_file_name(), str(e)])
            except (OSError, IOError) as e:
                return Status(StatusCode.ERROR_CONFIG_FILE_WRITE_FAILED, [config.get_file_name(), str(e)])

        except Exception as e:
            return Status(StatusCode.ERROR_CONFIG_ASSEMBLY_FAILED, [config.get_file_name(), str(e)])
