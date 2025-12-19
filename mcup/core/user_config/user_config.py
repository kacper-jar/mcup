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
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.user_config = json.load(f)
                self.logger.info(f"Configuration loaded successfully with {len(self.user_config)} keys")
            else:
                self.logger.info("Configuration file not found, using defaults")
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
            yield Status(StatusCode.ERROR_USERCONFIG_SAVE_FAILED, str(e))

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
                yield Status(StatusCode.ERROR_USERCONFIG_KEY_NOT_FOUND, key)
            else:
                self.logger.debug(f"Configuration key '{key}' = {value}")
                yield Status(StatusCode.SUCCESS, value)
        except Exception as e:
            self.logger.error(f"Failed to get configuration key '{key}': {e}")
            yield Status(StatusCode.ERROR_USERCONFIG_READ_FAILED, str(e))

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
            yield Status(StatusCode.ERROR_USERCONFIG_SET_FAILED, str(e))

    def remove_configuration(self, key):
        """
        Remove a configuration value.

        Args:
            key: The configuration key to remove
        """
        self.logger.info(f"Removing configuration key: '{key}'")

        try:
            if key not in self.user_config:
                self.logger.warning(f"Configuration key '{key}' not found for removal")
                yield Status(StatusCode.ERROR_USERCONFIG_KEY_NOT_FOUND, key)
                return

            old_value = self.user_config[key]
            del self.user_config[key]
            self.logger.debug(f"Configuration key '{key}' with value '{old_value}' removed from memory")

            for status in self.save_configuration():
                if status.status_code == StatusCode.SUCCESS:
                    self.logger.info(f"Configuration key '{key}' removed successfully")
                    yield Status(StatusCode.SUCCESS, {"key": key, "old_value": old_value})
                else:
                    self.user_config[key] = old_value
                    self.logger.error(f"Failed to save configuration after removing '{key}', key restored")
                    yield status
        except Exception as e:
            self.logger.error(f"Failed to remove configuration key '{key}': {e}")
            yield Status(StatusCode.ERROR_USERCONFIG_REMOVE_FAILED, str(e))

    def clear_configuration(self):
        """
        Clear all configuration by deleting the userconfig.json file.
        This will reset all user configuration to defaults.
        """
        self.logger.info("Clearing all user configuration")

        try:
            if not os.path.exists(self.config_file):
                self.logger.warning(f"Configuration file '{self.config_file}' does not exist")
                yield Status(StatusCode.ERROR_USERCONFIG_FILE_NOT_FOUND, str(self.config_file))
                return

            keys_count = len(self.user_config)

            os.remove(self.config_file)
            self.logger.debug(f"Configuration file '{self.config_file}' deleted successfully")

            self.user_config.clear()

            self.logger.info(f"All user configuration cleared successfully ({keys_count} keys removed)")
            yield Status(StatusCode.SUCCESS, {"keys_removed": keys_count, "file_path": str(self.config_file)})

        except FileNotFoundError:
            self.logger.warning(f"Configuration file '{self.config_file}' not found during clear operation")
            self.user_config.clear()
            yield Status(StatusCode.ERROR_USERCONFIG_FILE_NOT_FOUND, str(self.config_file))
        except PermissionError as e:
            self.logger.error(f"Permission denied when trying to delete configuration file '{self.config_file}': {e}")
            yield Status(StatusCode.ERROR_USERCONFIG_CLEAR_FAILED, f"Permission denied: {e}")
        except Exception as e:
            self.logger.error(f"Failed to clear configuration: {e}")
            yield Status(StatusCode.ERROR_USERCONFIG_CLEAR_FAILED, str(e))

    def list_configuration(self):
        """
        List all configuration keys and their values.
        """
        self.logger.debug("Listing all configuration keys and values")

        try:
            config_count = len(self.user_config)
            self.logger.debug(f"Found {config_count} configuration entries")

            if config_count == 0:
                output = "No configuration entries found"
            else:
                lines = [f"Current configuration ({config_count} entries):"]

                for key in sorted(self.user_config.keys()):
                    value = self.user_config[key]
                    lines.append(f"  {key} = {value}")

                output = "\n".join(lines)

            self.logger.info(f"Configuration list formatted successfully ({config_count} entries)")
            yield Status(StatusCode.SUCCESS, output)

        except Exception as e:
            self.logger.error(f"Failed to list configuration: {e}")
            yield Status(StatusCode.ERROR_USERCONFIG_LIST_FAILED, str(e))
