from mcup.core.configs import ConfigFile


class DockerComposeFile(ConfigFile):
    """Class representing a docker-compose.yml for the Minecraft server."""

    def __init__(self):
        """Initialize the docker-compose.yml configuration."""
        self.config_file_name = "docker-compose.yml"
        self.config_file_path = "."

        self.configuration = {
            "service-name": "minecraft-server",
            "container-name": "minecraft-server",
            "port": "25565",
            "uid": 1000,
            "gid": 1000
        }

        self.default_configuration = self.configuration.copy()
