import pytest
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.user_config.user_config import UserConfig
from mcup.core.status import StatusCode


class TestUserConfig:

    @pytest.fixture
    def mock_deps(self):
        with patch("mcup.core.user_config.user_config.PathProvider") as MockPathProvider, \
                patch("os.makedirs") as mock_makedirs:
            mock_path = MagicMock()
            mock_path.__truediv__.return_value = "mock/path/userconfig.json"
            MockPathProvider.return_value.get_config_path.return_value = mock_path

            yield

    def test_init_load_defaults(self, mock_deps):
        with patch("os.path.exists", return_value=False):
            config = UserConfig()
            assert config.user_config == {}

    def test_init_load_existing(self, mock_deps):
        with patch("os.path.exists", return_value=True), \
                patch("builtins.open", mock_open(read_data='{"key": "value"}')):
            config = UserConfig()
            assert config.user_config == {"key": "value"}

    def test_set_and_save(self, mock_deps):
        with patch("os.path.exists", return_value=True), \
                patch("builtins.open", mock_open(read_data='{}')) as mock_file:
            config = UserConfig()
            statuses = list(config.set_configuration("new_key", "new_value"))

            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)

            mock_file().write.assert_called()

    def test_remove(self, mock_deps):
        with patch("os.path.exists", return_value=True), \
                patch("builtins.open", mock_open(read_data='{"to_remove": "value"}')):
            config = UserConfig()
            statuses = list(config.remove_configuration("to_remove"))

            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)
            assert "to_remove" not in config.user_config

    def test_get(self, mock_deps):
        with patch("os.path.exists", return_value=False):
            config = UserConfig()
            config.user_config = {"exists": "yes"}

            statuses = list(config.get_configuration("exists"))
            assert statuses[0].status_details == "yes"

            statuses = list(config.get_configuration("missing", "default"))
            assert statuses[0].status_details == "default"

            statuses = list(config.get_configuration("missing"))
            assert statuses[0].status_code == StatusCode.ERROR_USERCONFIG_KEY_NOT_FOUND

    def test_clear(self, mock_deps):
        with patch("os.path.exists", return_value=True), \
                patch("os.remove") as mock_remove:
            config = UserConfig()
            config.user_config = {"data": 1}

            list(config.clear_configuration())

            mock_remove.assert_called()
            assert config.user_config == {}

    def test_list_configuration(self, mock_deps):
        with patch("os.path.exists", return_value=True), \
             patch("builtins.open", mock_open(read_data='{"a": 1, "b": 2}')):
            config = UserConfig()
            
            statuses = list(config.list_configuration())
            assert statuses[0].status_code == StatusCode.SUCCESS
            assert "Current configuration (2 entries):" in statuses[0].status_details
            assert "  a = 1" in statuses[0].status_details
            assert "  b = 2" in statuses[0].status_details

