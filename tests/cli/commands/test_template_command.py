import pytest
from unittest.mock import MagicMock, patch
from mcup.cli.commands.template import TemplateCommand
from mcup.core.status import StatusCode, Status


class TestTemplateCommand:

    @pytest.fixture
    def mock_args(self):
        args = MagicMock()
        args.server_type = "paper"
        args.server_version = "1.20.1"
        args.template_name = "my_tmpl"
        args.path = "/tmp/server"
        args.destination = "/tmp/export.json"

        return args

    @patch("mcup.cli.commands.template.LockerUpdater")
    @patch("mcup.cli.commands.template.TemplateHandler")
    @patch("mcup.cli.commands.template.ServerConfigsCollector")
    @patch("mcup.cli.commands.template.PathProvider")
    @patch("os.path.exists", return_value=False)
    @patch("builtins.print")
    def test_create_invokes_handler(self, mock_print, mock_exists, MockPathProvider, MockCollector, MockTemplateHandler,
                                    MockLocker, mock_args):
        """Verify mcup template create calls TemplateHandler.create_template."""

        mock_locker = MockLocker.return_value
        locker_data = {
            "servers": {
                "paper": [
                    {"version": "1.20.1", "source": "DOWNLOAD", "configs": []}
                ]
            }
        }
        mock_locker.load_locker.return_value = iter([Status(StatusCode.SUCCESS, locker_data)])

        mock_handler = MockTemplateHandler.return_value
        mock_handler.create_template.return_value = iter([Status(StatusCode.SUCCESS)])

        TemplateCommand.create(mock_args)

        mock_handler.create_template.assert_called_once()
        call_args = mock_handler.create_template.call_args
        assert call_args[0][0] == "my_tmpl"
        assert call_args[0][1] == "paper"
        assert call_args[0][2] == "1.20.1"

    @patch("mcup.cli.commands.template.TemplateHandler")
    @patch("builtins.print")
    def test_list_output(self, mock_print, MockTemplateHandler, mock_args):
        """Verify list output format."""
        mock_handler = MockTemplateHandler.return_value
        mock_handler.list_templates.return_value = iter([Status(StatusCode.SUCCESS, ["tmpl1", "tmpl2"])])

        TemplateCommand.list(mock_args)

        calls = [str(call) for call in mock_print.call_args_list]
        assert any("tmpl1" in c for c in calls)
        assert any("tmpl2" in c for c in calls)

    @patch("mcup.cli.commands.template.TemplateHandler")
    @patch("builtins.print")
    def test_import_invokes_handler(self, mock_print, MockTemplateHandler, mock_args):
        """Verify import calls handler."""
        mock_handler = MockTemplateHandler.return_value
        mock_handler.import_template.return_value = iter([Status(StatusCode.SUCCESS)])
        mock_args.path = "/tmp/import.json"

        TemplateCommand.import_template(mock_args)

        mock_handler.import_template.assert_called_with("/tmp/import.json")

    @patch("mcup.cli.commands.template.TemplateHandler")
    @patch("builtins.print")
    def test_export_invokes_handler(self, mock_print, MockTemplateHandler, mock_args):
        """Verify export calls handler."""
        mock_handler = MockTemplateHandler.return_value
        mock_handler.export_template.return_value = iter([Status(StatusCode.SUCCESS)])

        TemplateCommand.export_template(mock_args)

        mock_handler.export_template.assert_called_with("my_tmpl", "/tmp/export.json")

    @patch("mcup.cli.commands.template.TemplateHandler")
    @patch("builtins.print")
    def test_delete_invokes_handler(self, mock_print, MockTemplateHandler, mock_args):
        """Verify delete calls handler."""
        mock_handler = MockTemplateHandler.return_value
        mock_handler.delete_template.return_value = iter([Status(StatusCode.SUCCESS)])

        TemplateCommand.delete(mock_args)

        mock_handler.delete_template.assert_called_with("my_tmpl")

    @patch("mcup.cli.commands.template.TemplateHandler")
    @patch("builtins.print")
    def test_use_invokes_handler(self, mock_print, MockTemplateHandler, mock_args):
        """Verify use calls handler."""
        mock_handler = MockTemplateHandler.return_value
        mock_handler.use_template.return_value = iter([Status(StatusCode.SUCCESS)])

        TemplateCommand.use(mock_args)

        call_args = mock_handler.use_template.call_args
        assert call_args[0][0] == "my_tmpl"
        assert str(call_args[0][1]) == "/tmp/server"

    @patch("mcup.cli.commands.template.TemplateHandler")
    @patch("builtins.print")
    def test_refresh_invokes_handler(self, mock_print, MockTemplateHandler, mock_args):
        """Verify refresh calls handler."""
        mock_handler = MockTemplateHandler.return_value
        mock_handler.refresh_template.return_value = iter([Status(StatusCode.SUCCESS)])

        TemplateCommand.refresh(mock_args)

        mock_handler.refresh_template.assert_called_with("my_tmpl")
