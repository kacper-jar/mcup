import os
import sys
from pathlib import Path


class PathProvider:
    def __init__(self):
        self.platform = sys.platform

    def get_config_path(self):
        match self.platform:
            case "linux":
                return Path("~/.config/mcup/").expanduser()
            case "darwin":
                return Path("~/Library/Application Support/mcup/config/").expanduser()
            case "win32":
                return Path(os.environ["APPDATA"]) / "mcup"
        return None

    def get_templates_path(self):
        match self.platform:
            case "linux":
                return Path("~/.local/share/mcup/templates/").expanduser()
            case "darwin":
                return Path("~/Library/Application Support/mcup/templates/").expanduser()
            case "win32":
                return Path(os.environ["LOCALAPPDATA"]) / "mcup" / "templates"
        return None
