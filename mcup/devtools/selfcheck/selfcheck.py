import sys
import subprocess
import tempfile
import os
import logging
from pathlib import Path


class SelfCheck:
    """Provides simple functional testing for mcup before release to avoid regressions."""

    @staticmethod
    def run(args):
        logger = logging.getLogger(__name__)
        logger.info("Starting mcup selfcheck...")

        if getattr(sys, 'frozen', False):
            base_cmd = [sys.executable]
        else:
            base_cmd = [sys.executable, "-m", "mcup"]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            command = base_cmd + [
                "server",
                "create",
                "paper",
                "1.20.4",
                str(temp_path),
                "--all-defaults",
                "--skip-java-check"
            ]

            logger.info(f"Executing subsystem call: {' '.join(command)}")
            try:
                result = subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                logger.error(f"Functional subsystem test failed with exit code {e.returncode}")
                sys.exit(1)

            logger.info("Verifying generated filesystem artifacts...")
            expected_files = [
                "server.properties",
                "eula.txt"
            ]

            missing_files = []
            for file_name in expected_files:
                target = temp_path / file_name
                if not target.exists():
                    missing_files.append(file_name)

            if not list(temp_path.glob("*.jar")):
                missing_files.append("server.jar (or dynamic equivalent)")

            if missing_files:
                logger.error(f"Selfcheck failed! Missing expected files: {', '.join(missing_files)}")
                sys.exit(1)

            start_bat = temp_path / "start.bat"
            start_sh = temp_path / "start.sh"

            if os.name == 'nt' and not start_bat.exists():
                logger.error("Selfcheck failed! start.bat is missing on a Windows target.")
                sys.exit(1)
            elif os.name != 'nt' and not start_sh.exists():
                logger.error("Selfcheck failed! start.sh is missing on a Unix target.")
                sys.exit(1)

            logger.info("All assertions passed! mcup looks to function exactly as intended.")
            sys.exit(0)
