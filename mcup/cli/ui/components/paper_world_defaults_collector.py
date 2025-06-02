from mcup.cli.ui.elements.collector import Collector, CollectorSection, CollectorInputType, CollectorInput


class PaperWorldDefaultsCollector(Collector):
    def __init__(self):
        super().__init__()

        self.add_section(CollectorSection(
            "Paper (World Defaults) - Anticheat",
            [
                CollectorInput("anticheat/enabled", "", CollectorInputType.BOOL,)
            ]
        ))
