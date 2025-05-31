from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType
from mcup.core.utils.version import OLDEST_SUPPORTED_VERSION, LATEST_VERSION


class StartScriptCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Start Script Configuration",
            [
                CollectorInput("screen-name", "Screen name", CollectorInputType.STRING,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
                CollectorInput("initial-heap", "Initial heap size (in MB)", CollectorInputType.INT,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
                CollectorInput("max-heap", "Maximum heap size (in MB)", CollectorInputType.INT,
                               OLDEST_SUPPORTED_VERSION, LATEST_VERSION),
            ]
        ))
