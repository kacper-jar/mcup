from dataclasses import dataclass

from mcup.configs import ConfigFile


@dataclass
class Assembler:
    """Class representing configuration file assembler."""
    @staticmethod
    def assemble(path: str, config: ConfigFile):
        """Assemble configuration file at the specified path."""
        pass
