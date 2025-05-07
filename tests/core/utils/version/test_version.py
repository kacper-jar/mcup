from mcup.core.utils.version.version import Version


def test_init():
    """Test initialization of Version objects."""
    version = Version(1, 2, 3)
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3

    version = Version(1, 2)
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 0


def test_from_string():
    """Test creating Version objects from strings."""
    version = Version.from_string("1.2.3")
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3

    version = Version.from_string("1.2")
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 0


def test_comparison():
    """Test version comparison operators."""
    v1 = Version(1, 2, 3)
    v2 = Version(1, 2, 3)
    v3 = Version(1, 2, 4)
    v4 = Version(1, 3, 0)
    v5 = Version(2, 0, 0)

    assert v1 == v2
    assert v1 != v3

    assert v1 < v3
    assert v3 < v4
    assert v4 < v5

    assert v1 <= v2
    assert v1 <= v3

    assert v3 > v1
    assert v4 > v3
    assert v5 > v4

    assert v2 >= v1
    assert v3 >= v1


def test_get_methods():
    """Test getter methods."""
    version = Version(1, 2, 3)
    assert version.get_major() == 1
    assert version.get_minor() == 2
    assert version.get_patch() == 3


def test_get_string():
    """Test string representation."""
    version = Version(1, 2, 3)
    assert version.get_string() == "1.2.3"

    version = Version(1, 2, 0)
    assert version.get_string() == "1.2"
