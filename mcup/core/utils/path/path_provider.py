import os
import sys
from pathlib import Path


class PathProvider:
    """Class providing platform-agnostic directory paths."""
    def __init__(self):
        """Initialize platform."""
        self.platform = sys.platform

    def get_config_path(self):
        """Get path for configuration files."""
        match self.platform:
            case "linux":
                return Path("~/.config/mcup/").expanduser()
            case "darwin":
                return Path("~/Library/Application Support/mcup/config/").expanduser()
            case "win32":
                return Path(os.environ["APPDATA"]) / "mcup"
        return None

    def get_templates_path(self):
        """Get path for template files."""
        match self.platform:
            case "linux":
                return Path("~/.local/share/mcup/templates/").expanduser()
            case "darwin":
                return Path("~/Library/Application Support/mcup/templates/").expanduser()
            case "win32":
                return Path(os.environ["LOCALAPPDATA"]) / "mcup" / "templates"
        return None
