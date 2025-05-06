class HelpCommand:
    @staticmethod
    def run(args):
        """Handles 'mcup help [command]' command."""
        if args.command:
            print(f"[TODO] Showing help for command '{args.command}'")
        else:
            print("[TODO] Showing general help")
