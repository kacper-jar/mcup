import pytest
from unittest.mock import MagicMock, patch, mock_open
from pathlib import Path
from mcup.core.handlers.server_handler import ServerHandler
from mcup.core.configs import ServerPropertiesConfig, StartScript, DockerFile, DockerComposeFile
from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.utils.version import Version
from mcup.core.status import Status, StatusCode


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

    @patch("mcup.core.handlers.server_handler.ServerHandler._get_java_major_version")
    def test_validate_java_version_logic(self, mock_get_java_version, handler):
        """Verify Java version validation matrix."""

        cases = [
            (Version(26, 1, 0), 25, None, True),
            (Version(26, 1, 0), 24, StatusCode.INFO_JAVA_MINIMUM_25, False),

            (Version(1, 20, 6), 21, None, True),
            (Version(1, 20, 6), 17, StatusCode.INFO_JAVA_MINIMUM_21, False),
            (Version(1, 21), 21, None, True),

            (Version(1, 18), 17, None, True),
            (Version(1, 18), 16, StatusCode.INFO_JAVA_MINIMUM_17, False),

            (Version(1, 17), 16, None, True),
            (Version(1, 17), 11, StatusCode.INFO_JAVA_MINIMUM_16, False),

            (Version(1, 16, 5), 8, None, True),
            (Version(1, 12, 2), 8, None, True),
            (Version(1, 12, 2), 7, StatusCode.INFO_JAVA_MINIMUM_8, False),
        ]

        for mc_ver, java_ver, expected_code, expect_none in cases:
            mock_get_java_version.return_value = java_ver

            gen = handler._validate_java_version_for_minecraft(mc_ver)

            next(gen)

            try:
                next(gen)
                assert False, f"Should have returned via StopIteration for {mc_ver} / Java {java_ver}"
            except StopIteration as e:
                returned_status = e.value
                if expect_none:
                    assert returned_status is None, f"Expected None for {mc_ver} / Java {java_ver}, got {returned_status}"
                else:
                    assert returned_status is not None
                    assert returned_status.status_code == expected_code, \
                        f"Expected {expected_code} for {mc_ver} / Java {java_ver}, got {returned_status.status_code}"

    def test_assemble_configuration_files_docker_port_sync(self, handler):
        """Verify that Docker port is synced from ServerPropertiesConfig."""
        server_path = Path("/tmp/server")
        version = Version(1, 20, 1)

        properties = ServerPropertiesConfig()
        properties.configuration["server-port"] = "25570"

        config_files = [properties]
        mock_linker_config = MagicMock(spec=AssemblerLinkerConfig)
        mock_linker_config.get_configuration_files.return_value = config_files

        with patch("mcup.core.handlers.server_handler.AssemblerLinker") as MockLinker:
            list(handler._assemble_configuration_files(
                server_path, version, "server.jar", False, mock_linker_config, create_docker_container=True
            ))

            docker_file = next(c for c in config_files if isinstance(c, DockerFile))
            docker_compose = next(c for c in config_files if isinstance(c, DockerComposeFile))

            assert docker_file.configuration["port"] == "25570"
            assert docker_compose.configuration["port"] == "25570"

    def test_assemble_configuration_files_docker_memory_sync(self, handler):
        """Verify that Docker memory is synced from StartScript."""
        server_path = Path("/tmp/server")
        version = Version(1, 20, 1)

        start_script = StartScript()
        start_script.configuration["initial-heap"] = 4096
        start_script.configuration["max-heap"] = 8192

        config_files = [start_script]
        mock_linker_config = MagicMock(spec=AssemblerLinkerConfig)
        mock_linker_config.get_configuration_files.return_value = config_files

        with patch("mcup.core.handlers.server_handler.AssemblerLinker"):
            list(handler._assemble_configuration_files(
                server_path, version, "server.jar", False, mock_linker_config, create_docker_container=True
            ))

            docker_file = next(c for c in config_files if isinstance(c, DockerFile))
            assert docker_file.configuration["memory-initial"] == "4096M"
            assert docker_file.configuration["memory-max"] == "8192M"

    @patch("mcup.core.handlers.server_handler.os.getuid", return_value=501)
    @patch("mcup.core.handlers.server_handler.os.getgid", return_value=20)
    def test_assemble_configuration_files_docker_user_mapping(self, mock_getgid, mock_getuid, handler):
        """Verify that Docker UID/GID are correctly detected and applied."""
        server_path = Path("/tmp/server")
        version = Version(1, 20, 1)

        config_files = []
        mock_linker_config = MagicMock(spec=AssemblerLinkerConfig)
        mock_linker_config.get_configuration_files.return_value = config_files

        with patch("mcup.core.handlers.server_handler.sys.platform", "linux"), \
                patch("mcup.core.handlers.server_handler.AssemblerLinker"):
            list(handler._assemble_configuration_files(
                server_path, version, "server.jar", False, mock_linker_config, create_docker_container=True
            ))

            docker_compose = next(c for c in config_files if isinstance(c, DockerComposeFile))
            assert docker_compose.configuration["uid"] == 501
            assert docker_compose.configuration["gid"] == 20

    def test_assemble_configuration_files_docker_user_mapping_windows_skipped(self, handler):
        """Verify that Docker UID/GID mapping is skipped on Windows."""
        server_path = Path("/tmp/server")
        version = Version(1, 20, 1)

        config_files = []
        mock_linker_config = MagicMock(spec=AssemblerLinkerConfig)
        mock_linker_config.get_configuration_files.return_value = config_files

        with patch("mcup.core.handlers.server_handler.sys.platform", "win32"), \
                patch("mcup.core.handlers.server_handler.AssemblerLinker"):
            list(handler._assemble_configuration_files(
                server_path, version, "server.jar", False, mock_linker_config, create_docker_container=True
            ))

            docker_compose = next(c for c in config_files if isinstance(c, DockerComposeFile))
            assert docker_compose.configuration["uid"] == 1000
            assert docker_compose.configuration["gid"] == 1000

    def test_assemble_configuration_files_docker_fallbacks(self, handler):
        """Verify that Docker logic handles missing configs gracefully with defaults."""
        server_path = Path("/tmp/server")
        version = Version(1, 20, 1)

        config_files = []
        mock_linker_config = MagicMock(spec=AssemblerLinkerConfig)
        mock_linker_config.get_configuration_files.return_value = config_files

        with patch("mcup.core.handlers.server_handler.AssemblerLinker"):
            list(handler._assemble_configuration_files(
                server_path, version, "server.jar", False, mock_linker_config, create_docker_container=True
            ))

            docker_file = next(c for c in config_files if isinstance(c, DockerFile))
            assert docker_file.configuration["port"] == "25565"
            assert docker_file.configuration["memory-initial"] == "1024M"
            assert docker_file.configuration["memory-max"] == "1024M"

    @patch("mcup.core.handlers.server_handler.requests.get")
    def test_create_server_docker_download(self, mock_get, handler):
        """Test full create flow with Docker enabled for DOWNLOAD source."""
        server_path = Path("/tmp/test_docker_server")
        locker_entry = {
            "source": "DOWNLOAD",
            "server_url": "https://example.com/server.jar",
            "cleanup": []
        }
        mock_assembler_config = MagicMock(spec=AssemblerLinkerConfig)
        mock_assembler_config.get_configuration_files.return_value = []

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.iter_content.return_value = [b"data"]
        mock_response.headers = {'content-length': '4'}
        mock_get.return_value = mock_response

        with patch("builtins.open", mock_open()), \
                patch("mcup.core.handlers.server_handler.os.makedirs"), \
                patch("mcup.core.handlers.server_handler.Path.exists", return_value=True), \
                patch("mcup.core.handlers.server_handler.AssemblerLinker") as MockLinker:
            status_generator = handler.create(
                server_path, "paper", "1.20.1", locker_entry,
                mock_assembler_config, skip_java_check=True, create_docker_container=True
            )

            statuses = list(status_generator)
            assert any(s.status_code == StatusCode.SUCCESS for s in statuses)

            added_configs = mock_assembler_config.get_configuration_files.return_value
            assert any(isinstance(c, DockerFile) for c in added_configs)
            assert any(isinstance(c, DockerComposeFile) for c in added_configs)
