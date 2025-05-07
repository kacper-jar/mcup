from pathlib import Path

from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

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
                    case StatusCode.ERROR_DOWNLOAD_SERVER_FAILED:
                        progress.stop()
                        print(f"Failed to download server. HTTP {status.status_details}")
                        return
                    case StatusCode.ERROR_DOWNLOAD_BUILDTOOLS_FAILED:
                        progress.stop()
                        print(f"Failed to download Spigot BuildTools. HTTP {status.status_details}")
                        return
                    case StatusCode.ERROR_BUILD_TOOLS_NOT_FOUND:
                        progress.stop()
                        print("Spigot BuildTools not found.")
                        return
                    case StatusCode.ERROR_SERVER_JAR_NOT_FOUND:
                        progress.stop()
                        print("Server JAR file not found. Check BuildTools.log.txt in server folder for more info.")
                        return
                    case StatusCode.PRINT_INFO:
                        print(status.status_details)
                    case StatusCode.SUCCESS:
                        print("Server created successfully.")
