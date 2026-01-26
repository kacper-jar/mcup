import pytest
from unittest.mock import MagicMock, patch, mock_open
from mcup.core.template import TemplateManager, Template


class TestTemplateManager:

    def test_save_template(self):
        mock_template = MagicMock(spec=Template)
        mock_template.get_template_name.return_value = "my_template"
        mock_template.get_dict.return_value = {"key": "value"}

        with patch("mcup.core.template.template_manager.PathProvider") as MockPathProvider, \
                patch("os.path.exists", return_value=True), \
                patch("builtins.open", mock_open()) as mock_file:
            mock_path_provider = MockPathProvider.return_value
            mock_path_provider.get_templates_path.return_value = "/templates"

            TemplateManager.save_template(mock_template)

            mock_file.assert_called_with("/templates/my_template.json", "w")

            handle = mock_file()
            handle.write.assert_called()
