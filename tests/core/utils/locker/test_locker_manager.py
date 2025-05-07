import json
from pathlib import Path
import pytest
import requests
from mcup.core.utils.locker.locker_manager import LockerManager


"""Test cases for the LockerManager class."""


@pytest.fixture
def mock_paths():
    """Set up mock paths for testing."""
    mock_config_path = Path("/mock/config/path")
    mock_locker_path = mock_config_path / "locker.json"
    mock_meta_path = mock_config_path / "locker-meta.json"
    return mock_config_path, mock_locker_path, mock_meta_path


@pytest.fixture
def mock_path_provider(mock_paths, mocker):
    """Set up mock PathProvider."""
    mock_config_path, _, _ = mock_paths
    mock_provider = mocker.patch('mcup.core.utils.locker.locker_manager.PathProvider')
    mock_provider.return_value.get_config_path.return_value = mock_config_path
    return mock_provider


@pytest.fixture
def mock_makedirs(mocker):
    """Set up mock os.makedirs."""
    return mocker.patch('os.makedirs')


def test_init(mock_paths, mock_path_provider, mock_makedirs):
    """Test initialization of LockerManager."""
    mock_config_path, mock_locker_path, mock_meta_path = mock_paths

    manager = LockerManager()

    assert manager.locker_path == mock_locker_path
    assert manager.meta_path == mock_meta_path

    mock_makedirs.assert_called_once_with(mock_config_path, exist_ok=True)


def test_get_remote_last_update_success(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test getting remote last update timestamp (success case)."""
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "commit": {
            "committer": {
                "date": "2023-01-01T12:00:00Z"
            }
        }
    }
    mock_get = mocker.patch('requests.get', return_value=mock_response)

    manager = LockerManager()
    result = manager.get_remote_last_update()

    assert result == "2023-01-01T12:00:00Z"

    mock_get.assert_called_once_with(manager.repo_api_url, timeout=10)


def test_get_remote_last_update_failure(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test getting remote last update timestamp (failure case)."""
    mock_get = mocker.patch('requests.get', side_effect=requests.RequestException("Network error"))

    manager = LockerManager()
    result = manager.get_remote_last_update()

    assert result is None


def test_get_local_last_update_success(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test getting local last update timestamp (success case)."""
    mocker.patch('os.path.exists', return_value=True)
    mock_file = mocker.patch('builtins.open', mocker.mock_open(read_data='{"last_updated": "2023-01-01T12:00:00Z"}'))

    manager = LockerManager()
    result = manager.get_local_last_update()

    assert result == "2023-01-01T12:00:00Z"

    mock_file.assert_called_once_with(manager.meta_path, "r", encoding="utf-8")


def test_get_local_last_update_no_file(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test getting local last update timestamp when file doesn't exist."""
    mocker.patch('os.path.exists', return_value=False)

    manager = LockerManager()
    result = manager.get_local_last_update()

    assert result is None


def test_update_local_meta(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test updating local metadata."""
    mock_file = mocker.patch("builtins.open", mocker.mock_open())

    manager = LockerManager()
    manager.update_local_meta("2023-01-01T12:00:00Z")

    mock_file.assert_called_once_with(manager.meta_path, "w", encoding="utf-8")

    handle = mock_file()
    written_content = "".join(call.args[0] for call in handle.write.call_args_list)

    expected_json = json.dumps({"last_updated": "2023-01-01T12:00:00Z"}, indent=4)
    assert written_content == expected_json


def test_download_locker_file_success(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test downloading locker file (success case)."""
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.text = '{"servers": {}}'
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    mock_file = mocker.patch('builtins.open', mocker.mock_open())

    manager = LockerManager()
    result = manager.download_locker_file()

    assert result is True

    mock_get.assert_called_once_with(manager.locker_url, timeout=10)

    mock_file.assert_called_once_with(manager.locker_path, "w", encoding="utf-8")

    mock_file().write.assert_called_once_with('{"servers": {}}')


def test_download_locker_file_failure(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test downloading locker file (failure case)."""
    mocker.patch('requests.get', side_effect=requests.RequestException("Network error"))

    manager = LockerManager()
    result = manager.download_locker_file()

    assert result is False


def test_update_locker_newer_remote(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test updating locker when remote is newer."""
    mock_get_remote = mocker.patch.object(LockerManager, 'get_remote_last_update', return_value="2023-02-01T12:00:00Z")
    mock_get_local = mocker.patch.object(LockerManager, 'get_local_last_update', return_value="2023-01-01T12:00:00Z")
    mock_download = mocker.patch.object(LockerManager, 'download_locker_file', return_value=True)
    mock_update_meta = mocker.patch.object(LockerManager, 'update_local_meta')

    manager = LockerManager()
    manager.update_locker()

    mock_download.assert_called_once()

    mock_update_meta.assert_called_once_with("2023-02-01T12:00:00Z")


def test_update_locker_up_to_date(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test updating locker when it's already up to date."""
    mock_get_remote = mocker.patch.object(LockerManager, 'get_remote_last_update', return_value="2023-01-01T12:00:00Z")
    mock_get_local = mocker.patch.object(LockerManager, 'get_local_last_update', return_value="2023-01-01T12:00:00Z")
    mock_download = mocker.patch.object(LockerManager, 'download_locker_file')
    mock_update_meta = mocker.patch.object(LockerManager, 'update_local_meta')

    manager = LockerManager()
    manager.update_locker()

    mock_download.assert_not_called()

    mock_update_meta.assert_not_called()


def test_load_locker_file_exists(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test loading locker when file exists."""
    mocker.patch('os.path.exists', return_value=True)
    mock_file = mocker.patch('builtins.open', mocker.mock_open(read_data='{"servers": {"paper": {"versions": ["1.19.4"]}}}'))
    mock_update = mocker.patch.object(LockerManager, 'update_locker')

    manager = LockerManager()
    result = manager.load_locker()

    assert result == {"servers": {"paper": {"versions": ["1.19.4"]}}}

    mock_update.assert_called_once()

    mock_file.assert_called_once_with(manager.locker_path, 'r')


def test_load_locker_file_not_exists(mocker, mock_paths, mock_path_provider, mock_makedirs):
    """Test loading locker when file doesn't exist."""
    mocker.patch('os.path.exists', return_value=False)
    mock_update = mocker.patch.object(LockerManager, 'update_locker')

    manager = LockerManager()
    result = manager.load_locker()

    assert result == {"servers": {}}

    mock_update.assert_called_once()
