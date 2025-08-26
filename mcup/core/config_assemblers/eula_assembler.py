from mcup.core.config_assemblers import Assembler
from mcup.core.configs import EulaFile


class EulaAssembler(Assembler):
    """Class representing eula file assembler."""

    @staticmethod
    def assemble(path: str, config: EulaFile):
        """Assemble eula file at the specified path."""
        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            config_file.write(f"""
#By changing the setting below to TRUE you are indicating your agreement to Minecraft EULA (https://aka.ms/MinecraftEULA).
eula=true""")
