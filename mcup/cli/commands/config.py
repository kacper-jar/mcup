from mcup.cli.language import Language
from mcup.core.status import StatusCode
from mcup.core.user_config import UserConfig


class ConfigCommand:
    @staticmethod
    def get(args):
        """Handles 'mcup config get <key>' command."""
        language = Language()
        user_config = UserConfig()

        for status in user_config.get_configuration(args.key):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_USERCONFIG_GET_VALUE", args.key, status.status_details))
                case StatusCode.ERROR_USERCONFIG_KEY_NOT_FOUND:
                    print(language.get_string("SUCCESS_USERCONFIG_GET_NO_VALUE", args.key))
                case StatusCode.ERROR_USERCONFIG_READ_FAILED:
                    print(language.get_string("ERROR_USERCONFIG_READ_FAILED", status.status_details))

    @staticmethod
    def set(args):
        """Handles 'mcup config set <key> <value>' command."""
        language = Language()
        user_config = UserConfig()

        for status in user_config.set_configuration(args.key, args.value):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_USERCONFIG_SET_VALUE", args.key, args.value))
                case StatusCode.ERROR_USERCONFIG_SET_FAILED:
                    print(language.get_string("ERROR_USERCONFIG_SET_FAILED", status.status_details))
                case StatusCode.ERROR_USERCONFIG_SAVE_FAILED:
                    print(language.get_string("ERROR_USERCONFIG_SAVE_FAILED", status.status_details))

    @staticmethod
    def remove(args):
        """Handles 'mcup config remove <key>' command."""
        language = Language()
        user_config = UserConfig()

        for status in user_config.remove_configuration(args.key):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_USERCONFIG_REMOVE", args.key))
                case StatusCode.ERROR_USERCONFIG_KEY_NOT_FOUND:
                    print(language.get_string("ERROR_USERCONFIG_KEY_NOT_FOUND", args.key))
                case StatusCode.ERROR_USERCONFIG_REMOVE_FAILED:
                    print(language.get_string("ERROR_USERCONFIG_REMOVE_FAILED", status.status_details))
                case StatusCode.ERROR_USERCONFIG_SAVE_FAILED:
                    print(language.get_string("ERROR_USERCONFIG_SAVE_FAILED", status.status_details))

    @staticmethod
    def clear(args):
        """Handles 'mcup config clear' command."""
        language = Language()
        user_config = UserConfig()

        for status in user_config.clear_configuration():
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("SUCCESS_USERCONFIG_CLEAR"))
                case StatusCode.ERROR_USERCONFIG_CLEAR_FAILED:
                    print(language.get_string("ERROR_USERCONFIG_CLEAR_FAILED", status.status_details))
                case StatusCode.ERROR_USERCONFIG_FILE_NOT_FOUND:
                    print(language.get_string("ERROR_USERCONFIG_FILE_NOT_FOUND"))

    @staticmethod
    def list(args):
        """Handles 'mcup config list' command."""
        language = Language()
        user_config = UserConfig()

        for status in user_config.list_configuration():
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(status.status_details)
                case StatusCode.ERROR_USERCONFIG_LIST_FAILED:
                    print(language.get_string("ERROR_USERCONFIG_LIST_FAILED", status.status_details))
                case StatusCode.ERROR_USERCONFIG_READ_FAILED:
                    print(language.get_string("ERROR_USERCONFIG_READ_FAILED", status.status_details))
