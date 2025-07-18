from mcup.core.config_assemblers import Assembler
from mcup.core.configs import ServerPropertiesConfig


class ServerPropertiesAssembler(Assembler):
    """Class representing server.properties configuration file assembler."""
    @staticmethod
    def assemble(path: str, config: ServerPropertiesConfig):
        """Assemble server.properties configuration file at the specified path."""
        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            for var, key in config.get_configuration().items():
                if key is None:
                    continue
                config_file.write(f"{var}={key}\n")
