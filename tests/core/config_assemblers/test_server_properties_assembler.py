import pytest
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.config_assemblers.server_properties_assembler import ServerPropertiesAssembler
from mcup.core.configs import ServerPropertiesConfig


class TestServerPropertiesAssembler:

    def test_assemble_content(self):
        """Verify correct key=value file generation."""
        assembler = ServerPropertiesAssembler()
        mock_config = MagicMock(spec=ServerPropertiesConfig)
        mock_config.config_file_path = "."
        mock_config.config_file_name = "server.properties"

        mock_config.get_configuration.return_value = {
            "server-port": 25565,
            "motd": "Minecraft Server",
            "online-mode": True
        }

        with patch("builtins.open", mock_open()) as mock_file:
            assembler.assemble("/tmp/server", mock_config)

            mock_file.assert_called_with("/tmp/server/./server.properties", "w")
            handle = mock_file()

            handle.write.assert_any_call("server-port=25565\n")
            handle.write.assert_any_call("motd=Minecraft Server\n")
            handle.write.assert_any_call("online-mode=True\n")

    def test_assemble_ignore_none(self):
        """Verify keys with None values are skipped."""
        assembler = ServerPropertiesAssembler()
        mock_config = MagicMock(spec=ServerPropertiesConfig)
        mock_config.config_file_path = "."
        mock_config.config_file_name = "server.properties"

        mock_config.get_configuration.return_value = {
            "view-distance": 10,
            "level-seed": None,
            "max-players": 20
        }

        with patch("builtins.open", mock_open()) as mock_file:
            assembler.assemble("/tmp/server", mock_config)

            handle = mock_file()
            handle.write.assert_any_call("view-distance=10\n")
            handle.write.assert_any_call("max-players=20\n")

            for call in handle.write.call_args_list:
                args, _ = call
                assert "level-seed" not in args[0]
