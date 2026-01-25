import pytest
from unittest.mock import MagicMock, patch
from mcup.cli.commands.update import UpdateCommand
from mcup.core.status import StatusCode, Status


class TestUpdateCommand:

    @pytest.fixture
    def mock_args(self):
        args = MagicMock()
        args.force = False
        return args

    @patch("mcup.cli.commands.update.LockerUpdater")
    @patch("builtins.print")
    def test_update_invokes_locker_updater(self, mock_print, MockLockerUpdater, mock_args):
        """Verify LockerUpdater.update_locker called with correct args."""
        mock_locker = MockLockerUpdater.return_value
        mock_locker.update_locker.return_value = iter([Status(StatusCode.SUCCESS)])

        UpdateCommand.run(mock_args)

        MockLockerUpdater.assert_called_once()

        mock_locker.update_locker.assert_called_with(False)

        mock_args.force = True
        UpdateCommand.run(mock_args)
        mock_locker.update_locker.assert_called_with(True)

    @patch("mcup.cli.commands.update.LockerUpdater")
    @patch("builtins.print")
    def test_update_success_output(self, mock_print, MockLockerUpdater, mock_args):
        """Verify successful update output."""
        mock_locker = MockLockerUpdater.return_value
        mock_locker.update_locker.return_value = iter([
            Status(StatusCode.INFO_LOCKER_UPDATING),
            Status(StatusCode.SUCCESS)
        ])

        UpdateCommand.run(mock_args)

        assert mock_print.call_count >= 2

    @patch("mcup.cli.commands.update.LockerUpdater")
    @patch("builtins.print")
    def test_update_error_handling(self, mock_print, MockLockerUpdater, mock_args):
        """Verify error message printing for various error codes."""
        mock_locker = MockLockerUpdater.return_value

        mock_locker.update_locker.return_value = iter([
            Status(StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED, "Network Error")
        ])

        UpdateCommand.run(mock_args)
        assert mock_print.called

        mock_print.reset_mock()

        mock_locker.update_locker.return_value = iter([
            Status(StatusCode.ERROR_LOCKER_META_UPDATE_FAILED, "Permission Denied")
        ])
        UpdateCommand.run(mock_args)
        assert mock_print.called
