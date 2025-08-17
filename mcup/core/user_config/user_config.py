import json
import os

from mcup.core.utils.path import PathProvider


class UserConfig:
    """Class to manage user configuration."""

    def __init__(self):
        """Initialize the user configuration manager."""
        self.user_config = {}
        self.config_file = self.get_config_file_path()
        self.load_configuration()

    def get_config_file_path(self):
        """Get the path to the user configuration file."""
        path_provider = PathProvider()
        path = path_provider.get_config_path() / "userconfig.json"
        return path

    def load_configuration(self):
        """Load configuration from the user configuration file."""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.user_config = json.load(f)
        except Exception as e:
            print(f"Error loading settings: {e}")
            self.user_config = {}

    def save_configuration(self):
        """Save configuration to the user configuration file."""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.user_config, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def get_configuration(self, key, default=None):
        """
        Get a configuration value.

        Args:
            key: The configuration key
            default: Default value if the configuration doesn't exist

        Returns:
            The setting value or the default value
        """
        return self.user_config.get(key, default)

    def set_configuration(self, key, value):
        """
        Set a configuration value.

        Args:
            key: The configuration key
            value: The configuration value
        """
        self.user_config[key] = value
        self.save_configuration()
