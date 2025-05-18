from mcup.cli.language import Language
from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerManager


class ServerInfoPrompt:
    @staticmethod
    def get_server_info(locker: LockerManager):
        language = Language()

        for status in locker.load_locker():
            match status.status_code:
                case StatusCode.INFO_LOCKER_UP_TO_DATE:
                    print(language.get_string("INFO_LOCKER_UP_TO_DATE"))
                case StatusCode.INFO_LOCKER_UPDATING:
                    print(language.get_string("INFO_LOCKER_UPDATING"))
                case StatusCode.ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED:
                    print(language.get_string("ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED", status.status_details))
                case StatusCode.ERROR_LOCKER_META_READ_FAILED:
                    print(language.get_string("ERROR_LOCKER_META_READ_FAILED", status.status_details))
                case StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED:
                    print(language.get_string("ERROR_LOCKER_DOWNLOAD_FAILED", status.status_details))
                case StatusCode.ERROR_LOCKER_META_UPDATE_FAILED:
                    print(language.get_string("ERROR_LOCKER_META_UPDATE_FAILED", status.status_details))
                case StatusCode.SUCCESS:
                    locker_data = status.status_details
                    break

        server_type = input("Server type (full list available at: ): ")
        is_valid_server_type = False
        for server in locker_data["servers"]:
            if server == server_type:
                is_valid_server_type = True
                break
        if not is_valid_server_type:
            raise Exception(f"Invalid or unsupported server type: {server_type}")

        server_version = input(f"{server_type} server version (full list available at: ): ")
        is_valid_server_version = False
        for version in locker_data["servers"][server_type]:
            if version["version"] == server_version:
                is_valid_server_version = True
                source = version["source"]
                if source == "DOWNLOAD":
                    target = version["url"]
                elif source == "BUILDTOOLS":
                    target = version["target"]
                configs = version["configs"]
                break
        if not is_valid_server_version:
            raise Exception(f"Invalid or unsupported server version: {server_version}")

        return server_type, server_version, source, target, configs
