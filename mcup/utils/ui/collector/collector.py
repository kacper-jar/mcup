from mcup.utils.ui.collector import CollectorSection


class Collector:
    """Class representing Collector, which will collect data for configuration via CLI"""
    def __init__(self):
        self.sections: list[CollectorSection] = []


    def start_collector(self):
        """Function for collecting user input into configuration."""
        pass
