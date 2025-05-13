from datetime import datetime
import logging
import os

from mcup import __version__
from mcup.cli import McupCLI
from mcup.core.utils.path import PathProvider


def main():
    """Entry point for the application when run with 'python -m mcup'."""
    path_provider = PathProvider()

    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    log_file = os.path.join(path_provider.get_logs_path(), log_filename)
    if not os.path.exists(path_provider.get_logs_path()):
        os.makedirs(path_provider.get_logs_path())
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
        handlers=[
            logging.FileHandler(log_file),
        ]
    )
    logger = logging.getLogger(__name__)
    logger.info("Logger initialized")

    logger.info(f"Starting Mcup CLI (mcup {__version__})")

    cli = McupCLI()
    cli.run()


if __name__ == "__main__":
    main()
