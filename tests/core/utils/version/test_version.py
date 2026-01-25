import pytest
from mcup.core.utils.version.version import Version


class TestVersion:
    def test_version_comparison(self):
        """Test version comparison operators."""
        v1_8 = Version(1, 8)
        v1_8_2 = Version(1, 8, 2)
        v1_12 = Version(1, 12, 0)
        v1_12_2 = Version(1, 12, 2)

        assert Version(1, 8) == Version(1, 8, 0)
        assert Version(1, 8, 2) == Version(1, 8, 2)

        assert v1_12 > v1_8
        assert v1_8_2 > v1_8
        assert v1_12_2 > v1_12

        assert v1_12 >= v1_8
        assert Version(1, 8) >= Version(1, 8)

        assert v1_8 < v1_12
        assert v1_8 < v1_8_2

        assert v1_8 <= v1_12
        assert Version(1, 8) <= Version(1, 8)

        # Test the new versioning scheme
        v26_0 = Version(26, 0)
        assert v26_0 > v1_12_2
        assert v26_0 > Version(1, 21, 4)
        assert v26_0.major == 26

        assert (v1_8 == "1.8") is False

        with pytest.raises(TypeError):
            _ = v1_8 < "1.12"

    def test_from_string(self):
        """Test creating Version from string."""
        v = Version.from_string("1.12.2")
        assert v.major == 1
        assert v.minor == 12
        assert v.patch == 2

        v = Version.from_string("1.8")
        assert v.major == 1
        assert v.minor == 8
        assert v.patch == 0

        v = Version.from_string("26.0")
        assert v.major == 26
        assert v.minor == 0
        assert v.patch == 0

    def test_get_string(self):
        """Test string representation."""
        assert Version(1, 8, 0).get_string() == "1.8"
        assert Version(1, 8, 2).get_string() == "1.8.2"
        assert Version(1, 20, 1).get_string() == "1.20.1"
        assert Version(26, 0, 0).get_string() == "26.0"
        assert Version(26, 0, 1).get_string() == "26.0.1"
