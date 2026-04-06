import json
import time
from unittest.mock import MagicMock, patch
import pytest

from mcup.__main__ import _run_update_check
from mcup.core.status import Status, StatusCode


@pytest.fixture
def mock_user_config():
    config = MagicMock()
    config.get_configuration.side_effect = lambda key, default: [Status(StatusCode.SUCCESS, default)]
    return config


@pytest.fixture
def mock_path_provider(tmp_path):
    provider = MagicMock()
    provider.get_config_path.return_value = tmp_path
    return provider


@pytest.fixture
def mock_update_checker():
    with patch("mcup.__main__.UpdateChecker") as mock:
        checker_instance = mock.return_value
        checker_instance.check_for_update.return_value = []
        yield checker_instance


class TestUpdateCheckTimeout:
    """Tests for the update check timeout mechanism in mcup.__main__."""

    def test_run_update_check_skips_when_enabled_is_false(self, mock_user_config, mock_update_checker):
        """Should skip the check entirely if updates.check is set to 'false'."""
        mock_user_config.get_configuration.side_effect = lambda key, default: [
            Status(StatusCode.SUCCESS, "false") if key == "updates.check" else Status(StatusCode.SUCCESS, default)
        ]

        _run_update_check(mock_user_config)

        mock_update_checker.check_for_update.assert_not_called()

    @patch("mcup.__main__.PathProvider")
    def test_run_update_check_performs_check_when_no_state_exists(
            self, mock_path_provider_class, mock_user_config, mock_path_provider, mock_update_checker
    ):
        """Should perform check and create updates.json if it doesn't exist."""
        mock_path_provider_class.return_value = mock_path_provider

        _run_update_check(mock_user_config)

        mock_update_checker.check_for_update.assert_called_once()
        updates_file = mock_path_provider.get_config_path() / "updates.json"
        assert updates_file.exists()

    @patch("mcup.__main__.PathProvider")
    def test_run_update_check_skips_within_timeout(
            self, mock_path_provider_class, mock_user_config, mock_path_provider, mock_update_checker
    ):
        """Should skip the check if the time elapsed is less than the timeout."""
        mock_path_provider_class.return_value = mock_path_provider
        config_dir = mock_path_provider.get_config_path()
        updates_file = config_dir / "updates.json"

        last_checked = time.time() - 10
        with open(updates_file, "w") as f:
            json.dump({"last_checked": last_checked}, f)

        mock_user_config.get_configuration.side_effect = lambda key, default: [
            Status(StatusCode.SUCCESS, 100) if key == "updates.check_timeout" else Status(StatusCode.SUCCESS, default)
        ]

        _run_update_check(mock_user_config)

        mock_update_checker.check_for_update.assert_not_called()

    @patch("mcup.__main__.PathProvider")
    def test_run_update_check_performs_after_timeout(
            self, mock_path_provider_class, mock_user_config, mock_path_provider, mock_update_checker
    ):
        """Should perform check if the time elapsed is greater than or equal to the timeout."""
        mock_path_provider_class.return_value = mock_path_provider
        config_dir = mock_path_provider.get_config_path()
        updates_file = config_dir / "updates.json"

        last_checked = time.time() - 200
        with open(updates_file, "w") as f:
            json.dump({"last_checked": last_checked}, f)

        mock_user_config.get_configuration.side_effect = lambda key, default: [
            Status(StatusCode.SUCCESS, 100) if key == "updates.check_timeout" else Status(StatusCode.SUCCESS, default)
        ]

        _run_update_check(mock_user_config)

        mock_update_checker.check_for_update.assert_called_once()

        with open(updates_file, "r") as f:
            data = json.load(f)
            assert data["last_checked"] > last_checked
