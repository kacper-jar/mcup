from mcup.cli.language import Language
from mcup.core.user_config import UserConfig


class ConfigCommand:
    @staticmethod
    def get(args):
        """Handles 'mcup config get <key>' command."""
        language = Language()
        user_config = UserConfig()

        output = user_config.get_configuration(args.key)

        if output is None:
            print(language.get_string("CONFIG_GET_NO_VALUE", args.key))
        else:
            print(language.get_string("CONFIG_GET_VALUE", args.key, output))

    @staticmethod
    def set(args):
        """Handles 'mcup config set <key> <value>' command."""
        language = Language()
        user_config = UserConfig()

        user_config.set_configuration(args.key, args.value)

        print(language.get_string("CONFIG_SET_VALUE", args.key, args.value))
