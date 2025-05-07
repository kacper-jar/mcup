from mcup.core.config_assemblers.assembler_linker_config import AssemblerLinkerConfig
from mcup.core.configs.config_file import ConfigFile


def test_init():
    """Test initialization of AssemblerLinkerConfig."""
    config = AssemblerLinkerConfig()

    assert config.configuration_files == []


def test_add_configuration_file():
    """Test add_configuration_file method."""
    config = AssemblerLinkerConfig()
    config_file = ConfigFile(
        config_file_name="test.yml",
        config_file_path="/path/to/config",
        configuration={"key": "value"},
        default_configuration={"key": "default"}
    )

    config.add_configuration_file(config_file)

    assert len(config.configuration_files) == 1
    assert config.configuration_files[0] == config_file


def test_get_configuration_files():
    """Test get_configuration_files method."""
    config = AssemblerLinkerConfig()
    config_file1 = ConfigFile(config_file_name="test1.yml")
    config_file2 = ConfigFile(config_file_name="test2.yml")

    config.add_configuration_file(config_file1)
    config.add_configuration_file(config_file2)

    config_files = config.get_configuration_files()
    assert len(config_files) == 2
    assert config_files[0] == config_file1
    assert config_files[1] == config_file2


def test_get_configuration_file_count():
    """Test get_configuration_file_count method."""
    config = AssemblerLinkerConfig()

    assert config.get_configuration_file_count() == 0

    config.add_configuration_file(ConfigFile(config_file_name="test1.yml"))
    config.add_configuration_file(ConfigFile(config_file_name="test2.yml"))

    assert config.get_configuration_file_count() == 2


def test_to_dict_with_default_config():
    """Test to_dict method with export_default_config=True."""
    config = AssemblerLinkerConfig()
    config_file = ConfigFile(
        config_file_name="test.yml",
        config_file_path="/path/to/config",
        configuration={"key": "value"},
        default_configuration={"key": "default"}
    )

    config.add_configuration_file(config_file)

    config_dict = config.to_dict(export_default_config=True)

    assert "configuration_files" in config_dict
    assert len(config_dict["configuration_files"]) == 1

    file_dict = config_dict["configuration_files"][0]
    assert file_dict["config_file_name"] == "test.yml"
    assert file_dict["config_file_path"] == "/path/to/config"
    assert file_dict["configuration"] == {"key": "value"}
    assert file_dict["default_configuration"] == {"key": "default"}


def test_to_dict_without_default_config():
    """Test to_dict method with export_default_config=False."""
    config = AssemblerLinkerConfig()
    config_file = ConfigFile(
        config_file_name="test.yml",
        config_file_path="/path/to/config",
        configuration={"key": "value"},
        default_configuration={"key": "default"}
    )

    config.add_configuration_file(config_file)

    config_dict = config.to_dict(export_default_config=False)

    assert "configuration_files" in config_dict
    assert len(config_dict["configuration_files"]) == 1

    file_dict = config_dict["configuration_files"][0]
    assert file_dict["config_file_name"] == "test.yml"
    assert file_dict["config_file_path"] == "/path/to/config"
    assert file_dict["configuration"] == {"key": "value"}
    assert "default_configuration" not in file_dict


def test_from_dict():
    """Test from_dict method."""
    config_dict = {
        "configuration_files": [
            {
                "config_file_name": "test.yml",
                "config_file_path": "/path/to/config",
                "configuration": {"key": "value"},
                "default_configuration": {"key": "default"}
            }
        ]
    }

    config = AssemblerLinkerConfig()
    config.from_dict(config_dict)

    assert len(config.configuration_files) == 1
    config_file = config.configuration_files[0]
    assert config_file.config_file_name == "test.yml"
    assert config_file.config_file_path == "/path/to/config"
    assert config_file.configuration == {"key": "value"}
    assert config_file.default_configuration == {"key": "default"}


def test_from_dict_empty():
    """Test from_dict method with an empty dictionary."""
    config = AssemblerLinkerConfig()
    config.from_dict({})

    assert len(config.configuration_files) == 0


def test_from_dict_missing_fields():
    """Test from_dict method with missing fields."""
    config_dict = {
        "configuration_files": [
            {
                "config_file_name": "test.yml"
            }
        ]
    }

    config = AssemblerLinkerConfig()
    config.from_dict(config_dict)

    assert len(config.configuration_files) == 1
    config_file = config.configuration_files[0]
    assert config_file.config_file_name == "test.yml"
    assert config_file.config_file_path == ""
    assert config_file.configuration is None
    assert config_file.default_configuration is None
