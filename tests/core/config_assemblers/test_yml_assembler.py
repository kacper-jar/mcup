import pytest
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.config_assemblers.yml_assembler import YmlAssembler
from mcup.core.configs import ConfigFile


class TestYmlAssembler:

    def test_clean_config(self):
        """Verify None, empty dicts/lists are removed recursively."""
        data = {
            "a": 1,
            "b": None,
            "c": [],
            "d": {},
            "e": {
                "f": 2,
                "g": None,
                "h": {}
            },
            "i": [1, None, {}, 2]
        }

        cleaned = YmlAssembler.clean_config(data)

        expected = {
            "a": 1,
            "e": {"f": 2},
            "i": [1, 2]
        }
        assert cleaned == expected

    def test_assemble_nested_structure(self):
        """Verify YAML generation preserves nested dictionary structure."""
        assembler = YmlAssembler()
        mock_config = MagicMock(spec=ConfigFile)
        mock_config.config_file_path = "."
        mock_config.config_file_name = "config.yml"

        mock_config.get_configuration.return_value = {
            "server": {
                "port": 25565,
                "properties": {
                    "online": True
                }
            },
            "players": ["Alice", "Bob"]
        }

        with patch("builtins.open", mock_open()) as mock_file, \
                patch("os.path.exists", return_value=True), \
                patch("yaml.dump") as mock_yaml_dump:
            assembler.assemble("/tmp", mock_config)

            mock_file.assert_called_with("/tmp/./config.yml", "w")

            args, _ = mock_yaml_dump.call_args
            dumped_data = args[0]

            assert dumped_data["server"]["port"] == 25565
            assert dumped_data["server"]["properties"]["online"] is True
            assert dumped_data["players"] == ["Alice", "Bob"]
