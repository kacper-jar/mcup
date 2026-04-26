import pytest
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.config_assemblers.docker_compose_assembler import DockerComposeAssembler


class TestDockerComposeAssembler:

    @pytest.fixture
    def mock_config(self):
        config = MagicMock()
        config.configuration = {
            "service-name": "minecraft-server",
            "container-name": "minecraft-server",
            "port": "25565",
            "uid": 1000,
            "gid": 1000
        }
        config.config_file_path = ""
        config.config_file_name = "docker-compose.yml"
        return config

    def test_assemble_basic(self, mock_config):
        """Test basic docker-compose.yml assembly."""
        with patch("builtins.open", mock_open()) as mock_file:
            DockerComposeAssembler.assemble("/path", mock_config)

            mock_file.assert_called_with("/path//docker-compose.yml", "w")
            handle = mock_file()
            content = handle.write.call_args[0][0]

            assert "services:" in content
            assert "minecraft-server:" in content
            assert 'container_name: minecraft-server' in content
            assert 'user: "1000:1000"' in content
            assert '- "25565:25565"' in content
            assert "volumes:" in content
            assert "- .:/app" in content

    def test_assemble_custom_values(self, mock_config):
        """Test assembly with custom service name, port, and UID/GID."""
        mock_config.configuration["service-name"] = "my-mc"
        mock_config.configuration["container-name"] = "survival-server"
        mock_config.configuration["port"] = "25570"
        mock_config.configuration["uid"] = 501
        mock_config.configuration["gid"] = 20

        with patch("builtins.open", mock_open()) as mock_file:
            DockerComposeAssembler.assemble("/path", mock_config)

            handle = mock_file()
            content = handle.write.call_args[0][0]

            assert "my-mc:" in content
            assert "container_name: survival-server" in content
            assert 'user: "501:20"' in content
            assert '- "25570:25570"' in content
