import json
import logging
import os

from mcup.core.status import Status, StatusCode
from mcup.core.utils.path import PathProvider


class UserConfig:
    """Class to manage user configuration."""

    def __init__(self):
        """Initialize the user configuration manager."""
        self.logger = logging.getLogger(__name__)

        self.user_config = {}

        path_provider = PathProvider()
        self.config_path = path_provider.get_config_path()
        self.config_file = self.config_path / "userconfig.json"

        self.load_configuration()

        self.logger.debug(f"UserConfig initialized with config file: {self.config_file}")

    def load_configuration(self):
        """Load configuration from the user configuration file."""
        try:
            self.logger.debug(f"Loading configuration from: {self.config_file}")
            if os.path.exists(self.config_path):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.user_config = json.load(f)
            self.logger.info(f"Configuration loaded successfully with {len(self.user_config)} keys")
        except Exception as e:
            self.logger.error(f"Failed to load configuration from '{self.config_file}': {e}")
            self.user_config = {}

    def save_configuration(self):
        """Save configuration to the user configuration file."""
        try:
            if not os.path.exists(self.config_path):
                self.logger.debug(f"Creating configuration directory: {self.config_file}")
                os.makedirs(self.config_path, exist_ok=True)

            self.logger.debug(f"Saving configuration to: {self.config_file}")
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.user_config, f, indent=4)
            self.logger.info(f"Configuration saved successfully with {len(self.user_config)} keys")
            yield Status(StatusCode.SUCCESS)
        except Exception as e:
            self.logger.error(f"Failed to save configuration to '{self.config_file}': {e}")
            yield Status(StatusCode.ERROR_CONFIG_SAVE_FAILED, str(e))

    def get_configuration(self, key, default=None):
        """
        Get a configuration value.

        Args:
            key: The configuration key
            default: Default value if the configuration doesn't exist

        Returns:
            The setting value or the default value
        """
        self.logger.debug(f"Getting configuration key: '{key}' (default: {default})")

        try:
            value = self.user_config.get(key, default)
            if value is None and default is None:
                self.logger.warning(f"Configuration key '{key}' not found and no default provided")
                yield Status(StatusCode.ERROR_CONFIG_KEY_NOT_FOUND, key)
            else:
                self.logger.debug(f"Configuration key '{key}' = {value}")
                yield Status(StatusCode.SUCCESS, value)
        except Exception as e:
            self.logger.error(f"Failed to get configuration key '{key}': {e}")
            yield Status(StatusCode.ERROR_CONFIG_READ_FAILED, str(e))

    def set_configuration(self, key, value):
        """
        Set a configuration value.

        Args:
            key: The configuration key
            value: The configuration value
        """
        self.logger.info(f"Setting configuration: '{key}' = {value}")

        try:
            old_value = self.user_config.get(key)
            self.user_config[key] = value

            if old_value != value:
                self.logger.debug(f"Configuration key '{key}' changed from {old_value} to {value}")
            else:
                self.logger.debug(f"Configuration key '{key}' value unchanged")

            for status in self.save_configuration():
                if status.status_code == StatusCode.SUCCESS:
                    self.logger.info(f"Configuration key '{key}' set successfully")
                    yield Status(StatusCode.SUCCESS, {"key": key, "value": value})
                else:
                    self.logger.error(f"Failed to save configuration after setting '{key}'")
                    yield status
        except Exception as e:
            self.logger.error(f"Failed to set configuration key '{key}': {e}")
            yield Status(StatusCode.ERROR_CONFIG_SET_FAILED, str(e))