import pytest
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.config_assemblers.bash_start_script_assembler import BashStartScriptAssembler


class TestBashStartScriptAssembler:

    @pytest.fixture
    def mock_config(self):
        config = MagicMock()
        config.configuration = {
            'initial-heap': 1024,
            'max-heap': 2048,
            'server-args-instead-of-jar': False,
            'use-aikars-flags': False,
            'server-jar': 'server.jar',
            'screen-name': 'mc-server',
            'max-restarts': 3,
            'restart-delay': 5
        }
        config.config_file_path = "."
        config.config_file_name = "start.sh"
        return config

    def test_assemble_basic(self, mock_config):
        with patch("builtins.open", mock_open()) as mock_file:
            BashStartScriptAssembler.assemble("/path", mock_config)

            mock_file.assert_called_with("/path/./start.sh", "w")
            handle = mock_file()

            args, _ = handle.write.call_args
            content = args[0]
            assert "java -Xms1024M -Xmx2048M -jar server.jar nogui" in content
            assert "#!/usr/bin/env sh" in content

    def test_assemble_aikars(self, mock_config):
        mock_config.configuration['use-aikars-flags'] = True

        with patch("builtins.open", mock_open()) as mock_file:
            BashStartScriptAssembler.assemble("/path", mock_config)

            handle = mock_file()
            args, _ = handle.write.call_args
            content = args[0]

            assert "-XX:+UseG1GC" in content
            assert "-Daikars.new.flags=true" in content

    def test_assemble_server_args(self, mock_config):
        mock_config.configuration['server-args-instead-of-jar'] = True

        with patch("builtins.open", mock_open()) as mock_file:
            BashStartScriptAssembler.assemble("/path", mock_config)

            handle = mock_file()
            args, _ = handle.write.call_args
            content = args[0]

            assert "-jar" not in content
            assert "java -Xms1024M -Xmx2048M  server.jar nogui" in content
