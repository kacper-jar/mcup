import typing
from dataclasses import dataclass
from typing import Any

if typing.TYPE_CHECKING:
    from mcup.core.status import StatusCode


@dataclass
class Status:
    """Class representing a status used to communicate with the CLI or any other user interface."""
    status_code: "StatusCode"
    status_details: Any = None

    def get_status_code(self) -> "StatusCode":
        return self.status_code

    def get_status_details(self) -> Any:
        return self.status_details
