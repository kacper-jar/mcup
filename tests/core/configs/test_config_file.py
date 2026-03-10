from mcup.core.configs.config_file import ConfigFile
from mcup.core.utils.version import Version, VersionDependantVariable, VersionDependantVariablePicker


class TestConfigFile:

    def test_set_nested_property(self):
        config = ConfigFile()
        config.configuration = {}

        config.set_configuration_property("a/b/c", "value", Version(1, 20))

        assert config.configuration["a"]["b"]["c"] == "value"

    def test_restore_defaults_simple(self):
        config = ConfigFile()
        config.configuration = {"key": "old"}
        config.default_configuration = {"key": "default"}

        config.set_configuration_default_property("key", Version(1, 20))
        assert config.configuration["key"] == "default"

    def test_restore_defaults_nested(self):
        config = ConfigFile()
        config.configuration = {"a": {"b": "old"}}
        config.default_configuration = {"a": {"b": "default"}}

        config.set_configuration_default_property("a/b", Version(1, 20))
        assert config.configuration["a"]["b"] == "default"

    def test_version_dependant_resolution(self):
        config = ConfigFile()
        config.configuration = {"key": "old"}

        v_new = VersionDependantVariable(Version(1, 19), Version(999, 999), "v_new_val")
        v_old = VersionDependantVariable(Version(1, 0), Version(1, 18),
                                         "v_old_val")

        picker = VersionDependantVariablePicker([v_new, v_old])

        config.default_configuration = {"key": picker}

        config.set_configuration_default_property("key", Version(1, 20))
        assert config.configuration["key"] == "v_new_val"

        config.set_configuration_default_property("key", Version(1, 17))
        assert config.configuration["key"] == "v_old_val"

    def test_nested_version_dependant_resolution(self):
        config = ConfigFile()
        config.configuration = {"outer": {"inner": "old"}}

        v_new = VersionDependantVariable(Version(1, 19), Version(999, 999), "v_new_val")
        v_old = VersionDependantVariable(Version(1, 0), Version(1, 18), "v_old_val")

        picker = VersionDependantVariablePicker([v_new, v_old])

        config.default_configuration = {
            "outer": {
                "inner": picker,
                "inner_list": [picker]
            }
        }

        config.set_configuration_default_property("outer/inner", Version(1, 20))
        assert config.configuration["outer"]["inner"] == "v_new_val"

        config.set_configuration_default_property("outer/inner_list", Version(1, 20))
        assert config.configuration["outer"]["inner_list"] == ["v_new_val"]

        defaults = config.get_default_values_for_variables(["outer"], Version(1, 17))
        assert defaults["outer"]["inner"] == "v_old_val"
        assert defaults["outer"]["inner_list"] == ["v_old_val"]

    def test_get_default_values_return_none(self):
        config = ConfigFile()
        config.default_configuration = {"key": "value"}

        defaults = config.get_default_values_for_variables(["missing"], Version(1, 20))
        assert defaults["missing"] is None

    def test_get_default_values_version_dependant(self):
        config = ConfigFile()
        var = VersionDependantVariable(Version(1, 18), Version(1, 19), "value")
        picker = VersionDependantVariablePicker([var])
        config.default_configuration = {"key": picker}

        defaults = config.get_default_values_for_variables(["key"], Version(1, 18))
        assert defaults["key"] == "value"

        defaults = config.get_default_values_for_variables(["key"], Version(1, 17))
        assert defaults["key"] is None
