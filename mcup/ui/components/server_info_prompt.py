from mcup.utils.locker import LockerManager


class ServerInfoPrompt:
    @staticmethod
    def get_server_info(locker: LockerManager):
        locker_data = locker.load_locker()

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