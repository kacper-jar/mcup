import json
import os
import requests


class LockerManager:
    """Manages the locker file that contains server information and versions."""
    def __init__(self):
        """Initialize the locker manager with default paths and URLs."""
        self.locker_url = "https://raw.githubusercontent.com/kacper-jar/mcup-locker-file/refs/heads/main/locker.json"
        self.repo_api_url = "https://api.github.com/repos/kacper-jar/mcup-locker-file/commits/main"
        self.locker_path = "locker.json"
        self.meta_path = "locker-meta.json"

    def get_remote_last_update(self):
        """Fetches the last commit date from GitHub."""
        try:
            response = requests.get(self.repo_api_url, timeout=10)
            response.raise_for_status()
            commit_data = response.json()
            return commit_data["commit"]["committer"]["date"]
        except requests.RequestException as e:
            print(f"Error fetching last commit date: {e}")
            return None

    def get_local_last_update(self):
        """Reads the local last updated timestamp from locker-meta.json."""
        if not os.path.exists(self.meta_path):
            return None
        try:
            with open(self.meta_path, "r", encoding="utf-8") as f:
                meta_data = json.load(f)
            return meta_data.get("last_updated")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading locker-meta.json: {e}")
            return None

    def update_local_meta(self, date):
        """Updates locker-meta.json with the latest update timestamp."""
        try:
            with open(self.meta_path, "w", encoding="utf-8") as f:
                json.dump({"last_updated": date}, f, indent=4)
        except IOError as e:
            print(f"Error updating locker-meta.json: {e}")

    def download_locker_file(self):
        """Downloads the latest locker.json from GitHub."""
        try:
            response = requests.get(self.locker_url, timeout=10)
            response.raise_for_status()
            with open(self.locker_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Successfully updated locker.json")
            return True
        except requests.RequestException as e:
            print(f"Error downloading locker.json: {e}")
            return False

    def update_locker(self):
        """Checks for updates and downloads the new locker.json if needed."""
        remote_date = self.get_remote_last_update()
        if not remote_date:
            print("Could not retrieve the latest update timestamp.")
            return

        local_date = self.get_local_last_update()
        if local_date and remote_date <= local_date:
            print("Locker.json is already up-to-date.")
            return

        print("Updating locker.json...")
        if self.download_locker_file():
            self.update_local_meta(remote_date)

    def load_locker(self):
        """Load the locker.json file."""
        self.update_locker()
        if os.path.exists(self.locker_path):
            with open(self.locker_path, 'r') as file:
                return json.load(file)
        return {"servers": {}}
