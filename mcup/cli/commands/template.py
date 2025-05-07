import os
from pathlib import Path

from mcup.core.handlers.template_handler import TemplateHandler
from mcup.core.status import Status
from mcup.core.utils.locker import LockerManager
from mcup.cli.ui.components import ServerInfoPrompt, ServerConfigsCollector
from mcup.core.utils.path import PathProvider


class TemplateCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup template create <template_name>' command."""
        template_name = args.template_name
        locker = LockerManager()
        path_provider = PathProvider()

        if os.path.exists(f"{path_provider.get_templates_path()}/{template_name}.json"):
            print(f"Error: Template '{template_name}' already exists.")
            return

        try:
            server_info_prompt = ServerInfoPrompt()
            server_type, server_version, source, target, configs = server_info_prompt.get_server_info(locker)
        except Exception as e:
            print(e)
            return

        assembler_linker_conf = ServerConfigsCollector.collect_configurations(server_version, configs)

        template_handler = TemplateHandler()
        template_handler.create_template(template_name, server_type, server_version, source, target,
                                         assembler_linker_conf)




    @staticmethod
    def import_template(args):
        """Handles 'mcup template import <path>' command."""
        path = args.path

        template_handler = TemplateHandler()
        template_handler.import_template(path)

    @staticmethod
    def export_template(args):
        """Handles 'mcup template export <template_name> <destination>' command."""
        template_name = args.template_name
        destination = args.destination

        template_handler = TemplateHandler()
        template_handler.export_template(template_name, destination)

    @staticmethod
    def delete(args):
        """Handles 'mcup template delete <template_name>' command."""
        template_name = args.template_name

        template_handler = TemplateHandler()
        template_handler.delete_template(template_name)

    @staticmethod
    def use(args):
        """Handles 'mcup template use <template_name> [path]' command."""
        template_name = args.template_name
        server_path = Path(args.path)

        template_handler = TemplateHandler()
        template_handler.use_template(template_name, server_path)

    @staticmethod
    def list(args):
        """Handles 'mcup template list' command."""
        template_handler = TemplateHandler()
        template_handler.list_templates()

    @staticmethod
    def refresh(args):
        """Handles 'mcup template refresh' command."""
        template_handler = TemplateHandler()
        template_handler.refresh_template()
