from mcup.configs import ConfigFile


class AssemblerLinkerConfig:
    """Configuration for the assembler linker that manages configuration files."""
    def __init__(self):
        """Initialize an empty configuration for the assembler linker."""
        self.configuration_files: list[ConfigFile] = []

    def add_configuration_file(self, configuration_file: ConfigFile):
        """Add a configuration file to the list of managed files."""
        self.configuration_files.append(configuration_file)

    def get_configuration_files(self):
        """Get all configuration files managed by this configuration."""
        return self.configuration_files

    def get_configuration_file_count(self):
        """Get the count of configuration files managed by this configuration."""
        return len(self.configuration_files)

    def to_dict(self, export_default_config=True):
        """Convert the AssemblerLinkerConfig object to a dictionary.

        Returns:
            dict: A dictionary representation of the AssemblerLinkerConfig object.
        """
        config_files = []
        for config_file in self.configuration_files:
            file_dict = {
                'config_file_name': config_file.config_file_name,
                'config_file_path': config_file.config_file_path,
                'configuration': config_file.configuration,
            }
            if export_default_config:
                file_dict['default_configuration'] = config_file.default_configuration

            config_files.append(file_dict)

        return {
            'configuration_files': config_files
        }

    def from_dict(self, data):
        """Populate the AssemblerLinkerConfig object from a dictionary.

        Args:
            data (dict): A dictionary containing the configuration data.

        Returns:
            AssemblerLinkerConfig: The populated AssemblerLinkerConfig object (self).
        """
        self.configuration_files = []

        if 'configuration_files' in data:
            for config_file_data in data['configuration_files']:
                config_file = ConfigFile(
                    config_file_name=config_file_data.get('config_file_name', ''),
                    config_file_path=config_file_data.get('config_file_path', ''),
                    configuration=config_file_data.get('configuration', None),
                    default_configuration=config_file_data.get('default_configuration', None)
                )
                self.add_configuration_file(config_file)

        return self
