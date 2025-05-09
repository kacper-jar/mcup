import json
import os
from typing import Iterator

import requests

from mcup.core.status import Status, StatusCode
from mcup.core.utils.path import PathProvider


class LockerManager:
    """Manages the locker file that contains server information and versions."""
    def __init__(self):
        """Initialize the locker manager with default paths and URLs."""
        path_provider = PathProvider()

        self.locker_url = "https://raw.githubusercontent.com/kacper-jar/mcup-locker-file/refs/heads/main/locker.json"
        self.repo_api_url = "https://api.github.com/repos/kacper-jar/mcup-locker-file/commits/main"
        self.locker_path = path_provider.get_config_path() / "locker.json"
        self.meta_path = path_provider.get_config_path() / "locker-meta.json"

        config_dir = path_provider.get_config_path()
        os.makedirs(config_dir, exist_ok=True)

    def _get_remote_last_update(self):
        """Fetches the last commit date from GitHub."""
        try:
            response = requests.get(self.repo_api_url, timeout=10)
            response.raise_for_status()
            commit_data = response.json()
            return commit_data["commit"]["committer"]["date"], None
        except requests.RequestException as e:
            return None, e

    def _get_local_last_update(self):
        """Reads the local last updated timestamp from locker-meta.json."""
        if not os.path.exists(self.meta_path):
            return "1970-01-01T00:00:00Z", None
        try:
            with open(self.meta_path, "r", encoding="utf-8") as f:
                meta_data = json.load(f)
            return meta_data.get("last_updated"), None
        except (json.JSONDecodeError, IOError) as e:
            return None, e

    def _update_local_meta(self, date):
        """Updates locker-meta.json with the latest update timestamp."""
        try:
            with open(self.meta_path, "w", encoding="utf-8") as f:
                json.dump({"last_updated": date}, f, indent=4)
            return True, None
        except IOError as e:
            return False, e

    def _download_locker_file(self):
        """Downloads the latest locker.json from GitHub."""
        try:
            response = requests.get(self.locker_url, timeout=10)
            response.raise_for_status()
            with open(self.locker_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            return True, None
        except requests.RequestException as e:
            return False, e

    def update_locker(self) -> Iterator[Status]:
        """Checks for updates and downloads the new locker.json if needed."""
        remote_date, err = self._get_remote_last_update()
        if not remote_date:
            yield Status(StatusCode.ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED, err)
            return

        local_date, err = self._get_local_last_update()
        if local_date is None:
            yield Status(StatusCode.ERROR_LOCKER_META_READ_FAILED, err)

        if remote_date <= local_date:
            yield Status(StatusCode.PRINT_INFO, "Locker file is already up-to-date.")
            return

        yield Status(StatusCode.PRINT_INFO, "Updating locker file...")
        download_result, err = self._download_locker_file()
        if not download_result:
            yield Status(StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED, err)
            return

        local_meta_update_result, err = self._update_local_meta(remote_date)
        if local_meta_update_result:
            yield Status(StatusCode.SUCCESS)
        else:
            yield Status(StatusCode.ERROR_LOCKER_META_UPDATE_FAILED, err)

    def load_locker(self) -> Iterator[Status]:
        """Load the locker.json file."""
        for status in self.update_locker():
            if status.status_code != StatusCode.SUCCESS:
                yield status
            else:
                break
        if os.path.exists(self.locker_path):
            with open(self.locker_path, 'r') as file:
                yield Status(StatusCode.SUCCESS, json.load(file))
        else:
            yield Status(StatusCode.SUCCESS, {"servers": {}})
