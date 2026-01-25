import pytest
from unittest.mock import MagicMock, patch
from mcup.cli.commands.server import ServerCommand
from mcup.core.status import StatusCode, Status


class TestServerCommand:

    @pytest.fixture
    def mock_args(self):
        args = MagicMock()
        args.server_type = "paper"
        args.server_version = "1.20.1"
        args.path = "/tmp/server"
        args.no_configs = False
        args.no_defaults = False
        args.all_defaults = False
        args.skip_java_check = True
        return args

    @patch("mcup.cli.commands.server.LockerUpdater")
    @patch("mcup.cli.commands.server.ServerHandler")
    @patch("mcup.cli.commands.server.ServerConfigsCollector")
    @patch("builtins.print")
    def test_server_create_invokes_handler(self, mock_print, mock_collector, MockServerHandler, MockLocker, mock_args):
        """Verify mcup server create calls ServerHandler.create."""

        mock_locker = MockLocker.return_value
        locker_data = {
            "servers": {
                "paper": [
                    {"version": "1.20.1", "source": "DOWNLOAD", "configs": []}
                ]
            }
        }
        mock_locker.load_locker.return_value = iter([Status(StatusCode.SUCCESS, locker_data)])

        mock_handler = MockServerHandler.return_value
        mock_handler.create.return_value = iter([Status(StatusCode.SUCCESS)])

        ServerCommand.create(mock_args)

        mock_handler.create.assert_called_once()
        call_args = mock_handler.create.call_args
        from pathlib import Path
        expected_path = str(Path("/tmp/server").resolve())
        assert str(call_args[0][0]) == expected_path
        assert call_args[0][1] == "paper"
        assert call_args[0][2] == "1.20.1"
        assert call_args[1]['skip_java_check'] is True

    @patch("mcup.cli.commands.server.LockerUpdater")
    @patch("builtins.print")
    def test_server_create_invalid_version_error(self, mock_print, MockLocker, mock_args):
        """Verify error handling for invalid versions."""
        mock_locker = MockLocker.return_value
        locker_data = {
            "servers": {
                "paper": []
            }
        }
        mock_locker.load_locker.return_value = iter([Status(StatusCode.SUCCESS, locker_data)])

        ServerCommand.create(mock_args)

        assert mock_print.called

    @patch("mcup.cli.commands.server.LockerUpdater")
    @patch("builtins.print")
    def test_server_list_output(self, mock_print, MockLocker, mock_args):
        """Verify list command output format."""
        mock_locker = MockLocker.return_value
        locker_data = {
            "servers": {
                "paper": [{"version": "1.20.1"}, {"version": "1.19.4"}],
                "forge": [{"version": "3.2.0"}]
            }
        }
        mock_locker.load_locker.return_value = iter([Status(StatusCode.SUCCESS, locker_data)])

        ServerCommand.list(mock_args)

        calls = [str(call) for call in mock_print.call_args_list]
        assert any("paper:" in c for c in calls)
        assert any("1.20.1, 1.19.4" in c for c in calls)
        assert any("forge:" in c for c in calls)
