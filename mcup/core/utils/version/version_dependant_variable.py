from dataclasses import dataclass
from typing import Any

from mcup.core.utils.version import Version


@dataclass
class VersionDependantVariable:
    """Class representing a version dependant variable."""
    variable_min_version: Version
    variable_max_version: Version
    variable_value: Any

    def get_variable_min_version(self) -> Version:
        return self.variable_min_version

    def get_variable_max_version(self) -> Version:
        return self.variable_max_version

    def get_variable_value(self) -> Any:
        return self.variable_value
