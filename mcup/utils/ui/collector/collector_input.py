from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from mcup.utils.ui.collector import CollectorInputType
    from mcup.utils.version import Version


@dataclass
class CollectorInput:
    variable_name: str
    variable_prompt: str
    variable_input_type: "CollectorInputType"

    variable_min_version: "Version"
    variable_max_version: "Version"

    def get_variable_name(self) -> str:
        return self.variable_name

    def get_variable_prompt(self) -> str:
        return self.variable_prompt

    def get_variable_input_type(self) -> "CollectorInputType":
        return self.variable_input_type
