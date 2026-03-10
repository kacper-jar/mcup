import enum


class CollectorInputType(enum.Enum):
    """Class representing collector input type."""
    STRING = enum.auto()
    INT = enum.auto()
    STRING_OR_INT = enum.auto()
    FLOAT = enum.auto()
    BOOL = enum.auto()
    STRING_LIST = enum.auto()
    INT_LIST = enum.auto()
    FLOAT_LIST = enum.auto()
    BOOL_LIST = enum.auto()

    # Specific server-related input types
    PAPER_OBFUSCATION_MODEL_OVERRIDES = enum.auto()
    PAPER_PACKET_LIMITER_OVERRIDES = enum.auto()
    PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_ENTITY_TYPE = enum.auto()
    PAPER_DOOR_BREAKING_DIFFICULTY_ENTITY_TYPE = enum.auto()
    PAPER_ALT_ITEM_DESPAWN_RATE_ITEM_TYPE = enum.auto()
