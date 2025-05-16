class Language:
    strings = {
        # Locker
        "INFO_LOCKER_UP_TO_DATE": "Locker file is already up-to-date.",
        "INFO_LOCKER_UPDATING": "Updating locker file...",
        "ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED": "Could not retrieve the latest update timestamp. Details: {}",
        "ERROR_LOCKER_META_READ_FAILED": "Error reading locker meta file. Details: {}",
        "ERROR_LOCKER_DOWNLOAD_FAILED": "Error downloading locker file. Details: {}",
        "ERROR_LOCKER_META_UPDATE_FAILED": "Error updating locker meta file. Details: {}",
        "SUCCESS_LOCKER": "Successfully updated locker file."
    }

    def get_string(self, key, *args):
        if args is not None:
            return self.strings.get(key, key).format(*args)
        return self.strings.get(key, key)
