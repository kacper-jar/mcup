import pytest
from unittest.mock import MagicMock, patch
from mcup.cli.commands.config import ConfigCommand
from mcup.core.status import StatusCode, Status


class TestConfigCommand:

    @pytest.fixture
    def mock_args(self):
        args = MagicMock()
        args.key = "test.key"
        args.value = "test_value"
        return args

    @patch("mcup.cli.commands.config.UserConfig")
    @patch("builtins.print")
    def test_config_get_invokes_user_config(self, mock_print, MockUserConfig, mock_args):
        """Verify get command functionality."""
        mock_config = MockUserConfig.return_value

        mock_config.get_configuration.return_value = iter([Status(StatusCode.SUCCESS, "some_value")])
        ConfigCommand.get(mock_args)
        mock_config.get_configuration.assert_called_with("test.key")
        assert mock_print.called

        mock_print.reset_mock()
        mock_config.get_configuration.return_value = iter([Status(StatusCode.ERROR_USERCONFIG_KEY_NOT_FOUND)])
        ConfigCommand.get(mock_args)
        assert mock_print.called

    @patch("mcup.cli.commands.config.UserConfig")
    @patch("builtins.print")
    def test_config_set_invokes_user_config(self, mock_print, MockUserConfig, mock_args):
        """Verify set command functionality."""
        mock_config = MockUserConfig.return_value
        mock_config.set_configuration.return_value = iter([Status(StatusCode.SUCCESS)])

        ConfigCommand.set(mock_args)

        mock_config.set_configuration.assert_called_with("test.key", "test_value")
        assert mock_print.called

    @patch("mcup.cli.commands.config.UserConfig")
    @patch("builtins.print")
    def test_config_remove_invokes_user_config(self, mock_print, MockUserConfig, mock_args):
        """Verify remove command functionality."""
        mock_config = MockUserConfig.return_value
        mock_config.remove_configuration.return_value = iter([Status(StatusCode.SUCCESS)])

        ConfigCommand.remove(mock_args)

        mock_config.remove_configuration.assert_called_with("test.key")
        assert mock_print.called

    @patch("mcup.cli.commands.config.UserConfig")
    @patch("builtins.print")
    def test_config_clear_invokes_user_config(self, mock_print, MockUserConfig, mock_args):
        """Verify clear command functionality."""
        mock_config = MockUserConfig.return_value
        mock_config.clear_configuration.return_value = iter([Status(StatusCode.SUCCESS)])

        ConfigCommand.clear(mock_args)

        mock_config.clear_configuration.assert_called_once()
        assert mock_print.called

    @patch("mcup.cli.commands.config.UserConfig")
    @patch("builtins.print")
    def test_config_list_invokes_user_config(self, mock_print, MockUserConfig, mock_args):
        """Verify list command functionality."""
        mock_config = MockUserConfig.return_value
        mock_config.list_configuration.return_value = iter([Status(StatusCode.SUCCESS, {"a": 1})])

        ConfigCommand.list(mock_args)

        mock_config.list_configuration.assert_called_once()
        mock_print.assert_called_with({"a": 1})
