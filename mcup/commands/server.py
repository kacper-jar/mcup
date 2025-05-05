from pathlib import Path

from mcup.handlers import ServerHandler
from mcup.utils.locker import LockerManager
from mcup.ui.components import ServerInfoPrompt, ServerConfigsCollector


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

        server = ServerHandler()
        server.create(server_path, server_version, source, target, assembler_linker_conf)
