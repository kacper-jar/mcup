from datetime import datetime
import logging
import os

from mcup import __version__
from mcup.cli import McupCLI
from mcup.core.utils.path import PathProvider
from mcup.core.user_config import UserConfig
from mcup.core.status import StatusCode


def _resolve_log_level(value):
    try:
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            v = value.strip().upper()
            if v.isdigit():
                return int(v)
            mapping = {
                'CRITICAL': logging.CRITICAL,
                'FATAL': logging.FATAL,
                'ERROR': logging.ERROR,
                'WARNING': logging.WARNING,
                'WARN': logging.WARNING,
                'INFO': logging.INFO,
                'DEBUG': logging.DEBUG,
                'NOTSET': logging.NOTSET,
            }
            return mapping.get(v, logging.INFO)
    except Exception:
        pass
    return logging.INFO


def main():
    """Entry point for the application when run with 'python -m mcup'."""
    path_provider = PathProvider()

    user_config = UserConfig()
    resolved_level = logging.INFO
    for status in user_config.get_configuration('logging.level', 'INFO'):
        if status.status_code == StatusCode.SUCCESS:
            resolved_level = _resolve_log_level(status.status_details)

    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    log_file = os.path.join(path_provider.get_logs_path(), log_filename)
    if not os.path.exists(path_provider.get_logs_path()):
        os.makedirs(path_provider.get_logs_path())
    logging.basicConfig(
        level=resolved_level,
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
