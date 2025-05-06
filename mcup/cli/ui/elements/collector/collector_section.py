from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .collector_input import CollectorInput


@dataclass
class CollectorSection:
    """Class representing a collector section."""
    section_title: str
    section_inputs: list["CollectorInput"]
    section_header: str = ""

    def get_section_title(self) -> str:
        """Get the title of the section."""
        return self.section_title

    def get_section_inputs(self) -> list["CollectorInput"]:
        """Get the inputs of the section."""
        return self.section_inputs

    def get_section_header(self) -> str:
        """Get the header of the section."""
        return self.section_header
