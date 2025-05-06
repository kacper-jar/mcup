import argparse
from mcup import __version__
from mcup.commands import ServerCommand, TemplateCommand, UpdateCommand, HelpCommand


class McupCLI:
    """Command-line interface for the Minecraft server utility program."""

    def __init__(self):
        """Initialize the CLI with all available commands and arguments."""
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
        self._register_help_command()

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

    def _register_help_command(self):
        """Register help command."""
        help_parser = self.subparsers.add_parser("help", help="Show help for a specific command")
        help_parser.add_argument("command", nargs="?", help="Command to show help for")
        help_parser.set_defaults(func=HelpCommand.run)

    def run(self):
        """Parse and execute the given command."""
        args = self.parser.parse_args()
        if hasattr(args, "func"):
            args.func(args)
        else:
            self.parser.print_help()
