import enum


class CollectorInputType(enum.Enum):
    """Class representing collector input type."""
    STRING = enum.auto()
    INT = enum.auto()
    FLOAT = enum.auto()
    BOOL = enum.auto()
    STRING_LIST = enum.auto()
    INT_LIST = enum.auto()
    FLOAT_LIST = enum.auto()
    BOOL_LIST = enum.auto()
