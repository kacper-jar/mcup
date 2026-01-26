from unittest.mock import MagicMock, patch, mock_open
from mcup.core.config_assemblers.eula_assembler import EulaAssembler


class TestEulaAssembler:

    def test_assemble(self):
        mock_config = MagicMock()
        mock_config.config_file_path = "."
        mock_config.config_file_name = "eula.txt"

        with patch("builtins.open", mock_open()) as mock_file:
            EulaAssembler.assemble("/server/path", mock_config)

            mock_file.assert_called_with("/server/path/./eula.txt", "w")

            handle = mock_file()
            args, _ = handle.write.call_args
            content = args[0]

            assert "eula=true" in content
            assert "https://aka.ms/MinecraftEULA" in content
