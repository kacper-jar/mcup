from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerManager


class ServerInfoPrompt:
    @staticmethod
    def get_server_info(locker: LockerManager):
        for status in locker.load_locker():
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
