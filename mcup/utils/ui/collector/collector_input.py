from dataclasses import dataclass
from typing import Any


@dataclass
class CollectorInput:
    variable_name: str
    variable_prompt: str
    # variable_expected_type: Any

    # optional
    # TODO: change these from ints
    # variable_min_version: int = 0
    # variable_max_version: int = 0

    def get_variable_name(self) -> str:
        return self.variable_name

    def get_variable_prompt(self) -> str:
        return self.variable_prompt

    # def get_variable_expected_type(self) -> Any:
    #     return self.variable_expected_type