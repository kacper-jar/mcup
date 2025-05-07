import enum


class StatusCode(enum.Enum):
    """Class representing status code."""
    SUCCESS = enum.auto()

    IN_PROGRESS = enum.auto()

    PROGRESSBAR_UPDATE = enum.auto()
    PROGRESSBAR_NEXT = enum.auto()
    PROGRESSBAR_FINISH_TASK = enum.auto()
    PROGRESSBAR_END = enum.auto()

    ERROR_GENERIC = enum.auto()
    ERROR_DOWNLOAD_SERVER_FAILED = enum.auto()
    ERROR_DOWNLOAD_BUILDTOOLS_FAILED = enum.auto()
    ERROR_BUILD_TOOLS_NOT_FOUND = enum.auto()
    ERROR_SERVER_JAR_NOT_FOUND = enum.auto()

    PRINT_INFO = enum.auto()
