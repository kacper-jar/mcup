import json
import logging
import os
import re
from typing import Iterator, Tuple
import requests

from mcup.core.status import Status, StatusCode
from mcup.core.user_config import UserConfig
from mcup.core.utils.path import PathProvider


class LockerUpdater:
    """Updates and loads the locker file that contains server information and versions."""

    def __init__(self):
        """Initialize the locker updater with default paths and URLs."""
        self.logger = logging.getLogger(__name__)
        self.user_config = UserConfig()

        path_provider = PathProvider()

        self.locker_path = path_provider.get_config_path() / "locker.json"
        self.meta_path = path_provider.get_config_path() / "locker-meta.json"

        config_dir = path_provider.get_config_path()
        os.makedirs(config_dir, exist_ok=True)

        self.logger.debug(f"LockerUpdater initialized - locker: {self.locker_path}, meta: {self.meta_path}")

    def _parse_github_url(self, repo_url: str) -> Tuple[str, str]:
        """
        Parse GitHub repository URL to extract owner and repository name.

        Args:
            repo_url: GitHub repository URL (e.g., https://github.com/owner/repo)

        Returns:
            Tuple of (owner, repo_name)
        """
        self.logger.debug(f"Parsing GitHub URL: {repo_url}")

        repo_url = repo_url.rstrip('/').replace('.git', '')

        github_pattern = r'https://github\.com/([^/]+)/([^/]+)'
        match = re.match(github_pattern, repo_url)

        if not match:
            self.logger.error(f"Invalid GitHub repository URL format: {repo_url}")
            raise ValueError(f"Invalid GitHub repository URL: {repo_url}")

        self.logger.debug(f"Parsed GitHub URL - owner: {match.group(1)}, repo: {match.group(2)}")

        return match.group(1), match.group(2)

    def _get_repository_config(self) -> Tuple[str, str]:
        """
        Get repository configuration from UserConfig or use defaults.

        Returns:
            Tuple of (remote_url, branch)
        """
        self.logger.debug("Getting repository configuration")

        remote_config_statuses = list(self.user_config.get_configuration("locker.remote",
                                                                         "https://github.com/kacper-jar/mcup-locker-file"))
        branch_config_statuses = list(self.user_config.get_configuration("locker.branch", "main"))

        remote_url = None
        for status in remote_config_statuses:
            if status.status_code == StatusCode.SUCCESS:
                remote_url = status.status_details
                self.logger.debug(f"Remote URL from config: {remote_url}")
                break

        branch = None
        for status in branch_config_statuses:
            if status.status_code == StatusCode.SUCCESS:
                branch = status.status_details
                self.logger.debug(f"Branch from config: {branch}")
                break

        return remote_url, branch

    def _build_urls(self, remote_url: str, branch: str) -> Tuple[str, str]:
        """
        Build locker file URL and API URL from repository configuration.

        Args:
            remote_url: GitHub repository URL
            branch: Branch name

        Returns:
            Tuple of (locker_file_url, api_url)
        """
        self.logger.debug(f"Building URLs for remote: {remote_url}, branch: {branch}")

        try:
            owner, repo_name = self._parse_github_url(remote_url)

            locker_url = f"https://raw.githubusercontent.com/{owner}/{repo_name}/refs/heads/{branch}/locker.json"

            api_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits/{branch}"

            self.logger.debug(f"Built URLs - locker: {locker_url}, api: {api_url}")

            return locker_url, api_url

        except ValueError as e:
            self.logger.error(f"Failed to parse repository URL: {e}")
            raise

    def _check_if_modified(self):
        """Check if the locker file is modified or not."""
        self.logger.debug(f"Checking if locker file is modified: {self.meta_path}")

        if not os.path.exists(self.meta_path):
            self.logger.debug("Meta file does not exist, considering unmodified")
            return False, None

        try:
            with open(self.meta_path, "r", encoding="utf-8") as f:
                meta_data = json.load(f)
            is_modified = meta_data.get("is_modified")
            self.logger.debug(f"Locker file modified status: {is_modified}")
            return is_modified, None
        except (json.JSONDecodeError, IOError) as e:
            self.logger.error(f"Failed to read locker-meta.json: {e}")
            return None, e

    def _get_remote_last_update(self, api_url: str):
        """Fetches the last commit date from GitHub."""
        self.logger.debug(f"Fetching remote last update from: {api_url}")

        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            commit_data = response.json()
            last_update = commit_data["commit"]["committer"]["date"]
            self.logger.debug(f"Remote last update: {last_update}")
            return last_update, None
        except requests.RequestException as e:
            self.logger.error(f"Failed to retrieve latest locker file timestamp: {e}")
            return None, e

    def _get_local_last_update(self):
        """Reads the local last updated timestamp from locker-meta.json."""
        self.logger.debug(f"Getting local last update from: {self.meta_path}")

        if not os.path.exists(self.meta_path):
            return "1970-01-01T00:00:00Z", None
        try:
            with open(self.meta_path, "r", encoding="utf-8") as f:
                meta_data = json.load(f)
            last_update = meta_data.get("last_updated")
            self.logger.debug(f"Local last update: {last_update}")
            return last_update, None
        except (json.JSONDecodeError, IOError) as e:
            self.logger.error(f"Failed to read locker-meta.json: {e}")
            return None, e

    def _update_local_meta(self, date: str, remote_url: str, branch: str):
        """Updates locker-meta.json with the latest update timestamp and configuration."""
        self.logger.debug(f"Updating local meta - date: {date}, remote: {remote_url}, branch: {branch}")

        try:
            meta_data = {
                "last_updated": date,
                "is_modified": False,
                "remote": remote_url,
                "branch": branch
            }
            with open(self.meta_path, "w", encoding="utf-8") as f:
                json.dump(meta_data, f, indent=4)
            self.logger.info(f"Local meta updated successfully")
            return True, None
        except IOError as e:
            self.logger.error(f"Failed to update locker-meta.json: {e}")
            return False, e

    def _download_locker_file(self, locker_url: str):
        """Downloads the latest locker.json from GitHub."""
        self.logger.info(f"Downloading locker file from: {locker_url}")

        try:
            response = requests.get(locker_url, timeout=10)
            response.raise_for_status()

            content_length = len(response.text)
            self.logger.debug(f"Downloaded locker file size: {content_length} characters")

            with open(self.locker_path, "w", encoding="utf-8") as f:
                f.write(response.text)

            self.logger.info(f"Locker file downloaded successfully to: {self.locker_path}")
            return True, None
        except requests.RequestException as e:
            self.logger.error(f"Failed to download locker file: {e}")
            return False, e

    def _check_config_change(self, remote_url: str, branch: str) -> bool:
        """Check if repository configuration has changed since last update."""
        self.logger.debug("Checking if repository configuration has changed")

        if not os.path.exists(self.meta_path):
            self.logger.debug("Meta file does not exist, considering config changed")
            return True

        try:
            with open(self.meta_path, "r", encoding="utf-8") as f:
                meta_data = json.load(f)

            old_remote = meta_data.get("remote")
            old_branch = meta_data.get("branch")

            config_changed = (old_remote != remote_url or old_branch != branch)

            if config_changed:
                self.logger.info(
                    f"Repository configuration changed - old: {old_remote}/{old_branch}, new: {remote_url}/{branch}")
            else:
                self.logger.debug("Repository configuration unchanged")

            return config_changed
        except (json.JSONDecodeError, IOError) as e:
            self.logger.warning(f"Failed to read meta file for config change check: {e}")
            return True

    def update_locker(self, force_update=False) -> Iterator[Status]:
        """Checks for updates and downloads the new locker.json if needed."""
        try:
            remote_url, branch = self._get_repository_config()
            locker_url, api_url = self._build_urls(remote_url, branch)

            self.logger.info(f"Using remote: {remote_url}, branch: {branch}")

        except ValueError as e:
            yield Status(StatusCode.ERROR_CONFIG_READ_FAILED, str(e))
            return

        config_changed = self._check_config_change(remote_url, branch)
        if config_changed:
            self.logger.info("Repository configuration changed, forcing update")
            force_update = True

        is_modified, err = self._check_if_modified()
        if is_modified is None:
            yield Status(StatusCode.ERROR_LOCKER_META_READ_FAILED)
            return

        yield Status(StatusCode.INFO_LOCKER_USING_REMOTE, {"remote_url": remote_url, "branch": branch})

        if is_modified and not force_update:
            yield Status(StatusCode.INFO_LOCKER_MODIFIED)
            return

        remote_date, err = self._get_remote_last_update(api_url)
        if not remote_date:
            yield Status(StatusCode.ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED, err)
            return

        local_date, err = self._get_local_last_update()
        if local_date is None:
            yield Status(StatusCode.ERROR_LOCKER_META_READ_FAILED, err)

        if remote_date <= local_date and not force_update:
            if os.path.exists(self.locker_path):
                yield Status(StatusCode.INFO_LOCKER_UP_TO_DATE)
                return

        yield Status(StatusCode.INFO_LOCKER_UPDATING)
        download_result, err = self._download_locker_file(locker_url)
        if not download_result:
            yield Status(StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED, err)
            return

        local_meta_update_result, err = self._update_local_meta(remote_date, remote_url, branch)
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
                self.logger.info("Locker file loaded successfully.")
        else:
            yield Status(StatusCode.SUCCESS, {"servers": {}})
            self.logger.warning("No locker file found. Using empty locker file instead.")
