import pytest
from mcup.core.configs.config_file import ConfigFile


def test_init():
    """Test initialization of ConfigFile objects."""
    config_file = ConfigFile()
    assert config_file.config_file_name == ""
    assert config_file.config_file_path == ""
    assert config_file.configuration is None
    assert config_file.default_configuration is None

    config_file = ConfigFile(
        config_file_name="test.yml",
        config_file_path="/path/to/config",
        configuration={"key": "value"},
        default_configuration={"key": "default"}
    )
    assert config_file.config_file_name == "test.yml"
    assert config_file.config_file_path == "/path/to/config"
    assert config_file.configuration == {"key": "value"}
    assert config_file.default_configuration == {"key": "default"}


def test_get_file_name():
    """Test get_file_name method."""
    config_file = ConfigFile(config_file_name="test.yml")
    assert config_file.get_file_name() == "test.yml"


def test_get_file_path():
    """Test get_file_path method."""
    config_file = ConfigFile(config_file_path="/path/to/config")
    assert config_file.get_file_path() == "/path/to/config"


def test_get_configuration():
    """Test get_configuration method."""
    config = {"key": "value"}
    config_file = ConfigFile(configuration=config)
    assert config_file.get_configuration() == config


def test_set_configuration():
    """Test set_configuration method."""
    config_file = ConfigFile()
    config = {"key": "value"}
    config_file.set_configuration(config)
    assert config_file.configuration == config


def test_set_configuration_property():
    """Test set_configuration_property method."""
    config_file = ConfigFile(configuration={})
    config_file.set_configuration_property("key", "value")
    assert config_file.configuration == {"key": "value"}

    config_file = ConfigFile(configuration={})
    config_file.set_configuration_property("parent/child", "value")
    assert config_file.configuration == {"parent": {"child": "value"}}

    config_file = ConfigFile(configuration={})
    config_file.set_configuration_property("parent/child/grandchild", "value")
    assert config_file.configuration == {"parent": {"child": {"grandchild": "value"}}}

    config_file = ConfigFile(configuration={"parent": {"existing": "old"}})
    config_file.set_configuration_property("parent/child", "value")
    assert config_file.configuration == {"parent": {"existing": "old", "child": "value"}}

    config_file = ConfigFile(
        configuration={"key": "value"},
        default_configuration={"key": "default"}
    )
    config_file.set_configuration_property("key", "")
    assert config_file.configuration == {"key": "default"}


def test_set_configuration_properties():
    """Test set_configuration_properties method."""
    config_file = ConfigFile(configuration={})
    properties = {
        "key1": "value1",
        "parent/child": "value2"
    }
    config_file.set_configuration_properties(properties)
    assert config_file.configuration == {
        "key1": "value1",
        "parent": {"child": "value2"}
    }


def test_set_configuration_default_property():
    """Test set_configuration_default_property method."""
    config_file = ConfigFile(
        configuration={"key": "value"},
        default_configuration={"key": "default"}
    )
    config_file.set_configuration_default_property("key")
    assert config_file.configuration == {"key": "default"}

    config_file = ConfigFile(
        configuration={"parent": {"child": "value"}},
        default_configuration={"parent": {"child": "default"}}
    )
    config_file.set_configuration_default_property("parent/child")
    assert config_file.configuration == {"parent": {"child": "default"}}

    config_file = ConfigFile(
        configuration={"key": "value"},
        default_configuration={}
    )
    with pytest.raises(KeyError):
        config_file.set_configuration_default_property("key")

    config_file = ConfigFile(
        configuration={"parent": {"child": "value"}},
        default_configuration={"parent": {}}
    )
    config_file.set_configuration_default_property("parent/child")
    assert config_file.configuration == {"parent": {"child": "value"}}


def test_set_configuration_default_properties():
    """Test set_configuration_default_properties method."""
    config_file = ConfigFile(
        configuration={"key1": "value1", "key2": "value2"},
        default_configuration={"key1": "default1", "key2": "default2"}
    )
    config_file.set_configuration_default_properties(["key1", "key2"])
    assert config_file.configuration == {"key1": "default1", "key2": "default2"}


def test_get_default_configuration():
    """Test get_default_configuration method."""
    default_config = {"key": "default"}
    config_file = ConfigFile(default_configuration=default_config)
    assert config_file.get_default_configuration() == default_config
