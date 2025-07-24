import os
from pathlib import Path

from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from mcup.cli.language import Language
from mcup.cli.ui.components import ServerInfoPrompt, ServerConfigsCollector
from mcup.core.handlers.template_handler import TemplateHandler
from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerUpdater
from mcup.core.utils.path import PathProvider


class TemplateCommand:
    @staticmethod
    def create(args):
        """Handles 'mcup template create <template_name>' command."""
        template_name = args.template_name
        locker = LockerUpdater()
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
        language = Language()
        for status in template_handler.create_template(template_name, server_type, server_version, source, target,
                                                       assembler_linker_conf):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_TEMPLATE_CREATE"))
                case StatusCode.ERROR_TEMPLATE_WRITE_FAILED:
                    print(language.get_string("ERROR_TEMPLATE_WRITE_FAILED", status.status_details))

    @staticmethod
    def import_template(args):
        """Handles 'mcup template import <path>' command."""
        path = args.path

        template_handler = TemplateHandler()
        language = Language()
        for status in template_handler.import_template(path):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_TEMPLATE_IMPORT", path))
                case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                    print(language.get_string("ERROR_TEMPLATE_NOT_FOUND", path))
                case StatusCode.ERROR_TEMPLATE_MISSING_DATA:
                    print(language.get_string("ERROR_TEMPLATE_MISSING_DATA", path))
                case StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT:
                    print(language.get_string("ERROR_TEMPLATE_INVALID_JSON_FORMAT", path))
                case StatusCode.ERROR_TEMPLATE_IMPORT_FAILED:
                    print(language.get_string("ERROR_TEMPLATE_IMPORT_FAILED", path))

    @staticmethod
    def export_template(args):
        """Handles 'mcup template export <template_name> <destination>' command."""
        template_name = args.template_name
        destination = args.destination

        template_handler = TemplateHandler()
        language = Language()
        for status in template_handler.export_template(template_name, destination):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_TEMPLATE_EXPORT", template_name, destination))
                case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                    print(language.get_string("ERROR_TEMPLATE_NOT_FOUND", template_name))
                case StatusCode.ERROR_TEMPLATE_EXPORT_FAILED:
                    print(language.get_string("ERROR_TEMPLATE_EXPORT_FAILED", status.status_details))

    @staticmethod
    def delete(args):
        """Handles 'mcup template delete <template_name>' command."""
        template_name = args.template_name

        template_handler = TemplateHandler()
        language = Language()
        for status in template_handler.delete_template(template_name):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_TEMPLATE_DELETE", template_name))
                case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                    print(language.get_string("ERROR_TEMPLATE_NOT_FOUND", template_name))

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
            language = Language()

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
                        print(language.get_string("INFO_JAVA_MINIMUM_21"))
                    case StatusCode.INFO_JAVA_MINIMUM_17:
                        print(language.get_string("INFO_JAVA_MINIMUM_17"))
                    case StatusCode.INFO_JAVA_MINIMUM_16:
                        print(language.get_string("INFO_JAVA_MINIMUM_16"))
                    case StatusCode.INFO_JAVA_MINIMUM_8:
                        print(language.get_string("INFO_JAVA_MINIMUM_8"))
                    case StatusCode.ERROR_TEMPLATE_NOT_FOUND:
                        print(language.get_string("ERROR_TEMPLATE_NOT_FOUND", template_name))
                    case StatusCode.ERROR_TEMPLATE_MISSING_DATA:
                        print(language.get_string("ERROR_TEMPLATE_MISSING_DATA", template_name))
                    case StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT:
                        print(language.get_string("ERROR_TEMPLATE_INVALID_JSON_FORMAT", template_name))
                    case StatusCode.ERROR_TEMPLATE_READ_FAILED:
                        print(language.get_string("ERROR_TEMPLATE_READ_FAILED", status.status_details))
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
                    case StatusCode.ERROR_SERVER_SOURCE_NOT_SUPPORTED:
                        progress.stop()
                        print(language.get_string("ERROR_SERVER_SOURCE_NOT_SUPPORTED", status.status_details))
                    case StatusCode.SUCCESS:
                        print(language.get_string("SUCCESS_SERVER"))

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
                    print(language.get_string("SUCCESS_TEMPLATE_REFRESH", template_name))
                case StatusCode.INFO_LOCKER_MODIFIED:
                    print(language.get_string("INFO_LOCKER_MODIFIED"))
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
                    print(language.get_string("ERROR_TEMPLATE_NOT_FOUND", template_name))
                case StatusCode.ERROR_TEMPLATE_MISSING_DATA:
                    print(language.get_string("ERROR_TEMPLATE_MISSING_DATA", template_name))
                case StatusCode.ERROR_TEMPLATE_INVALID_JSON_FORMAT:
                    print(language.get_string("ERROR_TEMPLATE_INVALID_JSON_FORMAT", template_name))
                case StatusCode.ERROR_TEMPLATE_REFRESH_FAILED:
                    print(language.get_string("ERROR_TEMPLATE_REFRESH_FAILED", status.status_details))
