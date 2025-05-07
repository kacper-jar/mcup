import pytest
from pathlib import Path
from mcup.core.config_assemblers.assembler_linker import AssemblerLinker
from mcup.core.config_assemblers.assembler_linker_config import AssemblerLinkerConfig
from mcup.core.configs.config_file import ConfigFile


@pytest.fixture
def mock_config():
    """Create a mock AssemblerLinkerConfig for testing."""
    config = AssemblerLinkerConfig()

    server_properties = ConfigFile(
        config_file_name="server.properties",
        config_file_path=".",
        configuration={"key": "value"},
        default_configuration={"key": "default"}
    )
    config.add_configuration_file(server_properties)

    bukkit_yml = ConfigFile(
        config_file_name="bukkit.yml",
        config_file_path=".",
        configuration={"key": "value"},
        default_configuration={"key": "default"}
    )
    config.add_configuration_file(bukkit_yml)

    return config


def test_init():
    """Test initialization of AssemblerLinker."""
    linker = AssemblerLinker()
    assert linker.configuration is None
    assert linker.linked_files == {}

    config = AssemblerLinkerConfig()
    linker = AssemblerLinker(config)
    assert linker.configuration == config
    assert linker.linked_files == {}


def test_set_configuration():
    """Test set_configuration method."""
    linker = AssemblerLinker()
    config = AssemblerLinkerConfig()

    linker.set_configuration(config)

    assert linker.configuration == config


def test_get_configuration():
    """Test get_configuration method."""
    config = AssemblerLinkerConfig()
    linker = AssemblerLinker(config)

    assert linker.get_configuration() == config


def test_add_configuration_file():
    """Test add_configuration_file method."""
    config = AssemblerLinkerConfig()
    linker = AssemblerLinker(config)

    config_file = ConfigFile(config_file_name="test.yml")
    linker.add_configuration_file(config_file)

    assert len(config.get_configuration_files()) == 1
    assert config.get_configuration_files()[0] == config_file


def test_link(mock_config, mocker):
    """Test link method."""
    mock_server_properties_assembler = mocker.patch('mcup.core.config_assemblers.ServerPropertiesAssembler')
    mock_yml_assembler = mocker.patch('mcup.core.config_assemblers.YmlAssembler')

    linker = AssemblerLinker(mock_config)

    mocker.patch('builtins.print')

    linker.link()

    assert len(linker.linked_files) == 2
    assert "server.properties" in linker.linked_files
    assert "bukkit.yml" in linker.linked_files

    mock_server_properties_assembler.assert_called_once()
    mock_yml_assembler.assert_called_once()


def test_get_linked_files(mock_config, mocker):
    """Test get_linked_files method."""

    linker = AssemblerLinker(mock_config)

    mocker.patch('builtins.print')

    linker.link()

    linked_files = linker.get_linked_files()

    assert len(linked_files) == 2
    assert "server.properties" in linked_files
    assert "bukkit.yml" in linked_files


def test_get_linked_file_count(mock_config, mocker):
    """Test get_linked_file_count method."""

    linker = AssemblerLinker(mock_config)

    mocker.patch('builtins.print')

    assert linker.get_linked_file_count() == 0

    linker.link()

    assert linker.get_linked_file_count() == 2


def test_drop_linked_files(mock_config, mocker):
    """Test drop_linked_files method."""

    linker = AssemblerLinker(mock_config)

    mocker.patch('builtins.print')

    linker.link()

    assert linker.get_linked_file_count() == 2

    linker.drop_linked_files()

    assert linker.get_linked_file_count() == 0
    assert linker.linked_files == {}


def test_assemble_linked_files(mock_config, mocker):
    """Test assemble_linked_files method."""
    mock_server_properties_assembler = mocker.Mock()
    mock_yml_assembler = mocker.Mock()

    linker = AssemblerLinker(mock_config)

    linker.linked_files = {
        "server.properties": mock_server_properties_assembler,
        "bukkit.yml": mock_yml_assembler
    }

    path = Path("/path/to/server")
    linker.assemble_linked_files(path)

    mock_server_properties_assembler.assemble.assert_called_once()
    mock_yml_assembler.assemble.assert_called_once()

    assert mock_server_properties_assembler.assemble.call_args[0][0] == path
    assert mock_yml_assembler.assemble.call_args[0][0] == path

    server_properties_file = mock_server_properties_assembler.assemble.call_args[0][1]
    assert server_properties_file.config_file_name == "server.properties"

    bukkit_yml_file = mock_yml_assembler.assemble.call_args[0][1]
    assert bukkit_yml_file.config_file_name == "bukkit.yml"
