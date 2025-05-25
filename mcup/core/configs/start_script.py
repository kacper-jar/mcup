from mcup.core.configs import ConfigFile


class StartScript(ConfigFile):
    def __init__(self):
        """Initialize the start script (start.sh)."""
        self.config_file_name = "start.sh"
        self.config_file_path = "."

        self.configuration = {
            "screen-name": None,
            "initial-heap": None,
            "max-heap": None,
            "server-jar": None
        }

        self.default_configuration = {
            "screen-name": "server",
            "initial-heap": 1024,
            "max-heap": 1024,
            "server-jar": None
        }
