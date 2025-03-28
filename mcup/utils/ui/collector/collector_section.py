from dataclasses import dataclass

from mcup.utils.ui.collector import CollectorInput


@dataclass
class CollectorSection:
    inputs: list[CollectorInput]
