from pathlib import Path

from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from mcup.cli.language import Language
from mcup.cli.ui.components import ServerInfoPrompt, ServerConfigsCollector
from mcup.core.handlers import ServerHandler
from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerUpdater


class ServerCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup server create [path]' command."""
        server_path = Path(args.path).resolve()
        locker = LockerUpdater()
        language = Language()

        print(f"Creating a Minecraft server in: {server_path}")
        print("By creating Minecraft server you agree with Minecraft EULA available at https://aka.ms/MinecraftEULA")

        try:
            server_type, server_version, locker_entry = ServerInfoPrompt.get_server_info(locker)
        except Exception as e:
            print(e)
            return

        assembler_linker_conf = ServerConfigsCollector.collect_configurations(server_version, locker_entry["configs"])

        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
        ) as progress:
            server = ServerHandler()
            task = None

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
                    case StatusCode.INFO_JAVA_MINIMUM_21:
                        print(language.get_string("INFO_JAVA_MINIMUM_21"))
                    case StatusCode.INFO_JAVA_MINIMUM_17:
                        print(language.get_string("INFO_JAVA_MINIMUM_17"))
                    case StatusCode.INFO_JAVA_MINIMUM_16:
                        print(language.get_string("INFO_JAVA_MINIMUM_16"))
                    case StatusCode.INFO_JAVA_MINIMUM_8:
                        print(language.get_string("INFO_JAVA_MINIMUM_8"))
                    case StatusCode.ERROR_DOWNLOAD_SERVER_FAILED:
                        progress.stop()
                        print(language.get_string("ERROR_DOWNLOAD_SERVER_FAILED", status.status_details))
                    case StatusCode.ERROR_DOWNLOAD_INSTALLER_FAILED:
                        progress.stop()
                        print(language.get_string("ERROR_DOWNLOAD_INSTALLER_FAILED", status.status_details))
                    case StatusCode.ERROR_INSTALLER_NOT_FOUND:
                        progress.stop()
                        print(language.get_string("ERROR_INSTALLER_NOT_FOUND"))
                    case StatusCode.ERROR_SERVER_JAR_NOT_FOUND:
                        progress.stop()
                        print(language.get_string("ERROR_SERVER_JAR_NOT_FOUND"))
                    case StatusCode.ERROR_SERVER_SOURCE_NOT_SUPPORTED:
                        progress.stop()
                        print(language.get_string("ERROR_SERVER_SOURCE_NOT_SUPPORTED", status.status_details))
                    case StatusCode.SUCCESS:
                        print("Server created successfully.")

    @staticmethod
    def list(args):
        """Handles 'mcup server list' command."""
        locker = LockerUpdater()
        language = Language()

        for status in locker.load_locker():
            match status.status_code:
                case StatusCode.INFO_LOCKER_MODIFIED:
                    print(language.get_string("INFO_LOCKER_MODIFIED"))
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
