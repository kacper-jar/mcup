from mcup.core.user_config import UserConfig


class ConfigCommand:
    @staticmethod
    def get(args):
        """Handles 'mcup config get <key>' command."""
        user_config = UserConfig()

        output = user_config.get_configuration(args.key)

        if output is None:
            print("no value found for key")
            return
        else:
            print(output)

    @staticmethod
    def set(args):
        """Handles 'mcup config set <key> <value>' command."""
        user_config = UserConfig()

        user_config.set_configuration(args.key, args.value)
