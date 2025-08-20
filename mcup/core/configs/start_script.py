from mcup.core.configs import ConfigFile


class StartScript(ConfigFile):
    def __init__(self):
        """Initialize the start script."""
        self.config_file_name = ""
        self.config_file_path = "."

        self.configuration = {
            "server-jar": None,
            "server-args-instead-of-jar": None,

            "screen-name": None,
            "initial-heap": None,
            "max-heap": None,
            "use-aikars-flags": None,
            "max-restarts": None,
            "restart-delay": None
        }

        self.default_configuration = {
            "server-jar": None,
            "server-args-instead-of-jar": None,

            "screen-name": "server",
            "initial-heap": 1024,
            "max-heap": 1024,
            "use-aikars-flags": False,
            "max-restarts": 10,
            "restart-delay": 5
        }
