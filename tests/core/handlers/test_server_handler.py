import pytest
from unittest.mock import MagicMock, patch, mock_open
from pathlib import Path
from mcup.core.handlers.server_handler import ServerHandler
from mcup.core.utils.version import Version
from mcup.core.status import StatusCode


class TestServerHandler:

    @pytest.fixture
    def handler(self):
        with patch("mcup.core.handlers.server_handler.UserConfig"):
            return ServerHandler()

    def test_get_java_command_default(self, handler):
        """Test _get_java_command returns default 'java' when no config."""
        handler.user_config.get_configuration.return_value = []
        assert handler._get_java_command() == "java"

    def test_get_java_command_config(self, handler):
        """Test _get_java_command returns configured path."""
        mock_status = MagicMock()
        mock_status.status_code = StatusCode.SUCCESS
        mock_status.status_details = "/path/to/java"
        handler.user_config.get_configuration.return_value = [mock_status]

        assert handler._get_java_command() == "/path/to/java"

    @patch("mcup.core.handlers.server_handler.subprocess.check_output")
    def test_get_java_major_version_parsing(self, mock_check_output, handler):
        """Test parsing of different Java version strings."""

        mock_check_output.return_value = 'java version "1.8.0_211"'
        assert handler._get_java_major_version() == 8

        mock_check_output.return_value = 'openjdk version "17.0.1" 2021-10-19'
        assert handler._get_java_major_version() == 17

        mock_check_output.return_value = 'openjdk version "21" 2023-09-19'
        assert handler._get_java_major_version() == 21

        mock_check_output.return_value = 'openjdk 11.0.12 2021-07-20'
        assert handler._get_java_major_version() == 11

    def test_check_version_support(self, handler):
        """Test _check_version_support for valid and future versions."""
        from mcup.core.utils.version import LATEST_VERSION

        assert handler._check_version_support(Version(1, 16, 5)) is True

        assert handler._check_version_support(LATEST_VERSION) is True

        future_version = Version(LATEST_VERSION.major, LATEST_VERSION.minor + 1, 0)
        assert handler._check_version_support(future_version) is False

    def test_determine_server_jar_info_vanilla(self, handler):
        """Test determining valid vanilla server jar."""
        server_path = MagicMock()
        mock_file = MagicMock()
        mock_file.is_file.return_value = True
        mock_file.suffix = ".jar"
        mock_file.name = "server-1.20.1.jar"

        server_path.iterdir.return_value = [mock_file]

        jar_name, use_args = handler._determine_server_jar_info(
            server_path, "server", "installer.jar", Version(1, 20, 1)
        )
        assert jar_name == "server-1.20.1.jar"
        assert use_args is False

    def test_determine_server_jar_info_forge(self, handler):
        """Test determining forge args file instead of jar."""
        jar_name, use_args = handler._determine_server_jar_info(
            Path("/tmp"), "forge", "forge-1.19-installer.jar", Version(1, 19, 0)
        )
        assert "unix_args.txt" in jar_name or "win_args.txt" in jar_name
        assert use_args is True

    @patch("mcup.core.handlers.server_handler.requests.get")
    def test_create_server_download(self, mock_get, handler):
        """Test create flow for DOWNLOAD source."""
        server_path = Path("/tmp/test_server")
        locker_entry = {
            "source": "DOWNLOAD",
            "server_url": "https://example.com/server.jar",
            "cleanup": []
        }
        mock_assembler_config = MagicMock()
        mock_assembler_config.get_configuration_files.return_value = []

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.iter_content.return_value = [b"data"]
        mock_response.headers = {'content-length': '4'}
        mock_get.return_value = mock_response

        with patch("builtins.open", mock_open()), \
                patch("mcup.core.handlers.server_handler.os.makedirs"), \
                patch("mcup.core.handlers.server_handler.Path.exists", return_value=True):
            status_generator = handler.create(
                server_path, "paper", "1.20.1", locker_entry,
                mock_assembler_config, skip_java_check=True
            )

            statuses = list(status_generator)

            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)

            mock_get.assert_called_with("https://example.com/server.jar", stream=True)

    @patch("mcup.core.handlers.server_handler.requests.get")
    @patch("mcup.core.handlers.server_handler.subprocess.run")
    def test_create_server_installer(self, mock_run, mock_get, handler):
        """Test create flow for INSTALLER source."""
        server_path = Path("/tmp/test_forge")
        locker_entry = {
            "source": "INSTALLER",
            "installer_url": "https://example.com/installer.jar",
            "installer_args": ["java", "-jar", "%file_path", "--installServer"],
            "cleanup": []
        }
        mock_assembler_config = MagicMock()
        mock_assembler_config.get_configuration_files.return_value = []

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.iter_content.return_value = [b"data"]
        mock_get.return_value = mock_response

        with patch("builtins.open", mock_open()), \
                patch("mcup.core.handlers.server_handler.os.makedirs"), \
                patch("mcup.core.handlers.server_handler.Path.exists", return_value=True), \
                patch.object(handler, '_determine_server_jar_info', return_value=("forge-server.jar", False)):
            status_generator = handler.create(
                server_path, "forge", "1.20.1", locker_entry,
                mock_assembler_config, skip_java_check=True
            )

            statuses = list(status_generator)

            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)
            mock_run.assert_called()
