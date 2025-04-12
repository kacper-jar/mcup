from mcup.configs import ConfigFile


class BukkitConfig(ConfigFile):
    """Class representing a bukkit.yml Minecraft server configuration file"""
    def __init__(self):
        self.config_file_name = "bukkit.yml"
        self.config_file_path = "."

        self.configuration = {

        }

        self.default_configuration = {

        }
