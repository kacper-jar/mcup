from dataclasses import dataclass

from mcup.core.utils.version import VersionDependantVariablePicker, Version, VersionDependantVariable


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

    def set_configuration_property(self, property_name: str, property_value, version: Version):
        """Set a single configuration property value."""
        if property_value == "":
            self.set_configuration_default_property(property_name, version)
        elif "/" in property_name:
            keys = property_name.split("/")
            current_dict = self.configuration

            for key in keys[:-1]:
                if key not in current_dict:
                    current_dict[key] = {}
                current_dict = current_dict[key]

            current_dict[keys[-1]] = property_value
        else:
            self.configuration[property_name] = property_value

    def set_configuration_properties(self, properties: dict, version: Version):
        """Set multiple configuration property values from a dictionary."""
        for property_name, property_value in properties.items():
            self.set_configuration_property(property_name, property_value, version)

    def set_configuration_default_property(self, property_name: str, version: Version):
        """Reset a configuration property to its default value."""
        if "/" in property_name:
            keys = property_name.split("/")
            config_dict = self.configuration
            default_dict = self.default_configuration

            for key in keys[:-1]:
                if key not in config_dict:
                    config_dict[key] = {}
                config_dict = config_dict[key]

                if key not in default_dict:
                    return
                default_dict = default_dict[key]

            last_key = keys[-1]
            if last_key in default_dict:
                if isinstance(default_dict[last_key], VersionDependantVariablePicker):
                    config_dict[last_key] = default_dict[last_key].resolve(version)
                elif isinstance(default_dict[last_key], list):
                    if len(default_dict[last_key]) > 0 and isinstance(default_dict[last_key][0], VersionDependantVariable):
                        config_dict[last_key] = VersionDependantVariablePicker(default_dict[last_key]).resolve(version)
                    else:
                        config_dict[last_key] = default_dict[last_key]
                else:
                    config_dict[last_key] = default_dict[last_key]
        else:
            if isinstance(self.default_configuration[property_name], VersionDependantVariablePicker):
                self.configuration[property_name] = self.default_configuration[property_name].resolve(version)
            elif isinstance(self.default_configuration[property_name], list):
                if len(self.default_configuration[property_name]) > 0 and isinstance(self.default_configuration[property_name][0], VersionDependantVariable):
                    self.configuration[property_name] = VersionDependantVariablePicker(self.default_configuration[property_name]).resolve(version)
                else:
                    self.configuration[property_name] = self.default_configuration[property_name]
            else:
                self.configuration[property_name] = self.default_configuration[property_name]

    def set_configuration_default_properties(self, properties: list, version: Version):
        """Reset multiple configuration properties to their default values."""
        for property_name in properties:
            self.set_configuration_default_property(property_name, version)

    def set_configuration_default_all_properties(self, version: Version):
        """Reset all configuration properties to their default values."""
        self.set_configuration_default_properties(list(self.default_configuration.keys()), version)

    def get_default_configuration(self) -> dict:
        """Get the default configuration dictionary."""
        return self.default_configuration

    def get_default_values_for_variables(self, variable_names: list[str], version: Version) -> dict:
        """Get default values for specific variables."""
        defaults = {}

        for variable_name in variable_names:
            default_value = self._get_default_value_for_variable(variable_name, version)
            defaults[variable_name] = default_value

        return defaults

    def _get_default_value_for_variable(self, variable_name: str, version: Version):
        """Get the default value for a single variable."""
        if self.default_configuration is None:
            return None

        if "/" in variable_name:
            keys = variable_name.split("/")
            current_dict = self.default_configuration

            for key in keys:
                if isinstance(current_dict, dict) and key in current_dict:
                    current_dict = current_dict[key]
                else:
                    return None

            if isinstance(current_dict, VersionDependantVariablePicker):
                return current_dict.resolve(version)
            elif isinstance(current_dict, list):
                if len(current_dict) > 0 and isinstance(current_dict[0], VersionDependantVariable):
                    return VersionDependantVariablePicker(current_dict).resolve(version)
                else:
                    return current_dict
            else:
                return current_dict
        else:
            if variable_name in self.default_configuration:
                default_val = self.default_configuration[variable_name]
                if isinstance(default_val, VersionDependantVariablePicker):
                    return default_val.resolve(version)
                elif isinstance(default_val, list):
                    if len(default_val) > 0 and isinstance(default_val[0], VersionDependantVariable):
                        return VersionDependantVariablePicker(default_val).resolve(version)
                    else:
                        return default_val
                else:
                    return default_val
            else:
                return None
