from mcup.core.utils.version import Version, VersionDependantVariable, VersionDependantVariablePicker


class TestVersionDependantVariablePicker:

    def test_resolve_match(self):
        var = VersionDependantVariable(Version(1, 18), Version(1, 19), "value")
        picker = VersionDependantVariablePicker([var])

        assert picker.resolve(Version(1, 18)) == "value"
        assert picker.resolve(Version(1, 19)) == "value"
        assert picker.resolve(Version(1, 18, 2)) == "value"

    def test_resolve_no_match(self):
        var = VersionDependantVariable(Version(1, 18), Version(1, 19), "value")
        picker = VersionDependantVariablePicker([var])

        assert picker.resolve(Version(1, 17)) is None
        assert picker.resolve(Version(1, 20)) is None

    def test_resolve_multiple_variables(self):
        v1 = VersionDependantVariable(Version(1, 17), Version(1, 17), "v1")
        v2 = VersionDependantVariable(Version(1, 18), Version(1, 18), "v2")
        picker = VersionDependantVariablePicker([v1, v2])

        assert picker.resolve(Version(1, 17)) == "v1"
        assert picker.resolve(Version(1, 18)) == "v2"
