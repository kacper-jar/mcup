from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .collector_input import CollectorInput


@dataclass
class CollectorSection:
    section_title: str
    section_inputs: list["CollectorInput"]
    # allow_default: bool

    def get_section_title(self) -> str:
        return self.section_title

    def get_section_inputs(self) -> list["CollectorInput"]:
        return self.section_inputs
