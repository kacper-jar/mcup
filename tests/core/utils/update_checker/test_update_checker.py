from unittest.mock import MagicMock, patch

from mcup.core.status import StatusCode
from mcup.core.utils.update_checker.update_checker import UpdateChecker


def _make_release(tag_name: str, published_at: str, prerelease: bool = False, draft: bool = False) -> dict:
    return {
        "tag_name": tag_name,
        "published_at": published_at,
        "prerelease": prerelease,
        "draft": draft,
        "html_url": f"https://github.com/kacper-jar/mcup/releases/tag/{tag_name}",
    }


CURRENT_VERSION = "1.0.1"

OLDER = "2025-01-01T00:00:00Z"
CURRENT = "2026-01-01T00:00:00Z"
NEWER = "2026-06-01T00:00:00Z"

RELEASES_WITH_STABLE_UPDATE = [
    _make_release("1.1.0", NEWER, prerelease=False),
    _make_release(CURRENT_VERSION, CURRENT, prerelease=False),
    _make_release("1.0.0", OLDER, prerelease=False),
]

RELEASES_WITH_PRERELEASE_UPDATE = [
    _make_release("1.1.0-rc1", NEWER, prerelease=True),
    _make_release(CURRENT_VERSION, CURRENT, prerelease=False),
    _make_release("1.0.0", OLDER, prerelease=False),
]

RELEASES_UP_TO_DATE = [
    _make_release(CURRENT_VERSION, NEWER, prerelease=False),
    _make_release("1.0.0", OLDER, prerelease=False),
]

RELEASES_CURRENT_NOT_FOUND = [
    _make_release("1.0.0", CURRENT, prerelease=False),
]


def _mock_response(releases: list) -> MagicMock:
    mock_resp = MagicMock()
    mock_resp.json.return_value = releases
    mock_resp.raise_for_status = MagicMock()
    return mock_resp


class TestUpdateChecker:
    """Tests for UpdateChecker.check_for_update()."""

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_newer_stable_release_channel_stable(self, mock_get):
        """Yields INFO_UPDATE_AVAILABLE when a newer stable release exists (channel=stable)."""
        mock_get.return_value = _mock_response(RELEASES_WITH_STABLE_UPDATE)

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="stable"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.INFO_UPDATE_AVAILABLE
        details = statuses[0].status_details
        assert details["latest_tag"] == "1.1.0"
        assert details["current_version"] == CURRENT_VERSION
        assert details["prerelease"] is False

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_newer_prerelease_channel_all(self, mock_get):
        """Yields INFO_UPDATE_AVAILABLE for a pre-release when channel=all."""
        mock_get.return_value = _mock_response(RELEASES_WITH_PRERELEASE_UPDATE)

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="all"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.INFO_UPDATE_AVAILABLE
        details = statuses[0].status_details
        assert details["latest_tag"] == "1.1.0-rc1"
        assert details["prerelease"] is True

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_newer_prerelease_channel_stable_no_notification(self, mock_get):
        """Does NOT notify about a pre-release when channel=stable."""
        mock_get.return_value = _mock_response(RELEASES_WITH_PRERELEASE_UPDATE)

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="stable"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.SUCCESS

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_already_on_latest(self, mock_get):
        """Yields SUCCESS when no newer release exists."""
        mock_get.return_value = _mock_response(RELEASES_UP_TO_DATE)

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="stable"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.SUCCESS

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_current_tag_not_found(self, mock_get):
        """Yields ERROR_UPDATE_CHECK_FAILED when current tag is absent from API response."""
        mock_get.return_value = _mock_response(RELEASES_CURRENT_NOT_FOUND)

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="stable"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.ERROR_UPDATE_CHECK_FAILED

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_network_timeout_is_silent(self, mock_get):
        """Yields ERROR_UPDATE_CHECK_FAILED on timeout without raising an exception."""
        import requests as req_lib
        mock_get.side_effect = req_lib.exceptions.Timeout("timed out")

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="stable"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.ERROR_UPDATE_CHECK_FAILED

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_network_connection_error_is_silent(self, mock_get):
        """Yields ERROR_UPDATE_CHECK_FAILED on connection error without raising."""
        import requests as req_lib
        mock_get.side_effect = req_lib.exceptions.ConnectionError("no route to host")

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="stable"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.ERROR_UPDATE_CHECK_FAILED

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_version_tag_with_v_prefix(self, mock_get):
        """Handles tags with a leading 'v' prefix correctly."""
        releases = [
            _make_release("v1.1.0", NEWER, prerelease=False),
            _make_release(f"v{CURRENT_VERSION}", CURRENT, prerelease=True),
        ]
        mock_get.return_value = _mock_response(releases)

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="stable"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.INFO_UPDATE_AVAILABLE
        assert statuses[0].status_details["latest_tag"] == "v1.1.0"

    @patch("mcup.core.utils.update_checker.update_checker.__version__", CURRENT_VERSION)
    @patch("mcup.core.utils.update_checker.update_checker.requests.get")
    def test_draft_releases_are_skipped(self, mock_get):
        """Draft releases are never surfaced as updates."""
        releases = [
            _make_release("1.1.0", NEWER, prerelease=False, draft=True),
            _make_release(CURRENT_VERSION, CURRENT, prerelease=True),
        ]
        mock_get.return_value = _mock_response(releases)

        checker = UpdateChecker()
        statuses = list(checker.check_for_update(channel="all"))

        assert len(statuses) == 1
        assert statuses[0].status_code == StatusCode.SUCCESS
