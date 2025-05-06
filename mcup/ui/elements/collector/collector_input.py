from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcup.ui.elements.collector import CollectorInputType
    from mcup.utils.version import Version


@dataclass
class CollectorInput:
    """Class representing a collector input."""
    variable_name: str
    variable_prompt: str
    variable_input_type: "CollectorInputType"

    variable_min_version: "Version"
    variable_max_version: "Version"

    def get_variable_name(self) -> str:
        """Get variable name."""
        return self.variable_name

    def get_variable_prompt(self) -> str:
        """Get variable prompt."""
        return self.variable_prompt

    def get_variable_input_type(self) -> "CollectorInputType":
        """Get variable input type."""
        return self.variable_input_type
