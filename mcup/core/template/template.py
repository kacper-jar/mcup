from dataclasses import dataclass

from mcup.core.config_assemblers import AssemblerLinkerConfig


@dataclass
class Template:
    """Class representing template data."""
    template_name: str
    template_server_type: str
    template_server_version: str
    template_locker_entry: dict
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

    def get_template_locker_entry(self) -> dict:
        """Get the template locker entry."""
        return self.template_locker_entry

    def get_template_linker_config(self) -> AssemblerLinkerConfig:
        """Get the template linker config."""
        return self.template_linker_config

    def get_dict(self):
        """Get the template data as a dictionary."""
        return {
            "template_name": self.template_name,
            "template_server_type": self.template_server_type,
            "template_server_version": self.template_server_version,
            "template_locker_entry": self.template_locker_entry,
            "template_linker_config": self.template_linker_config.to_dict(export_default_config=False)
        }
