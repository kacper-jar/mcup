import argparse
import logging

from mcup import __version__
from mcup.cli.commands import ServerCommand, TemplateCommand, UpdateCommand
from mcup.devtools.confdiff import ConfDiff
from mcup.devtools.locker_mgr import LockerManager


class McupCLI:
    """Command-line interface for the Minecraft server utility program."""

    def __init__(self):
        """Initialize the CLI with all available commands and arguments."""
        self.logger = logging.getLogger(__name__)

        self.DEVTOOLS_ENABLED = True  # temporary variable

        self.parser = argparse.ArgumentParser(
            prog="mcup",
            description="Tool for quickly creating Minecraft servers",
        )
        self.parser.add_argument(
            "-v", "--version", action="version",
            version=f"%(prog)s {__version__}", help="Show the version of mcup"
        )
        self.subparsers = self.parser.add_subparsers(dest="command", help="Available commands")

        self._register_server_commands()
        self._register_template_commands()
        self._register_update_command()
        self._register_devtools_commands()

        self.logger.info("CLI initialized")

    def _register_server_commands(self):
        """Register server-related commands."""
        server_parser = self.subparsers.add_parser("server", help="Create Minecraft servers")
        server_subparsers = server_parser.add_subparsers(dest="action", help="Server actions")

        create_parser = server_subparsers.add_parser("create", help="Create a new server")
        create_parser.add_argument("path", nargs="?", default=".",
                                   help="Path to create the server (default: current directory)")
        create_parser.set_defaults(func=ServerCommand.create)

    def _register_template_commands(self):
        """Register template-related commands."""
        template_parser = self.subparsers.add_parser("template", help="Manage server templates")
        template_subparsers = template_parser.add_subparsers(dest="action", help="Template actions")

        create_parser = template_subparsers.add_parser("create", help="Create a new template")
        create_parser.add_argument("template_name", help="Name of the template to create")
        create_parser.set_defaults(func=TemplateCommand.create)

        import_parser = template_subparsers.add_parser("import", help="Import a template")
        import_parser.add_argument("path", help="Path to the template file to import")
        import_parser.set_defaults(func=TemplateCommand.import_template)

        export_parser = template_subparsers.add_parser("export", help="Export a template")
        export_parser.add_argument("template_name", help="Name of the template to export")
        export_parser.add_argument("destination", help="Destination path for the exported template")
        export_parser.set_defaults(func=TemplateCommand.export_template)

        delete_parser = template_subparsers.add_parser("delete", help="Delete a template")
        delete_parser.add_argument("template_name", help="Name of the template to delete")
        delete_parser.set_defaults(func=TemplateCommand.delete)

        use_parser = template_subparsers.add_parser("use", help="Use a template")
        use_parser.add_argument("template_name", help="Name of the template to use")
        use_parser.add_argument("path", nargs="?", default=".",
                                help="Path to apply the template (default: current directory)")
        use_parser.set_defaults(func=TemplateCommand.use)

        list_parser = template_subparsers.add_parser("list", help="List available templates")
        list_parser.set_defaults(func=TemplateCommand.list)

        refresh_parser = template_subparsers.add_parser("refresh", help="Update download links in a template")
        refresh_parser.add_argument("template_name", help="Name of the template to refresh")
        refresh_parser.set_defaults(func=TemplateCommand.refresh)

    def _register_update_command(self):
        """Register command for updating the locker file."""
        update_parser = self.subparsers.add_parser("update", help="Manually update the locker file")
        update_parser.set_defaults(func=UpdateCommand.run)

    def _register_devtools_commands(self):
        """Register devtools commands."""
        if self.DEVTOOLS_ENABLED:
            devtools_parser = self.subparsers.add_parser("devtools", help="Developer tools")
            devtools_subparsers = devtools_parser.add_subparsers(dest="action", help="Devtools actions")

            confdiff_parser = devtools_subparsers.add_parser("confdiff", help="Compare configuration files")
            confdiff_parser.add_argument("configuration_files", help="Configuration files with version"
                                         " formatted like this: VERSION:PATH", nargs="+")
            confdiff_parser.set_defaults(func=ConfDiff.run)

            locker_mgr_parser = devtools_subparsers.add_parser("lockermgr", help="Manage the locker file")
            locker_mgr_subparsers = locker_mgr_parser.add_subparsers(dest="locker_action", help="Locker actions")

            init_locker_parser = locker_mgr_subparsers.add_parser("init", help="Initialize locker file")
            init_locker_parser.set_defaults(func=LockerManager.initialize_locker)

            add_server_parser = locker_mgr_subparsers.add_parser("add-server", help="Add a new server type")
            add_server_parser.add_argument("server_type", help="Type of server to add")
            add_server_parser.set_defaults(func=LockerManager.add_server)

            add_version_parser = locker_mgr_subparsers.add_parser("add-version", help="Add a new version to a server type")
            add_version_parser.add_argument("server_type", help="Type of server")
            add_version_parser.add_argument("version", help="Version to add")
            add_version_parser.add_argument("source", help="Source type (DOWNLOAD or BUILDTOOLS)")
            add_version_parser.add_argument("url_target", help="URL for DOWNLOAD or target for BUILDTOOLS")
            add_version_parser.add_argument("supports_plugins", help="Whether the version supports plugins (true/false)")
            add_version_parser.add_argument("supports_mods", help="Whether the version supports mods (true/false)")
            add_version_parser.add_argument("third_party_warning", help="Whether to show 3rd party warning (true/false)")
            add_version_parser.add_argument("--configs", nargs="*", help="Configuration files for the version")
            add_version_parser.set_defaults(func=LockerManager.add_version)

            update_version_parser = locker_mgr_subparsers.add_parser("update-version", help="Update a version's URL")
            update_version_parser.add_argument("server_type", help="Type of server")
            update_version_parser.add_argument("version", help="Version to update")
            update_version_parser.add_argument("url", help="New URL for the version")
            update_version_parser.set_defaults(func=LockerManager.update_version)

            remove_version_parser = locker_mgr_subparsers.add_parser("remove-version", help="Remove a version from a server type")
            remove_version_parser.add_argument("server_type", help="Type of server")
            remove_version_parser.add_argument("version", help="Version to remove")
            remove_version_parser.set_defaults(func=LockerManager.remove_version)

            list_locker_parser = locker_mgr_subparsers.add_parser("list", help="List all server types and versions")
            list_locker_parser.set_defaults(func=LockerManager.list_locker)

    def run(self):
        """Parse and execute the given command."""
        args = self.parser.parse_args()
        command_str = getattr(args, "command", "")
        action_str = getattr(args, "action", "")
        self.logger.info(f"Executing command: {command_str} {action_str}".strip())
        if hasattr(args, "func"):
            args.func(args)
        else:
            self.parser.print_help()
            self.logger.info("Unknown command, printing help message.")
