from pathlib import Path
from mcup.core.utils.path.path_provider import PathProvider


"""Test cases for the PathProvider class."""


def test_get_config_path_linux(monkeypatch):
    """Test getting config path on Linux."""
    monkeypatch.setattr('sys.platform', 'linux')
    provider = PathProvider()
    expected_path = Path("~/.config/mcup/").expanduser()
    assert provider.get_config_path() == expected_path


def test_get_config_path_macos(monkeypatch):
    """Test getting config path on macOS."""
    monkeypatch.setattr('sys.platform', 'darwin')
    provider = PathProvider()
    expected_path = Path("~/Library/Application Support/mcup/config/").expanduser()
    assert provider.get_config_path() == expected_path


def test_get_config_path_windows(monkeypatch):
    """Test getting config path on Windows."""
    monkeypatch.setattr('sys.platform', 'win32')
    monkeypatch.setenv("APPDATA", "C:\\Users\\Test\\AppData\\Roaming")
    provider = PathProvider()
    expected_path = Path("C:\\Users\\Test\\AppData\\Roaming") / "mcup"
    assert provider.get_config_path() == expected_path


def test_get_config_path_unknown(monkeypatch):
    """Test getting config path on unknown platform."""
    monkeypatch.setattr('sys.platform', 'unknown')
    provider = PathProvider()
    assert provider.get_config_path() is None


def test_get_templates_path_linux(monkeypatch):
    """Test getting templates path on Linux."""
    monkeypatch.setattr('sys.platform', 'linux')
    provider = PathProvider()
    expected_path = Path("~/.local/share/mcup/templates/").expanduser()
    assert provider.get_templates_path() == expected_path


def test_get_templates_path_macos(monkeypatch):
    """Test getting templates path on macOS."""
    monkeypatch.setattr('sys.platform', 'darwin')
    provider = PathProvider()
    expected_path = Path("~/Library/Application Support/mcup/templates/").expanduser()
    assert provider.get_templates_path() == expected_path


def test_get_templates_path_windows(monkeypatch):
    """Test getting templates path on Windows."""
    monkeypatch.setattr('sys.platform', 'win32')
    monkeypatch.setenv("LOCALAPPDATA", "C:\\Users\\Test\\AppData\\Local")
    provider = PathProvider()
    expected_path = Path("C:\\Users\\Test\\AppData\\Local") / "mcup" / "templates"
    assert provider.get_templates_path() == expected_path


def test_get_templates_path_unknown(monkeypatch):
    """Test getting templates path on unknown platform."""
    monkeypatch.setattr('sys.platform', 'unknown')
    provider = PathProvider()
    assert provider.get_templates_path() is None
