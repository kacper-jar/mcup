import yaml

from mcup.config_assemblers import Assembler
from mcup.configs import ConfigFile


class YmlAssembler(Assembler):
    """Class representing yaml configuration files assembler."""
    @staticmethod
    def assemble(path: str, config: ConfigFile):
        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            yaml.dump(config.get_configuration(), config_file, sort_keys=False, default_flow_style=False)
