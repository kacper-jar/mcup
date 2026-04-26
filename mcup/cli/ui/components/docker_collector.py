from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInput, CollectorInputType, \
    CollectorInputMode
from mcup.core.utils.version import OLDEST_SUPPORTED_VERSION, INF_VERSION


class DockerCollector(Collector):
    def __init__(self):
        super().__init__("Docker Configuration")

        self.add_section(CollectorSection(
            "General",
            [
                CollectorInput("service-name", "COLLECTOR_DOCKER_SERVICE_NAME", CollectorInputType.STRING,
                               CollectorInputMode.BASIC, OLDEST_SUPPORTED_VERSION, INF_VERSION),
                CollectorInput("container-name", "COLLECTOR_DOCKER_CONTAINER_NAME", CollectorInputType.STRING,
                               CollectorInputMode.BASIC, OLDEST_SUPPORTED_VERSION, INF_VERSION),
            ]
        ))
