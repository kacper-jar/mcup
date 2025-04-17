import yaml

from mcup.config_assemblers import Assembler
from mcup.configs import ConfigFile


class YmlAssembler(Assembler):
    """Class representing yaml configuration files assembler."""
    @staticmethod
    def assemble(path: str, config: ConfigFile):
        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            filtered_config = {key: value for key, value in config.get_configuration().items() if value is not None}
            yaml.dump(
                filtered_config,
                config_file,
                sort_keys=False,
                default_flow_style=False
            )
