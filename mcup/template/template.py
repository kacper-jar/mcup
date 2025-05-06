from dataclasses import dataclass

from mcup.config_assemblers import AssemblerLinkerConfig


@dataclass
class Template:
    """Class representing template data."""
    template_name: str
    template_server_type: str
    template_server_version: str
    template_server_source: str
    template_server_target: str
    template_linker_config: AssemblerLinkerConfig

    def get_template_name(self) -> str:
        """Get the template name."""
        return self.template_name

    def get_template_server_type(self) -> str:
        """Get the template server type."""
        return self.template_server_type

    def get_template_server_version(self) -> str:
        """Get the template server version."""
        return self.template_server_version

    def get_template_server_source(self) -> str:
        """Get the template server source."""
        return self.template_server_source

    def get_template_server_target(self) -> str:
        """Get the template server target."""
        return self.template_server_target

    def get_template_linker_config(self) -> AssemblerLinkerConfig:
        """Get the template linker config."""
        return self.template_linker_config

    def get_dict(self):
        """Get the template data as dictionary."""
        return {
            "template_name": self.template_name,
            "template_server_type": self.template_server_type,
            "template_server_version": self.template_server_version,
            "template_server_source": self.template_server_source,
            "template_server_target": self.template_server_target,
            "template_linker_config": self.template_linker_config.to_dict(export_default_config=False)
        }
