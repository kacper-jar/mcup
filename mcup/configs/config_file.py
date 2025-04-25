from dataclasses import dataclass


@dataclass
class ConfigFile:
    """Class representing a Minecraft server configuration file."""
    config_file_name: str = ""
    config_file_path: str = ""
    configuration: dict = None
    default_configuration: dict = None

    def get_file_name(self) -> str:
        """Get the name of the configuration file."""
        return self.config_file_name

    def get_file_path(self) -> str:
        """Get the path to the configuration file."""
        return self.config_file_path

    def get_configuration(self) -> dict:
        """Get the current configuration dictionary."""
        return self.configuration

    def set_configuration(self, configuration: dict):
        """Set the entire configuration dictionary."""
        self.configuration = configuration

    def set_configuration_property(self, property_name: str, property_value):
        """Set a single configuration property value."""
        if property_value == "":
            self.set_configuration_default_property(property_name)
        elif ":" in property_name:
            parts = property_name.split(":", 1)
            outer_key = parts[0]
            inner_key = parts[1]

            self.configuration[outer_key][inner_key] = property_value
        else:
            self.configuration[property_name] = property_value

    def set_configuration_properties(self, properties: dict):
        """Set multiple configuration property values from a dictionary."""
        for property_name, property_value in properties.items():
            self.set_configuration_property(property_name, property_value)

    def set_configuration_default_property(self, property_name: str):
        """Reset a configuration property to its default value."""
        if ":" in property_name:
            parts = property_name.split(":", 1)
            outer_key = parts[0]
            inner_key = parts[1]

            self.configuration[outer_key][inner_key] = self.default_configuration[outer_key][inner_key]
        else:
            self.configuration[property_name] = self.default_configuration[property_name]

    def set_configuration_default_properties(self, properties: list):
        """Reset multiple configuration properties to their default values."""
        for property_name in properties:
            self.set_configuration_default_property(property_name)

    def get_default_configuration(self) -> dict:
        """Get the default configuration dictionary."""
        return self.default_configuration
