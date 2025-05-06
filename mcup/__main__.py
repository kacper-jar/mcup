from mcup.cli import McupCLI


def main():
    """Entry point for the application when run with 'python -m mcup'."""
    cli = McupCLI()
    cli.run()


if __name__ == "__main__":
    main()
