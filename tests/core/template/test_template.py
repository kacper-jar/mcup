import pytest
from unittest.mock import MagicMock
from mcup.core.template import Template


class TestTemplate:

    @pytest.fixture
    def mock_linker_config(self):
        config = MagicMock()
        config.to_dict.return_value = {"linker": "config"}
        return config

    def test_getters(self, mock_linker_config):
        template = Template(
            template_name="test-template",
            template_server_type="paper",
            template_server_version="1.20.4",
            template_locker_entry={"id": 1},
            template_linker_config=mock_linker_config
        )

        assert template.get_template_name() == "test-template"
        assert template.get_template_server_type() == "paper"
        assert template.get_template_server_version() == "1.20.4"
        assert template.get_template_locker_entry() == {"id": 1}
        assert template.get_template_linker_config() == mock_linker_config

    def test_get_dict(self, mock_linker_config):
        template = Template(
            template_name="test-template",
            template_server_type="paper",
            template_server_version="1.20.4",
            template_locker_entry={"id": 1},
            template_linker_config=mock_linker_config
        )

        data = template.get_dict()
        assert data["template_name"] == "test-template"
        assert data["template_server_type"] == "paper"
        assert data["template_locker_entry"] == {"id": 1}
        assert data["template_linker_config"] == {"linker": "config"}
        mock_linker_config.to_dict.assert_called_with(export_default_config=False)
