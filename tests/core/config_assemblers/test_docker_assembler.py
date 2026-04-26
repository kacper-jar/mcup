import pytest
import json
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.config_assemblers.docker_assembler import DockerAssembler


class TestDockerAssembler:

    @pytest.fixture
    def mock_config(self):
        config = MagicMock()
        config.configuration = {
            "java-version": "21",
            "server-jar": "server.jar",
            "server-args-instead-of-jar": False,
            "memory-initial": "1G",
            "memory-max": "2G",
            "port": "25565"
        }
        config.config_file_path = ""
        config.config_file_name = "Dockerfile"
        return config

    def test_assemble_basic(self, mock_config):
        """Test basic Dockerfile assembly."""
        with patch("builtins.open", mock_open()) as mock_file:
            DockerAssembler.assemble("/path", mock_config)

            mock_file.assert_called_with("/path//Dockerfile", "w")
            handle = mock_file()
            content = handle.write.call_args[0][0]

            assert "FROM azul/zulu-openjdk-alpine:21-jre" in content
            assert 'ENTRYPOINT ["java", "-Xms1G", "-Xmx2G", "-jar", "server.jar", "nogui"]' in content
            assert "EXPOSE 25565" in content

    def test_assemble_argument_splitting(self, mock_config):
        """Test that server-jar with spaces is correctly split into arguments."""
        mock_config.configuration["server-jar"] = "installer.jar --installServer"
        mock_config.configuration["server-args-instead-of-jar"] = True

        with patch("builtins.open", mock_open()) as mock_file:
            DockerAssembler.assemble("/path", mock_config)

            handle = mock_file()
            content = handle.write.call_args[0][0]

            assert '"installer.jar", "--installServer"' in content
            assert "-jar" not in content

    def test_assemble_forge_prefix_preservation(self, mock_config):
        """Test that the @ prefix for Forge/NeoForge is preserved."""
        mock_config.configuration["server-jar"] = "@libraries/net/minecraftforge/forge/args.txt"
        mock_config.configuration["server-args-instead-of-jar"] = True

        with patch("builtins.open", mock_open()) as mock_file:
            DockerAssembler.assemble("/path", mock_config)

            handle = mock_file()
            content = handle.write.call_args[0][0]

            assert '"@libraries/net/minecraftforge/forge/args.txt"' in content

    def test_assemble_custom_java_and_memory(self, mock_config):
        """Test custom Java version and memory settings."""
        mock_config.configuration["java-version"] = "17"
        mock_config.configuration["memory-initial"] = "512M"
        mock_config.configuration["memory-max"] = "4G"

        with patch("builtins.open", mock_open()) as mock_file:
            DockerAssembler.assemble("/path", mock_config)

            handle = mock_file()
            content = handle.write.call_args[0][0]

            assert "FROM azul/zulu-openjdk-alpine:17-jre" in content
            assert '"-Xms512M"' in content
            assert '"-Xmx4G"' in content
