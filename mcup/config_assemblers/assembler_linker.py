from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcup.config_assemblers import AssemblerLinkerConfig, Assembler
    from mcup.configs import ConfigFile


class AssemblerLinker:
    """Links configuration files with their appropriate assemblers."""
    def __init__(self, configuration: "AssemblerLinkerConfig" = None):
        """Initialize the assembler linker with optional configuration."""
        self.configuration = configuration
        self.linked_files: dict = {}

    def set_configuration(self, configuration: "AssemblerLinkerConfig"):
        """Set the configuration for the assembler linker."""
        self.configuration = configuration

    def get_configuration(self) -> "AssemblerLinkerConfig":
        """Get the current configuration of the assembler linker."""
        return self.configuration

    def add_configuration_file(self, configuration_file: "ConfigFile"):
        """Add a configuration file to the current configuration."""
        self.configuration.add_configuration_file(configuration_file)

    def link(self):
        """Link configuration files with their appropriate assemblers."""
        from mcup.config_assemblers import ServerPropertiesAssembler, YmlAssembler

        for config_file in self.configuration.get_configuration_files():
            if config_file.get_file_name() == "server.properties":
                self.linked_files[config_file.config_file_name] = ServerPropertiesAssembler()
                continue

            if config_file.get_file_name() in ["bukkit.yml"]:
                self.linked_files[config_file.config_file_name] = YmlAssembler()
                continue
        print(self.linked_files)

    def get_linked_files(self) -> dict[str, "Assembler"]:
        """Get all linked files with their assemblers."""
        return self.linked_files

    def get_linked_file_count(self) -> int:
        """Get the count of linked files."""
        return len(self.linked_files)

    def drop_linked_files(self):
        """Clear all linked files."""
        self.linked_files = {}

    def assemble_linked_files(self, path):
        """Assemble all linked configuration files at the specified path."""
        for config_file_name, assembler in self.get_linked_files().items():
            for config_file in self.configuration.get_configuration_files():
                if config_file.get_file_name() == config_file_name:
                    file = config_file

            assembler.assemble(path, file)
