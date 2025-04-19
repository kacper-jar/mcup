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
