import enum


class ServerConfigsCollectorFlags(enum.Enum):
    """Class representing server configs collector flags."""
    NONE = enum.auto()
    NO_CONFIGS = enum.auto()
    ALL_DEFAULTS = enum.auto()
