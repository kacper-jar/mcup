import os
from pathlib import Path
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from mcup.cli.language import Language
from mcup.cli.ui.components import ServerInfoPrompt, ServerConfigsCollector
from mcup.core.handlers.template_handler import TemplateHandler
from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerManager
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
        for status in template_handler.create_template(template_name, server_type, server_version, source, target,
                                                       assembler_linker_conf):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(f"Template '{template_name}' created successfully.")
                case StatusCode.ERROR_TEMPLATE_WRITE_FAILED:
                    print(f"Error: Failed to write template file. Details: {status.status_details}")

    @staticmethod
    def import_template(args):
        """Handles 'mcup template import <path>' command."""
        path = args.path

        template_handler = TemplateHandler()
        for status in template_handler.import_template(path):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(f"Template imported successfully from '{path}'.")
                case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                    print(f"Error: Template file not found at path: {path}")
                case StatusCode.ERROR_TEMPLATE_MISSING_DATA:
                    print(f"Error: Missing data inside template file at path: {path}")
                case StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT:
                    print(f"Error: Invalid JSON format in template file at path: {path}")
                case StatusCode.ERROR_TEMPLATE_IMPORT_FAILED:
                    print(f"Error importing template: {status.status_details}")

    @staticmethod
    def export_template(args):
        """Handles 'mcup template export <template_name> <destination>' command."""
        template_name = args.template_name
        destination = args.destination

        template_handler = TemplateHandler()
        for status in template_handler.export_template(template_name, destination):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(f"Template '{template_name}' exported successfully to '{destination}'.")
                case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                    print(f"Error: Template '{template_name}' not found.")
                case StatusCode.ERROR_TEMPLATE_EXPORT_FAILED:
                    print(f"Error exporting template: {status.status_details}")

    @staticmethod
    def delete(args):
        """Handles 'mcup template delete <template_name>' command."""
        template_name = args.template_name

        template_handler = TemplateHandler()
        for status in template_handler.delete_template(template_name):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(f"Template '{template_name}' deleted successfully.")
                case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                    print(f"Error: Template '{template_name}' not found.")

    @staticmethod
    def use(args):
        """Handles 'mcup template use <template_name> [path]' command."""
        template_name = args.template_name
        server_path = Path(args.path)

        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
        ) as progress:
            template_handler = TemplateHandler()
            task = None

            for status in template_handler.use_template(template_name, server_path):
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
                        print("Minecraft 1.20.6 and above require at least JDK 21. BuildTools may fail. "
                              "(Azul Zulu JDK is recommended.)")
                    case StatusCode.INFO_JAVA_MINIMUM_17:
                        print("Minecraft 1.17.1 and above require at least JDK 17. BuildTools may fail. "
                              "(Azul Zulu JDK is recommended.)")
                    case StatusCode.INFO_JAVA_MINIMUM_16:
                        print("Minecraft 1.17 and 1.17.1 require at least JDK 16. BuildTools may fail. "
                              "(Azul Zulu JDK is recommended.)")
                    case StatusCode.INFO_JAVA_MINIMUM_8:
                        print("Minecraft versions below 1.17 require at least JDK 8. BuildTools may fail. "
                              "(Azul Zulu JDK is recommended.")
                    case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                        print(f"Error: Template '{template_name}' not found.")
                    case StatusCode.ERROR_TEMPLATE_MISSING_DATA:
                        print(f"Error: Missing data inside template file at path: {status.status_details}")
                    case StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT:
                        print(f"Error: Invalid JSON format in template file at path: {status.status_details}")
                    case StatusCode.ERROR_TEMPLATE_READ_FAILED:
                        print(f"Error reading template: {str(status.status_details)}")
                    case StatusCode.ERROR_DOWNLOAD_SERVER_FAILED:
                        progress.stop()
                        print(f"Failed to download server. HTTP {status.status_details}")
                    case StatusCode.ERROR_DOWNLOAD_BUILDTOOLS_FAILED:
                        progress.stop()
                        print(f"Failed to download Spigot BuildTools. HTTP {status.status_details}")
                    case StatusCode.ERROR_BUILD_TOOLS_NOT_FOUND:
                        progress.stop()
                        print("Spigot BuildTools not found.")
                    case StatusCode.ERROR_SERVER_JAR_NOT_FOUND:
                        progress.stop()
                        print("Server JAR file not found. Check BuildTools.log.txt in server folder for more info.")
                    case StatusCode.SUCCESS:
                        print("Server created successfully.")

    @staticmethod
    def list(args):
        """Handles 'mcup template list' command."""
        template_handler = TemplateHandler()
        for status in template_handler.list_templates():
            for template in status.status_details:
                print(template)

    @staticmethod
    def refresh(args):
        """Handles 'mcup template refresh' command."""
        template_name = args.template_name

        language = Language()
        template_handler = TemplateHandler()
        for status in template_handler.refresh_template(template_name):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(f"Template refreshed successfully.")
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
                case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                    print(f"Error: Template file not found: {status.status_details}")
                case StatusCode.ERROR_TEMPLATE_MISSING_DATA:
                    print(f"Error: Missing data inside template file: {status.status_details}")
                case StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT:
                    print(f"Error: Invalid JSON format in template file: {status.status_details}")
                case StatusCode.ERROR_TEMPLATE_REFRESH_FAILED:
                    print(f"Error refreshing template: {status.status_details}")
