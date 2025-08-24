from pathlib import Path

from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from mcup.cli.language import Language
from mcup.cli.ui.components import ServerConfigsCollector, ServerConfigsCollectorFlags
from mcup.core.handlers import ServerHandler
from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerUpdater


class ServerCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup server create <server_type> <server_version> [path]' command."""
        server_type = args.server_type
        server_version = args.server_version
        server_path = Path(args.path).resolve()
        locker = LockerUpdater()
        language = Language()

        print(language.get_string("INFO_CREATING_SERVER", server_type, server_version, server_path))
        print(language.get_string("INFO_EULA"))

        locker_data = None
        for status in locker.load_locker():
            match status.status_code:
                case StatusCode.INFO_LOCKER_USING_REMOTE:
                    print(language.get_string("INFO_LOCKER_USING_REMOTE", status.status_details['remote_url'],
                                              status.status_details['branch']))
                case StatusCode.INFO_LOCKER_MODIFIED | StatusCode.INFO_LOCKER_UP_TO_DATE | StatusCode.INFO_LOCKER_UPDATING:
                    print(language.get_string(status.status_code.name))
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_LOCKER"))
                    locker_data = status.status_details
                    break
                case _:
                    error_message = language.get_string(status.status_code.name, status.status_details)
                    print(error_message)
                    return None

        if locker_data is None:
            print(language.get_string("ERROR_LOCKER_LOAD_FAILED"))
            return None

        if server_type not in locker_data["servers"]:
            print(language.get_string("ERROR_INVALID_SERVER_TYPE", server_type))
            return None

        locker_entry = None
        for version in locker_data["servers"][server_type]:
            if version["version"] == server_version:
                if version["source"] not in ["DOWNLOAD", "BUILDTOOLS", "INSTALLER"]:
                    print(language.get_string("ERROR_SERVER_SOURCE_NOT_SUPPORTED", version["source"]))
                    return None
                locker_entry = version
                break

        if locker_entry is None:
            print(language.get_string("ERROR_INVALID_SERVER_VERSION", server_version))
            return None

        if args.no_configs:
            flags = ServerConfigsCollectorFlags.NO_CONFIGS
        elif args.no_defaults:
            flags = ServerConfigsCollectorFlags.NO_DEFAULTS
        elif args.all_defaults:
            flags = ServerConfigsCollectorFlags.ALL_DEFAULTS
        else:
            flags = ServerConfigsCollectorFlags.NONE

        assembler_linker_conf = ServerConfigsCollector.collect_configurations(server_version, locker_entry["configs"],
                                                                              flags)

        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
        ) as progress:
            server = ServerHandler()
            task = None

            java_info_codes = {
                StatusCode.INFO_JAVA_MINIMUM_21: "INFO_JAVA_MINIMUM_21",
                StatusCode.INFO_JAVA_MINIMUM_17: "INFO_JAVA_MINIMUM_17",
                StatusCode.INFO_JAVA_MINIMUM_16: "INFO_JAVA_MINIMUM_16",
                StatusCode.INFO_JAVA_MINIMUM_8: "INFO_JAVA_MINIMUM_8"
            }

            error_codes = {
                StatusCode.ERROR_DOWNLOAD_SERVER_FAILED: "ERROR_DOWNLOAD_SERVER_FAILED",
                StatusCode.ERROR_DOWNLOAD_INSTALLER_FAILED: "ERROR_DOWNLOAD_INSTALLER_FAILED",
                StatusCode.ERROR_INSTALLER_NOT_FOUND: "ERROR_INSTALLER_NOT_FOUND",
                StatusCode.ERROR_JAVA_VERSION_DETECTION_FAILED: "ERROR_JAVA_VERSION_DETECTION_FAILED",
                StatusCode.ERROR_SERVER_JAR_NOT_FOUND: "ERROR_SERVER_JAR_NOT_FOUND",
                StatusCode.ERROR_SERVER_SOURCE_NOT_SUPPORTED: "ERROR_SERVER_SOURCE_NOT_SUPPORTED"
            }

            for status in server.create(server_path, server_type, server_version, locker_entry, assembler_linker_conf):
                match status.status_code:
                    case StatusCode.PROGRESSBAR_NEXT:
                        if task is not None:
                            progress.update(task, advance=1)
                        task = progress.add_task(status.status_details[0], total=status.status_details[1])
                    case StatusCode.PROGRESSBAR_UPDATE:
                        progress.update(task, advance=status.status_details)
                    case StatusCode.PROGRESSBAR_FINISH_TASK:
                        progress.update(task, advance=1)
                    case StatusCode.PROGRESSBAR_END:
                        progress.stop()
                    case StatusCode.SUCCESS:
                        print(language.get_string("SUCCESS_SERVER"))
                        return None
                    case status_code if status_code in java_info_codes:
                        print(language.get_string(java_info_codes[status_code]))
                    case status_code if status_code in error_codes:
                        progress.stop()
                        error_msg = language.get_string(error_codes[status_code], status.status_details)
                        print(error_msg)
                        return None

    @staticmethod
    def list(args):
        """Handles 'mcup server list' command."""
        locker = LockerUpdater()
        language = Language()

        for status in locker.load_locker():
            match status.status_code:
                case StatusCode.INFO_LOCKER_MODIFIED:
                    print(language.get_string("INFO_LOCKER_MODIFIED"))
                case StatusCode.INFO_LOCKER_USING_REMOTE:
                    print(language.get_string("INFO_LOCKER_USING_REMOTE", status.status_details['remote_url'],
                                              status.status_details['branch']))
                case StatusCode.INFO_LOCKER_UP_TO_DATE:
                    print(language.get_string("INFO_LOCKER_UP_TO_DATE"))
                case StatusCode.INFO_LOCKER_UPDATING:
                    print(language.get_string("INFO_LOCKER_UPDATING"))
                case StatusCode.ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED:
                    print(language.get_string("ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED",
                                              status.status_details))
                    return
                case StatusCode.ERROR_LOCKER_META_READ_FAILED:
                    print(language.get_string("ERROR_LOCKER_META_READ_FAILED", status.status_details))
                    return
                case StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED:
                    print(language.get_string("ERROR_LOCKER_DOWNLOAD_FAILED", status.status_details))
                    return
                case StatusCode.ERROR_LOCKER_META_UPDATE_FAILED:
                    print(language.get_string("ERROR_LOCKER_META_UPDATE_FAILED", status.status_details))
                    return
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_LOCKER"))
                    locker_data = status.status_details
                    break

        for server in locker_data["servers"]:
            versions = [version['version'] for version in locker_data["servers"][server]]
            print(f"{server}:")
            print(f"  {', '.join(versions)}")
