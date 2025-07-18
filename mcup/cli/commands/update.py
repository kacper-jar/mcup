from mcup.cli.language import Language
from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerUpdater


class UpdateCommand:
    @staticmethod
    def run(args):
        """Handles 'mcup update' command."""
        language = Language()
        locker_manager = LockerUpdater()

        for status in locker_manager.update_locker():
            match status.status_code:
                case StatusCode.INFO_LOCKER_UP_TO_DATE:
                    print(language.get_string("INFO_LOCKER_UP_TO_DATE"))
                case StatusCode.INFO_LOCKER_UPDATING:
                    print(language.get_string("INFO_LOCKER_UPDATING"))
                case StatusCode.ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED:
                    print(language.get_string("ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED",
                                              status.status_details))
                case StatusCode.ERROR_LOCKER_META_READ_FAILED:
                    print(language.get_string("ERROR_LOCKER_META_READ_FAILED",
                                              status.status_details))
                case StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED:
                    print(language.get_string("ERROR_LOCKER_DOWNLOAD_FAILED",
                                              status.status_details))
                case StatusCode.ERROR_LOCKER_META_UPDATE_FAILED:
                    print(language.get_string("ERROR_LOCKER_META_UPDATE_FAILED",
                                              status.status_details))
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_LOCKER"))
