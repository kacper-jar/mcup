from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.core.utils.version import OLDEST_SUPPORTED_VERSION, LATEST_VERSION


class StartScriptCollector(Collector):
    def __init__(self):
        super().__init__("Start Script")

        self.add_section(CollectorSection(
            "Configuration",
            [
                CollectorInput("screen-name", "COLLECTOR_START_SCRIPT_SCREEN_NAME", CollectorInputType.STRING,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
                CollectorInput("initial-heap", "COLLECTOR_START_SCRIPT_SCREEN_NAME", CollectorInputType.INT,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
                CollectorInput("max-heap", "COLLECTOR_START_SCRIPT_MAX_HEAP", CollectorInputType.INT,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
            ]
        ))
        self.add_section(CollectorSection(
            "Auto-Restart",
            [
                CollectorInput("max-restarts", "COLLECTOR_START_SCRIPT_MAX_RESTARTS",
                               CollectorInputType.INT, OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
                CollectorInput("restart-delay", "COLLECTOR_START_SCRIPT_RESTART_DELAY",
                               CollectorInputType.INT, OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
            ]
        ))
