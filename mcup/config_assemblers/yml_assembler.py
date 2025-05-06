import yaml

from mcup.config_assemblers import Assembler
from mcup.configs import ConfigFile


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
    def assemble(path: str, config: ConfigFile):
        """Assemble and write YAML configuration to the specified path."""
        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            filtered_config = YmlAssembler.clean_config(config.get_configuration())
            yaml.dump(
                filtered_config,
                config_file,
                sort_keys=False,
                default_flow_style=False,
                default_style=None
            )
