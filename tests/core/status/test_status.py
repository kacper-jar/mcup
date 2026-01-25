import pytest
from mcup.core.status.status import Status
from mcup.core.status.status_code import StatusCode


class TestStatus:

    def test_initialization(self):
        """Verify object creation with and without details."""
        status = Status(StatusCode.SUCCESS)
        assert status.status_code == StatusCode.SUCCESS
        assert status.status_details is None

        status_with_details = Status(StatusCode.ERROR_GENERIC, "Something went wrong")
        assert status_with_details.status_details == "Something went wrong"

    def test_getters(self):
        """Verify get_status_code and get_status_details."""
        status = Status(StatusCode.IN_PROGRESS, {"progress": 50})

        assert status.get_status_code() == StatusCode.IN_PROGRESS
        assert status.get_status_details() == {"progress": 50}

    def test_immutability_behavior_check(self):
        """Check mutation behavior."""
        status = Status(StatusCode.SUCCESS)
        status.status_details = "New Details"
        assert status.get_status_details() == "New Details"
