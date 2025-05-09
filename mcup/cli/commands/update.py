from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerManager


class UpdateCommand:
    @staticmethod
    def run(args):
        """Handles 'mcup update' command."""
        for status in LockerManager().update_locker():
            match status.status_code:
                case StatusCode.ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED:
                    print(f"Could not retrieve the latest update timestamp. Details: {status.status_details}")
                case StatusCode.ERROR_LOCKER_META_READ_FAILED:
                    print(f"Error reading locker meta file. Details: {status.status_details}")
                case StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED:
                    print(f"Error downloading locker file: {status.status_details}")
                case StatusCode.ERROR_LOCKER_META_UPDATE_FAILED:
                    print(f"Error updating locker meta file: {status.status_details}")
                case StatusCode.PRINT_INFO:
                    print(status.status_details)
                case StatusCode.SUCCESS:
                    print("Successfully updated locker file")
