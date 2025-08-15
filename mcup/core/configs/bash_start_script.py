from mcup.core.configs import StartScript


class BashStartScript(StartScript):
    def __init__(self):
        """Initialize the start script (start.sh)."""
        super().__init__()

        self.config_file_name = "start.sh"
