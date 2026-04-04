import logging
from datetime import datetime, timezone

import requests

from mcup import __version__
from mcup.core.status import Status, StatusCode


class UpdateChecker:
    """Checks GitHub Releases for a newer version of mcup."""

    GITHUB_RELEASES_URL = "https://api.github.com/repos/kacper-jar/mcup/releases"
    REQUEST_TIMEOUT = 2  # seconds

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def check_for_update(self, channel: str = "stable"):
        """Check GitHub Releases for a newer version of mcup.

        Args:
            channel: "stable" to only consider non-pre-release releases,
                     "all" to consider any release including pre-releases.
        """
        self.logger.debug(f"Checking for updates (channel={channel})")

        try:
            response = requests.get(
                self.GITHUB_RELEASES_URL,
                timeout=self.REQUEST_TIMEOUT,
                headers={"Accept": "application/vnd.github+json"},
            )
            response.raise_for_status()
            releases = response.json()
        except Exception as e:
            self.logger.debug(f"Update check failed (network/HTTP error): {e}")
            yield Status(StatusCode.ERROR_UPDATE_CHECK_FAILED, str(e))
            return

        if not isinstance(releases, list) or len(releases) == 0:
            self.logger.debug("Update check: empty or invalid releases response")
            yield Status(StatusCode.ERROR_UPDATE_CHECK_FAILED, "empty response")
            return

        current_version = __version__
        current_tag_candidates = {current_version, f"v{current_version}"}

        current_published_at = None
        for release in releases:
            tag = release.get("tag_name", "")
            if tag in current_tag_candidates:
                raw = release.get("published_at")
                if raw:
                    current_published_at = datetime.fromisoformat(
                        raw.replace("Z", "+00:00")
                    )
                self.logger.debug(
                    f"Found current release tag '{tag}' published at {current_published_at}"
                )
                break

        if current_published_at is None:
            self.logger.debug(
                f"Current version tag '{current_version}' not found in GitHub releases — skipping update check"
            )
            yield Status(StatusCode.ERROR_UPDATE_CHECK_FAILED, "current tag not found")
            return

        for release in releases:
            is_prerelease = release.get("prerelease", False)
            if channel == "stable" and is_prerelease:
                continue

            if release.get("draft", False):
                continue

            tag = release.get("tag_name", "")
            if tag in current_tag_candidates:
                continue

            raw = release.get("published_at")
            if not raw:
                continue

            release_date = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            if release_date > current_published_at:
                html_url = release.get("html_url", self.GITHUB_RELEASES_URL)
                self.logger.info(
                    f"Update available: {tag} (published {release_date}), "
                    f"current: {current_version} (published {current_published_at})"
                )
                yield Status(
                    StatusCode.INFO_UPDATE_AVAILABLE,
                    {
                        "latest_tag": tag,
                        "current_version": current_version,
                        "html_url": html_url,
                        "prerelease": is_prerelease,
                    },
                )
                return

        self.logger.debug("Update check: already on the latest release")
        yield Status(StatusCode.SUCCESS)
