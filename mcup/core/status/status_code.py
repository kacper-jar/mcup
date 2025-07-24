import enum


class StatusCode(enum.Enum):
    """Class representing status code."""
    SUCCESS = enum.auto()

    IN_PROGRESS = enum.auto()

    PROGRESSBAR_UPDATE = enum.auto()
    PROGRESSBAR_NEXT = enum.auto()
    PROGRESSBAR_FINISH_TASK = enum.auto()
    PROGRESSBAR_END = enum.auto()

    INFO_JAVA_MINIMUM_21 = enum.auto()
    INFO_JAVA_MINIMUM_17 = enum.auto()
    INFO_JAVA_MINIMUM_16 = enum.auto()
    INFO_JAVA_MINIMUM_8 = enum.auto()
    INFO_LOCKER_MODIFIED = enum.auto()
    INFO_LOCKER_UP_TO_DATE = enum.auto()
    INFO_LOCKER_UPDATING = enum.auto()

    ERROR_GENERIC = enum.auto()
    ERROR_DOWNLOAD_SERVER_FAILED = enum.auto()
    ERROR_DOWNLOAD_BUILDTOOLS_FAILED = enum.auto()
    ERROR_BUILD_TOOLS_NOT_FOUND = enum.auto()
    ERROR_SERVER_JAR_NOT_FOUND = enum.auto()
    ERROR_SERVER_SOURCE_NOT_SUPPORTED = enum.auto()
    ERROR_TEMPLATE_WRITE_FAILED = enum.auto()
    ERROR_TEMPLATE_NOT_FOUND = enum.auto()
    ERROR_TEMPLATE_MISSING_DATA = enum.auto()
    ERROR_TEMPLATE_INVALID_JSON_FORMAT = enum.auto()
    ERROR_TEMPLATE_READ_FAILED = enum.auto()
    ERROR_TEMPLATE_EXPORT_FAILED = enum.auto()
    ERROR_TEMPLATE_IMPORT_FAILED = enum.auto()
    ERROR_TEMPLATE_REFRESH_FAILED = enum.auto()
    ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED = enum.auto()
    ERROR_LOCKER_META_READ_FAILED = enum.auto()
    ERROR_LOCKER_META_UPDATE_FAILED = enum.auto()
    ERROR_LOCKER_DOWNLOAD_FAILED = enum.auto()
