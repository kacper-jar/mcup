from mcup.core.configs import ConfigFile


class DockerFile(ConfigFile):
    """Class representing a Dockerfile for the Minecraft server."""

    def __init__(self):
        """Initialize the Dockerfile configuration."""
        self.config_file_name = "Dockerfile"
        self.config_file_path = "."

        self.configuration = {
            "java-version": "21",
            "server-jar": "server.jar",
            "server-args-instead-of-jar": False,
            "memory-initial": "1G",
            "memory-max": "2G",
            "port": "25565"
        }

        self.default_configuration = self.configuration.copy()
