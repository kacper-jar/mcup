from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcup.config_assemblers import AssemblerLinkerConfig, Assembler
    from mcup.configs import ConfigFile


class AssemblerLinker:
    def __init__(self, configuration: "AssemblerLinkerConfig" = None):
        self.configuration = configuration
        self.linked_files: dict = {}

    def set_configuration(self, configuration: "AssemblerLinkerConfig"):
        self.configuration = configuration

    def get_configuration(self) -> "AssemblerLinkerConfig":
        return self.configuration

    def add_configuration_file(self, configuration_file: "ConfigFile"):
        self.configuration.add_configuration_file(configuration_file)

    def link(self):
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
        return self.linked_files

    def get_linked_file_count(self) -> int:
        return len(self.linked_files)

    def drop_linked_files(self):
        self.linked_files = {}

    def assemble_linked_files(self, path):
        for config_file_name, assembler in self.get_linked_files().items():
            for config_file in self.configuration.get_configuration_files():
                if config_file.get_file_name() == config_file_name:
                    file = config_file

            assembler.assemble(path, file)
