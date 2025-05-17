class Language:
    strings = {
        # Server
        "INFO_JAVA_MINIMUM_21": "Minecraft 1.20.6 and above require at least JDK 21. BuildTools may fail. "
                                "(Azul Zulu JDK is recommended.)",
        "INFO_JAVA_MINIMUM_17": "Minecraft 1.17.1 and above require at least JDK 17. BuildTools may fail. "
                                "(Azul Zulu JDK is recommended.)",
        "INFO_JAVA_MINIMUM_16": "Minecraft 1.17 and 1.17.1 require at least JDK 16. BuildTools may fail. "
                                "(Azul Zulu JDK is recommended.)",
        "INFO_JAVA_MINIMUM_8": "Minecraft versions below 1.17 require at least JDK 8. BuildTools may fail. "
                               "(Azul Zulu JDK is recommended.",
        "ERROR_DOWNLOAD_SERVER_FAILED": "Failed to download server. HTTP {}",
        "ERROR_DOWNLOAD_BUILDTOOLS_FAILED": "Failed to download Spigot BuildTools. HTTP {}",
        "ERROR_BUILD_TOOLS_NOT_FOUND": "Spigot BuildTools not found.",
        "ERROR_SERVER_JAR_NOT_FOUND": "Server JAR file not found. "
                                      "Check BuildTools.log.txt in server folder for more info.",
        "SUCCESS_SERVER": "Server created successfully.",

        # Template
        "ERROR_TEMPLATE_WRITE_FAILED": "Failed to write template file. Details: {}",
        "ERROR_TEMPLATE_READ_FAILED": "Failed to read template file. Details: {}",
        "ERROR_TEMPLATE_NOT_FOUND": "Template not found: {}",
        "ERROR_TEMPLATE_MISSING_DATA": "Missing data inside template file: {}",
        "ERROR_TEMPLATE_INVALID_JSON_FORMAT": "Invalid JSON format in template file: {}",
        "ERROR_TEMPLATE_IMPORT_FAILED": "Error importing template: {}",
        "ERROR_TEMPLATE_EXPORT_FAILED": "Error exporting template: {}",
        "ERROR_TEMPLATE_REFRESH_FAILED": "Error refreshing template: {}",
        "SUCCESS_TEMPLATE_CREATE": "Template '{}' created successfully.",
        "SUCCESS_TEMPLATE_IMPORT": "Template imported successfully from {}.",
        "SUCCESS_TEMPLATE_EXPORT": "Template '{}' exported successfully to {}.",
        "SUCCESS_TEMPLATE_DELETE": "Template '{}' deleted successfully.",
        "SUCCESS_TEMPLATE_REFRESH": "Template '{}' refreshed successfully.",

        # Locker
        "INFO_LOCKER_UP_TO_DATE": "Locker file is already up-to-date.",
        "INFO_LOCKER_UPDATING": "Updating locker file...",
        "ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED": "Could not retrieve the latest update timestamp. Details: {}",
        "ERROR_LOCKER_META_READ_FAILED": "Error reading locker meta file. Details: {}",
        "ERROR_LOCKER_DOWNLOAD_FAILED": "Error downloading locker file. Details: {}",
        "ERROR_LOCKER_META_UPDATE_FAILED": "Error updating locker meta file. Details: {}",
        "SUCCESS_LOCKER": "Successfully updated locker file."
    }

    def get_string(self, key, *args):
        if args is not None:
            return self.strings.get(key, key).format(*args)
        return self.strings.get(key, key)
