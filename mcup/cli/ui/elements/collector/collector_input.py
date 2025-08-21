from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcup.cli.ui.elements.collector import CollectorInputType, CollectorInputMode
    from mcup.core.utils.version import Version


@dataclass
class CollectorInput:
    """Class representing a collector input."""
    variable_name: str
    variable_prompt_key: str
    variable_input_type: "CollectorInputType"
    variable_input_mode: "CollectorInputMode"

    variable_min_version: "Version"
    variable_max_version: "Version"

    def get_variable_name(self) -> str:
        """Get variable name."""
        return self.variable_name

    def get_variable_prompt_key(self) -> str:
        """Get variable prompt key."""
        return self.variable_prompt_key

    def get_variable_input_type(self) -> "CollectorInputType":
        """Get variable input type."""
        return self.variable_input_type

    def get_variable_input_mode(self) -> "CollectorInputMode":
        """Get variable input mode."""
        return self.variable_mode
