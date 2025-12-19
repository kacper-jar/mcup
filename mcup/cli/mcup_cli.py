import argparse
import logging

from mcup import __version__
from mcup.cli.commands import ServerCommand, TemplateCommand, UpdateCommand, ConfigCommand, AboutCommand
from mcup.core.status import StatusCode
from mcup.core.user_config import UserConfig
from mcup.devtools.confdiff import ConfDiff
from mcup.devtools.locker_mgr import LockerManager


class McupCLI:
    """Command-line interface for the Minecraft server utility program."""

    def __init__(self):
        """Initialize the CLI with all available commands and arguments."""
        self.logger = logging.getLogger(__name__)

        try:
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
            self._register_config_commands()
            self._register_about_command()
            self._register_devtools_commands()

            self.logger.info("CLI initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize CLI: {e}")
            raise

    def _register_server_commands(self):
        """Register server-related commands."""
        server_parser = self.subparsers.add_parser("server", help="Create Minecraft servers")
        server_subparsers = server_parser.add_subparsers(dest="action", help="Server actions")

        create_parser = server_subparsers.add_parser("create", help="Create a new server")
        create_parser.add_argument("server_type", help="Type of server")
        create_parser.add_argument("server_version", help="Version of server")
        create_parser.add_argument("path", nargs="?", default=".",
                                   help="Path to create the server (default: current directory)")
        configs_group = create_parser.add_mutually_exclusive_group()
        configs_group.add_argument("--no-configs", action="store_true",
                                   help="Skip generation of configuration files")
        configs_group.add_argument("--no-defaults", action="store_true",
                                   help="Prompt for all configuration values")
        configs_group.add_argument("--all-defaults", action="store_true",
                                   help="Use default configuration values for all configuration files")
        create_parser.add_argument("--skip-java-check", action="store_true",
                                   help="Skip Java installation and version checks")
        create_parser.set_defaults(func=ServerCommand.create)

        list_parser = server_subparsers.add_parser("list", help="List available server types and versions")
        list_parser.set_defaults(func=ServerCommand.list)

    def _register_template_commands(self):
        """Register template-related commands."""
        template_parser = self.subparsers.add_parser("template", help="Manage server templates")
        template_subparsers = template_parser.add_subparsers(dest="action", help="Template actions")

        create_parser = template_subparsers.add_parser("create", help="Create a new template")
        create_parser.add_argument("server_type", help="Type of server")
        create_parser.add_argument("server_version", help="Version of server")
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
        update_parser.add_argument("--force", action="store_true", help="Force update the locker file even if it's up to date")
        update_parser.set_defaults(func=UpdateCommand.run)

    def _register_config_commands(self):
        """Register configuration-related commands."""
        config_parser = self.subparsers.add_parser("config", help="Manage mcup configuration")
        config_subparsers = config_parser.add_subparsers(dest="action", help="Configuration actions")

        get_parser = config_subparsers.add_parser("get", help="Get a configuration value")
        get_parser.add_argument("key", help="Name of the configuration property")
        get_parser.set_defaults(func=ConfigCommand.get)

        set_parser = config_subparsers.add_parser("set", help="Set a configuration value")
        set_parser.add_argument("key", help="Name of the configuration property")
        set_parser.add_argument("value", help="Value of the configuration property")
        set_parser.set_defaults(func=ConfigCommand.set)

        remove_parser = config_subparsers.add_parser("remove", help="Remove a configuration value")
        remove_parser.add_argument("key", help="Name of the configuration property")
        remove_parser.set_defaults(func=ConfigCommand.remove)

        clear_parser = config_subparsers.add_parser("clear", help="Clear all configuration values")
        clear_parser.set_defaults(func=ConfigCommand.clear)

        list_parser = config_subparsers.add_parser("list", help="List all configuration keys and values")
        list_parser.set_defaults(func=ConfigCommand.list)

    def _register_about_command(self):
        """Register about command."""
        about_parser = self.subparsers.add_parser("about", help="About mcup")
        about_parser.set_defaults(func=AboutCommand.run)

    def _register_devtools_commands(self):
        """Register devtools commands."""
        user_config = UserConfig()

        for status in user_config.get_configuration("devtools.enabled", default="false"):
            if status.status_code == StatusCode.SUCCESS:
                devtools_enabled = str(status.status_details).lower()
                logging.info(f"Devtools enabled.")
                break
            else:
                devtools_enabled = "false"
                logging.info(f"Devtools disabled. Use 'mcup config set devtools.enabled true' to enable.")
                break

        if devtools_enabled == "true":
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
            source_group = add_version_parser.add_mutually_exclusive_group(required=True)
            source_group.add_argument("--server-url", help="Direct download URL for server jar (DOWNLOAD source)")
            source_group.add_argument("--installer-url", help="URL for installer jar (INSTALLER source)")
            add_version_parser.add_argument("--installer-args", nargs=argparse.REMAINDER, help="Arguments for installer jar (INSTALLER source only). Use '--' before these to separate from mcup flags.")
            add_version_parser.add_argument("--supports-plugins", action="store_true", help="Mark server as supporting plugins")
            add_version_parser.add_argument("--supports-mods", action="store_true", help="Mark server as supporting mods")
            add_version_parser.add_argument("--configs", nargs="*", default=[], help="Config files associated with this server")
            add_version_parser.add_argument("--cleanup", nargs="*", default=[], help="Files to clean up after install")
            add_version_parser.set_defaults(func=LockerManager.add_version)

            update_version_parser = locker_mgr_subparsers.add_parser("update-version", help="Update a version's URL")
            update_version_parser.add_argument("server_type", help="Type of server")
            update_version_parser.add_argument("version", help="Version to update")
            update_version_parser.add_argument("--server-url", default=None,
                                               help="Direct download URL for server jar (DOWNLOAD source)")
            update_version_parser.add_argument("--installer-url", default=None,
                                               help="URL for installer jar (INSTALLER source)")
            update_version_parser.add_argument("--installer-args", default=None, nargs=argparse.REMAINDER,
                                               help="Arguments for installer jar (INSTALLER source only). Use '--' before these to separate from mcup flags.")
            update_version_parser.add_argument("--supports-plugins", default=None,
                                               help="Mark server as supporting plugins (true/false)")
            update_version_parser.add_argument("--supports-mods", default=None,
                                               help="Mark server as supporting mods (true/false)")
            update_version_parser.add_argument("--configs", nargs="*", default=None,
                                               help="Config files associated with this server")
            update_version_parser.add_argument("--cleanup", nargs="*", default=None,
                                               help="Files to clean up after install")
            update_version_parser.set_defaults(func=LockerManager.update_version)

            remove_version_parser = locker_mgr_subparsers.add_parser("remove-version", help="Remove a version from a server type")
            remove_version_parser.add_argument("server_type", help="Type of server")
            remove_version_parser.add_argument("version", help="Version to remove")
            remove_version_parser.set_defaults(func=LockerManager.remove_version)

            list_locker_parser = locker_mgr_subparsers.add_parser("list", help="List all server types and versions")
            list_locker_parser.set_defaults(func=LockerManager.list_locker)

            export_locker_parser = locker_mgr_subparsers.add_parser("export", help="Export the locker file")
            export_locker_parser.add_argument("destination", help="Destination path for the exported locker file")
            export_locker_parser.set_defaults(func=LockerManager.export_locker)

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
