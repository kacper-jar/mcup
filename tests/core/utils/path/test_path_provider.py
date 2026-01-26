from pathlib import Path
from unittest.mock import patch
from mcup.core.utils.path.path_provider import PathProvider


class TestPathProvider:

    def test_get_config_path_linux(self):
        with patch("sys.platform", "linux"):
            provider = PathProvider()
            path = provider.get_config_path()
            assert str(path).endswith(".config/mcup")

    def test_get_config_path_mac(self):
        with patch("sys.platform", "darwin"):
            provider = PathProvider()
            path = provider.get_config_path()
            assert "Library/Application Support/mcup/config" in str(path)

    def test_get_config_path_windows(self):
        with patch("sys.platform", "win32"), \
                patch.dict("os.environ", {"APPDATA": "C:\\Users\\Test\\AppData\\Roaming"}):
            provider = PathProvider()
            path = provider.get_config_path()
            expected = Path("C:\\Users\\Test\\AppData\\Roaming") / "mcup"
            assert path == expected

    def test_get_templates_path_linux(self):
        with patch("sys.platform", "linux"):
            provider = PathProvider()
            path = provider.get_templates_path()
            assert str(path).endswith(".local/share/mcup/templates")
