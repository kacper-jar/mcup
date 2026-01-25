import json
import pytest
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.handlers.template_handler import TemplateHandler
from mcup.core.status import StatusCode, Status
from mcup.core.config_assemblers import AssemblerLinkerConfig


class TestTemplateHandler:

    @pytest.fixture
    def handler(self):
        with patch("mcup.core.handlers.template_handler.PathProvider") as MockPathProvider:
            mock_provider = MockPathProvider.return_value
            mock_provider.get_templates_path.return_value = "/tmp/templates"
            return TemplateHandler()

    def test_create_template_object(self, handler):
        """Verify Template object creation and serialization (via mock)."""
        locker_entry = {"source": "DOWNLOAD"}
        linker_conf = MagicMock(spec=AssemblerLinkerConfig)

        with patch("mcup.core.handlers.template_handler.Template") as MockTemplate, \
                patch("mcup.core.handlers.template_handler.TemplateManager.save_template") as mock_save:
            status_gen = handler.create_template(
                "my_template", "paper", "1.20.1", locker_entry, linker_conf
            )
            statuses = list(status_gen)

            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)
            MockTemplate.assert_called_with(
                "my_template", "paper", "1.20.1", locker_entry, linker_conf
            )
            mock_save.assert_called()

    def test_validate_template_data_valid(self, handler):
        """Test _validate_template_data with complete data."""
        data = {
            "template_name": "test",
            "template_server_type": "paper",
            "template_server_version": "1.20",
            "template_locker_entry": {"valid": True},
            "template_linker_config": {"valid": True}
        }
        assert handler._validate_template_data(data, "path") is None

    def test_validate_template_data_missing_fields(self, handler):
        """Test _validate_template_data fails with missing fields."""
        data = {
            "template_name": "test",
        }
        status = handler._validate_template_data(data, "path")
        assert status is not None
        assert status.status_code == StatusCode.ERROR_TEMPLATE_MISSING_DATA

    def test_import_template_invalid_json(self, handler):
        """Verify error handling for malformed JSON imports."""
        with patch("builtins.open", mock_open(read_data="{invalid_json")), \
                patch("os.path.exists", return_value=True):
            status_gen = handler.import_template("/path/to/bad.json")
            statuses = list(status_gen)

            assert any(s.status_code == StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT for s in statuses)

    def test_save_and_load_template(self, handler):
        """Simulate saving (create) and loading (use) flow using mocks."""
        locker_entry = {"source": "DOWNLOAD", "server_url": "http://test"}
        linker_conf = MagicMock(spec=AssemblerLinkerConfig)
        linker_conf.to_dict.return_value = {}

        template_data = {
            "template_name": "saved_template",
            "template_server_type": "paper",
            "template_server_version": "1.20.1",
            "template_locker_entry": locker_entry,
            "template_linker_config": {"valid": True}
        }

        with patch("builtins.open", mock_open(read_data=json.dumps(template_data))), \
                patch("os.path.exists", return_value=True), \
                patch("mcup.core.handlers.template_handler.TemplateManager.save_template") as mock_save:
            list(handler.import_template("/path/to/template.json"))

            mock_save.assert_called()
            args = mock_save.call_args[0]
            saved_template = args[0]
            assert saved_template.template_name == "saved_template"
            assert saved_template.template_server_type == "paper"

    @patch("mcup.core.handlers.template_handler.ServerHandler")
    def test_use_template_to_create_server(self, MockServerHandler, handler):
        """Mock ServerHandler.create and verify use_template passes correct arguments."""

        template_data = json.dumps({
            "template_name": "my_template",
            "template_server_type": "paper",
            "template_server_version": "1.20.1",
            "template_locker_entry": {"source": "DOWNLOAD"},
            "template_linker_config": {"valid": True}
        })

        mock_server = MockServerHandler.return_value
        mock_server.create.return_value = iter([Status(StatusCode.SUCCESS)])

        with patch("builtins.open", mock_open(read_data=template_data)), \
                patch("os.path.exists", return_value=True):
            status_gen = handler.use_template("my_template", "/tmp/server")
            list(status_gen)

            mock_server.create.assert_called_once()
            args = mock_server.create.call_args
            assert args[0][0] == "/tmp/server"
            assert args[0][1] == "paper"
            assert args[0][2] == "1.20.1"

    def test_refresh_template_failure(self, handler):
        """Test refresh template handles locker failure without crashing."""
        mock_status = MagicMock()
        mock_status.status_code = StatusCode.ERROR_GENERIC

        with patch("mcup.core.handlers.template_handler.LockerUpdater") as MockLocker, \
                patch("os.path.exists", return_value=True):
            mock_locker_instance = MockLocker.return_value
            mock_locker_instance.load_locker.return_value = iter([mock_status])

            status_gen = handler.refresh_template("my_template")
            statuses = list(status_gen)

            assert len(statuses) > 0
            for s in statuses:
                assert s is not None
                assert hasattr(s, 'status_code')

    def test_export_template(self, handler):
        """Test export template to file."""
        template_name = "my_template"
        destination = "/tmp/exported.json"

        template_data = {"template_name": "my_template"}

        with patch.object(handler, '_get_template_path', return_value="/templates/my_template.json"), \
                patch("os.path.exists", return_value=True), \
                patch.object(handler, '_read_template_file', return_value=template_data), \
                patch.object(handler, '_ensure_destination_directory'), \
                patch.object(handler, '_write_template_file') as mock_write:
            status_gen = handler.export_template(template_name, destination)
            statuses = list(status_gen)

            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)
            mock_write.assert_called_with(destination, template_data)

    def test_delete_template(self, handler):
        """Test delete template."""
        with patch.object(handler, '_get_template_path', return_value="/templates/del.json"), \
                patch("os.path.exists", return_value=True), \
                patch("os.remove") as mock_remove:
            status_gen = handler.delete_template("del_template")
            statuses = list(status_gen)

            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)
            mock_remove.assert_called_with("/templates/del.json")

    def test_list_templates(self, handler):
        """Test listing templates."""
        with patch("os.listdir", return_value=["t1.json", "t2.json", "other.txt"]):
            status_gen = handler.list_templates()
            statuses = list(status_gen)

            success_status = next(s for s in statuses if s.status_code == StatusCode.SUCCESS)
            assert "t1" in success_status.status_details
            assert "t2" in success_status.status_details
            assert "other" not in success_status.status_details

    def test_refresh_template_success(self, handler):
        """Test successful template refresh."""
        template_name = "refresh_me"

        locker_server_entry = {
            "version": "1.20.1",
            "url": "http://new.url"
        }
        locker_data = {
            "servers": {
                "paper": [locker_server_entry]
            }
        }

        template_data = {
            "template_name": template_name,
            "template_server_type": "paper",
            "template_server_version": "1.20.1",
            "template_linker_config": {"valid": True},
            "template_locker_entry": {"old": "entry"}
        }

        def mock_load_locker_gen():
            if False: yield
            return locker_data

        with patch.object(handler, '_get_template_path', return_value="/path/to/template.json"), \
                patch("os.path.exists", return_value=True), \
                patch.object(handler, '_load_locker_data', side_effect=mock_load_locker_gen), \
                patch.object(handler, '_read_template_file', return_value=template_data), \
                patch.object(handler, '_validate_template_data_for_refresh', return_value=None), \
                patch("mcup.core.handlers.template_handler.TemplateManager.save_template") as mock_save:
            status_gen = handler.refresh_template(template_name)
            statuses = list(status_gen)

            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)

            mock_save.assert_called()
            saved_tmpl = mock_save.call_args[0][0]
            assert saved_tmpl.template_locker_entry == locker_server_entry
