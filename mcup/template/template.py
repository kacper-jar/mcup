from dataclasses import dataclass

from mcup.config_assemblers import AssemblerLinkerConfig


@dataclass
class Template:
    template_name: str
    template_server_type: str
    template_server_version: str
    template_linker_config: AssemblerLinkerConfig

    def get_template_name(self) -> str:
        return self.template_name

    def get_template_server_type(self) -> str:
        return self.template_server_type

    def get_template_server_version(self) -> str:
        return self.template_server_version

    def get_template_linker_config(self) -> AssemblerLinkerConfig:
        return self.template_linker_config

    def get_dict(self):
        return {
            "template_name": self.template_name,
            "template_server_type": self.template_server_type,
            "template_server_version": self.template_server_version,
            "template_linker_config": self.template_linker_config.to_dict()
        }
