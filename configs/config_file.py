from dataclasses import dataclass


@dataclass
class ConfigFile:
    """Class representing a Minecraft server configuration file."""
    config_file_name: str = ""
    config_file_path: str = ""
    configuration: dict = None