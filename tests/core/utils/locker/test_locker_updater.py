import pytest
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.utils.locker.locker_updater import LockerUpdater
from mcup.core.status import StatusCode


class TestLockerUpdater:

    @pytest.fixture
    def mock_deps(self):
        with patch("mcup.core.utils.locker.locker_updater.UserConfig") as MockUserConfig, \
                patch("mcup.core.utils.locker.locker_updater.PathProvider") as MockPathProvider, \
                patch("os.makedirs") as mock_makedirs:
            mock_user_config = MockUserConfig.return_value
            mock_path_provider = MockPathProvider.return_value

            from mcup.core.status import Status, StatusCode
            mock_user_config.get_configuration.side_effect = lambda key, default: iter([
                Status(StatusCode.SUCCESS, default)
            ])

            yield mock_user_config, mock_path_provider, mock_makedirs

    def test_parse_github_url(self, mock_deps):
        updater = LockerUpdater()
        owner, repo = updater._parse_github_url("https://github.com/owner/repo")
        assert owner == "owner"
        assert repo == "repo"

        owner, repo = updater._parse_github_url("https://github.com/owner/repo.git")
        assert owner == "owner"
        assert repo == "repo"

        with pytest.raises(ValueError):
            updater._parse_github_url("invalid_url")

    def test_build_urls(self, mock_deps):
        updater = LockerUpdater()
        locker, api = updater._build_urls("https://github.com/owner/repo", "main")
        assert locker == "https://raw.githubusercontent.com/owner/repo/refs/heads/main/locker.json"
        assert api == "https://api.github.com/repos/owner/repo/commits/main"

    @patch("mcup.core.utils.locker.locker_updater.requests.get")
    def test_update_locker_up_to_date(self, mock_get, mock_deps):
        """Verify INFO_LOCKER_UP_TO_DATE when timestamps match."""
        updater = LockerUpdater()

        mock_response = MagicMock()
        mock_response.json.return_value = {"commit": {"committer": {"date": "2023-01-01T00:00:00Z"}}}
        mock_get.return_value = mock_response

        with patch("builtins.open", mock_open(
                read_data='{"last_updated": "2023-01-01T00:00:00Z", "remote": "https://github.com/kacper-jar/mcup-locker-file", "branch": "main", "is_modified": false}')), \
                patch("os.path.exists", return_value=True):
            statuses = list(updater.update_locker())
            codes = [s.status_code for s in statuses]

            assert StatusCode.INFO_LOCKER_UP_TO_DATE in codes
            assert StatusCode.SUCCESS not in codes

    @patch("mcup.core.utils.locker.locker_updater.requests.get")
    def test_update_locker_force(self, mock_get, mock_deps):
        """Verify update occurs when force=True even if timestamps match."""
        updater = LockerUpdater()

        mock_response = MagicMock()
        mock_response.json.return_value = {"commit": {"committer": {"date": "2023-01-01T00:00:00Z"}}}
        mock_response.text = "{}"
        mock_get.return_value = mock_response

        with patch("builtins.open", mock_open(
                read_data='{"last_updated": "2023-01-01T00:00:00Z", "remote": "https://github.com/kacper-jar/mcup-locker-file", "branch": "main", "is_modified": false}')), \
                patch("os.path.exists", return_value=True):
            statuses = list(updater.update_locker(force_update=True))
            codes = [s.status_code for s in statuses]

            assert StatusCode.INFO_LOCKER_UPDATING in codes
            assert StatusCode.SUCCESS in codes

    @patch("mcup.core.utils.locker.locker_updater.requests.get")
    def test_update_locker_download_failure(self, mock_get, mock_deps):
        """Verify error handling on download failure."""
        updater = LockerUpdater()

        mock_response_commit = MagicMock()
        mock_response_commit.json.return_value = {"commit": {"committer": {"date": "2024-01-01T00:00:00Z"}}}

        import requests
        mock_get.side_effect = [mock_response_commit, requests.RequestException("Download failed")]

        with patch("builtins.open", mock_open(
                read_data='{"last_updated": "2023-01-01T00:00:00Z", "remote": "https://github.com/kacper-jar/mcup-locker-file", "branch": "main", "is_modified": false}')), \
                patch("os.path.exists", return_value=True):
            statuses = list(updater.update_locker())
            codes = [s.status_code for s in statuses]

            assert StatusCode.INFO_LOCKER_UPDATING in codes
            assert StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED in codes
