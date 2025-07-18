from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.core.utils.version import OLDEST_SUPPORTED_VERSION, LATEST_VERSION


class StartScriptCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Start Script Configuration",
            [
                CollectorInput("screen-name", "COLLECTOR_START_SCRIPT_SCREEN_NAME", CollectorInputType.STRING,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
                CollectorInput("initial-heap", "COLLECTOR_START_SCRIPT_SCREEN_NAME", CollectorInputType.INT,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
                CollectorInput("max-heap", "COLLECTOR_START_SCRIPT_MAX_HEAP", CollectorInputType.INT,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
            ]
        ))
