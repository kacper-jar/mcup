from typing import Any, TYPE_CHECKING

from mcup.core.utils.version import Version

if TYPE_CHECKING:
    from mcup.core.utils.version import VersionDependantVariable


class VersionDependantVariablePicker:
    def __init__(self, variables: list["VersionDependantVariable"]):
        self.variables = variables

    def get_variables(self) -> list["VersionDependantVariable"]:
        return self.variables

    def resolve(self, version: Version) -> Any:
        for variable in self.variables:
            if variable.get_variable_min_version() <= version <= variable.get_variable_max_version():
                return variable.get_variable_value()
        return None
