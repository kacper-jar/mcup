from pathlib import Path
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from mcup.cli.language import Language
from mcup.core.handlers import ServerHandler
from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerManager
from mcup.cli.ui.components import ServerInfoPrompt, ServerConfigsCollector


class ServerCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup server create [path]' command."""
        server_path = Path(args.path).resolve()
        locker = LockerManager()
        language = Language()

        print(f"Creating a Minecraft server in: {server_path}")
        print("By creating Minecraft server you agree with Minecraft EULA available at https://aka.ms/MinecraftEULA")

        try:
            server_type, server_version, source, target, configs = ServerInfoPrompt.get_server_info(locker)
        except Exception as e:
            print(e)
            return

        assembler_linker_conf = ServerConfigsCollector.collect_configurations(server_version, configs)

        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
        ) as progress:
            server = ServerHandler()
            task = None

            for status in server.create(server_path, server_version, source, target, assembler_linker_conf):
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
                    case StatusCode.ERROR_DOWNLOAD_BUILDTOOLS_FAILED:
                        progress.stop()
                        print(language.get_string("ERROR_DOWNLOAD_BUILDTOOLS_FAILED", status.status_details))
                    case StatusCode.ERROR_BUILD_TOOLS_NOT_FOUND:
                        progress.stop()
                        print(language.get_string("ERROR_BUILD_TOOLS_NOT_FOUND"))
                    case StatusCode.ERROR_SERVER_JAR_NOT_FOUND:
                        progress.stop()
                        print(language.get_string("ERROR_SERVER_JAR_NOT_FOUND"))
                    case StatusCode.SUCCESS:
                        print("Server created successfully.")
