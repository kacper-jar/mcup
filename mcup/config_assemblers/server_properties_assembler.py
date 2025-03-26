from mcup.config_assemblers import Assembler
from mcup.configs import ServerPropertiesConfig


class ServerPropertiesAssembler(Assembler):
    """Class representing server.properties configuration file assembler."""
    @staticmethod
    def assemble(config: ServerPropertiesConfig):
        with open(f"{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            config_file.write("#Minecraft Server Properties\n#Generated using mcup\n")
            for var, key in config.get_configuration().items():
                if key is None:
                    continue
                config_file.write(f"{var}={key}\n")
