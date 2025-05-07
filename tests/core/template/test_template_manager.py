import pytest
from pathlib import Path
from mcup.core.template.template import Template
from mcup.core.template.template_manager import TemplateManager
from mcup.core.config_assemblers.assembler_linker_config import AssemblerLinkerConfig


@pytest.fixture
def mock_template():
    """Create a mock Template for testing."""
    linker_config = AssemblerLinkerConfig()
    
    return Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=linker_config
    )


@pytest.fixture
def mock_path_provider(mocker):
    """Set up mock PathProvider."""
    mock_templates_path = Path("/mock/templates/path")
    mock_provider = mocker.patch('mcup.core.template.template_manager.PathProvider')
    mock_provider.return_value.get_templates_path.return_value = mock_templates_path
    return mock_provider, mock_templates_path


def test_save_template_directory_exists(mock_template, mock_path_provider, mocker):
    """Test saving template when templates directory exists."""
    mock_provider, mock_templates_path = mock_path_provider

    mocker.patch('os.path.exists', return_value=True)
    mock_makedirs = mocker.patch('os.makedirs')
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    mock_json_dump = mocker.patch('json.dump')
    mock_print = mocker.patch('builtins.print')

    TemplateManager.save_template(mock_template)

    mock_makedirs.assert_not_called()

    expected_path = f"{mock_templates_path}/{mock_template.get_template_name()}.json"
    mock_open.assert_called_once_with(expected_path, 'w')

    mock_json_dump.assert_called_once_with(
        mock_template.get_dict(),
        mock_open.return_value.__enter__.return_value,
        indent=4
    )

    mock_print.assert_called_once_with(f"Template '{mock_template.get_template_name()}' saved successfully.")


def test_save_template_directory_not_exists(mock_template, mock_path_provider, mocker):
    """Test saving template when templates directory doesn't exist."""
    mock_provider, mock_templates_path = mock_path_provider

    mocker.patch('os.path.exists', return_value=False)
    mock_makedirs = mocker.patch('os.makedirs')
    mock_open = mocker.patch('builtins.open', mocker.mock_open())
    mock_json_dump = mocker.patch('json.dump')
    mock_print = mocker.patch('builtins.print')

    TemplateManager.save_template(mock_template)

    mock_makedirs.assert_called_once_with(mock_templates_path)

    expected_path = f"{mock_templates_path}/{mock_template.get_template_name()}.json"
    mock_open.assert_called_once_with(expected_path, 'w')

    mock_json_dump.assert_called_once_with(
        mock_template.get_dict(),
        mock_open.return_value.__enter__.return_value,
        indent=4
    )

    mock_print.assert_called_once_with(f"Template '{mock_template.get_template_name()}' saved successfully.")
