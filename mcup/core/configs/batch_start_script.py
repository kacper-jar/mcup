from mcup.core.configs import StartScript


class BatchStartScript(StartScript):
    def __init__(self):
        """Initialize the start script (start.bat)."""
        super().__init__()

        self.config_file_name = "start.bat"
