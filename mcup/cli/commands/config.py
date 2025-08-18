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
                    print(language.get_string("CONFIG_GET_VALUE", args.key, status.status_details))
                case StatusCode.ERROR_CONFIG_KEY_NOT_FOUND:
                    print(language.get_string("CONFIG_GET_NO_VALUE", args.key))
                case StatusCode.ERROR_CONFIG_READ_FAILED:
                    print(language.get_string("ERROR_CONFIG_READ_FAILED", status.status_details))

    @staticmethod
    def set(args):
        """Handles 'mcup config set <key> <value>' command."""
        language = Language()
        user_config = UserConfig()

        for status in user_config.set_configuration(args.key, args.value):
            match status.status_code:
                case StatusCode.SUCCESS:
                    print(language.get_string("CONFIG_SET_VALUE", args.key, args.value))
                case StatusCode.ERROR_CONFIG_SET_FAILED:
                    print(language.get_string("ERROR_CONFIG_SET_FAILED", status.status_details))
                case StatusCode.ERROR_CONFIG_SAVE_FAILED:
                    print(language.get_string("ERROR_CONFIG_SAVE_FAILED", status.status_details))
