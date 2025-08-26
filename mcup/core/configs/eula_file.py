from mcup.core.configs import ConfigFile


class EulaFile(ConfigFile):
    """Class representing a eula.txt Minecraft server file."""

    def __init__(self):
        """Initialize the eula.txt file."""
        self.config_file_name = "eula.txt"
        self.config_file_path = "."

        self.configuration = {}

        self.default_configuration = {}
