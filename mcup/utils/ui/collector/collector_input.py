from dataclasses import dataclass
from typing import Any


@dataclass
class CollectorInput:
    variable_name: str
    variable_prompt: str
    variable_expected_type: Any

    # optional
    # TODO: change these from ints
    variable_min_version: int
    variable_max_version: int
