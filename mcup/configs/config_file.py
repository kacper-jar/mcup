from dataclasses import dataclass


@dataclass
class ConfigFile:
    """Class representing a Minecraft server configuration file."""
    config_file_name: str = ""
    config_file_path: str = ""
    configuration: dict = None
    default_configuration: dict = None

    def get_file_name(self) -> str:
        return self.config_file_name

    def get_file_path(self) -> str:
        return self.config_file_path

    def get_configuration(self) -> dict:
        return self.configuration

    def set_configuration(self, configuration: dict):
        self.configuration = configuration

    def set_configuration_property(self, property_name: str, property_value):
        if property_value == "":
            self.set_configuration_default_property(property_name)
        else:
            self.configuration[property_name] = property_value

    def set_configuration_properties(self, properties: dict):
        for property_name, property_value in properties.items():
            self.set_configuration_property(property_name, property_value)

    def set_configuration_default_property(self, property_name: str):
        self.configuration[property_name] = self.default_configuration[property_name]

    def set_configuration_default_properties(self, properties: list):
        for property_name in properties:
            self.set_configuration_default_property(property_name)

    def get_default_configuration(self) -> dict:
        return self.default_configuration
