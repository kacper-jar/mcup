from mcup.cli.language import Language
from .collector_input_type import CollectorInputType


class NestedCollector:
    """Class holding collection logic for nested/complex input types."""

    @staticmethod
    def _prompt_int(prompt: str, default: int | None = None, allow_empty: bool = True,
                    custom_str_val: str | None = None) -> int | str | None:
        """Prompt user for an integer, with optional custom string fallback."""
        language = Language()
        while True:
            val_str = input(prompt).strip()
            if val_str == "":
                if allow_empty:
                    return default
                else:
                    print(f"    {language.get_string('ERROR_INVALID_INTEGER_VALUE')}")
                    continue
            if custom_str_val and val_str.lower() == custom_str_val.lower():
                return custom_str_val.lower()
            try:
                return int(val_str)
            except ValueError:
                print(f"    {language.get_string('ERROR_INVALID_INTEGER_VALUE')}")

    @staticmethod
    def _prompt_float(prompt: str, default: float | None = None, allow_empty: bool = True) -> float | None:
        """Prompt user for a float."""
        language = Language()
        while True:
            val_str = input(prompt).strip()
            if val_str == "":
                if allow_empty:
                    return default
                else:
                    print(f"    {language.get_string('ERROR_INVALID_FLOAT_VALUE')}")
                    continue
            try:
                return float(val_str)
            except ValueError:
                print(f"    {language.get_string('ERROR_INVALID_FLOAT_VALUE')}")

    @staticmethod
    def _prompt_bool(prompt: str, default: bool | None = None, allow_empty: bool = True) -> bool | None:
        """Prompt user for a boolean."""
        language = Language()
        while True:
            val_str = input(prompt).strip()
            if val_str == "":
                if allow_empty:
                    return default
                else:
                    print(f"    {language.get_string('ERROR_INVALID_BOOLEAN_VALUE')}")
                    continue
            if val_str.lower() in ["y", "yes", "true"]:
                return True
            elif val_str.lower() in ["n", "no", "false"]:
                return False
            else:
                print(f"    {language.get_string('ERROR_INVALID_BOOLEAN_VALUE')}")

    @staticmethod
    def _collect_dict_of_ints(title: str, key_prompt: str, value_prompt: str, default_val: int | None = None,
                              allow_empty_val: bool = True) -> dict | None:
        """Helper to collect a mapping of strings to integers."""
        language = Language()
        overrides = {}
        print(f"  {title}")
        print(f"  {language.get_string('INFO_NESTED_COLLECTOR_LEAVE_EMPTY_TO_FINISH')}")
        while True:
            key = input(f"  {key_prompt} ").strip().lower()
            if key == "":
                break
            amount = NestedCollector._prompt_int(f"    {value_prompt} ", default=default_val,
                                                 allow_empty=allow_empty_val)
            overrides[key] = amount
        return overrides if overrides else None

    @staticmethod
    def _collect_nested_dict_of_ints(title: str, outer_prompt: str, inner_prompt: str, value_prompt: str,
                                     allow_empty_inner: bool = True) -> dict | None:
        """Helper to collect a nested mapping of strings to integers."""
        language = Language()
        result = {}
        print(f"  {title}")
        print(f"  {language.get_string('INFO_NESTED_COLLECTOR_LEAVE_EMPTY_TO_FINISH')}")
        while True:
            outer_key = input(f"  {outer_prompt} ").strip().lower()
            if outer_key == "":
                break

            inner_dict = {}
            while True:
                inner_key = input(f"    {inner_prompt} ").strip().lower()
                if inner_key == "":
                    break

                val = NestedCollector._prompt_int(f"      {value_prompt} ", allow_empty=allow_empty_inner)
                inner_dict[inner_key] = val

            if inner_dict:
                result[outer_key] = inner_dict
        return result if result else None

    @staticmethod
    def collect(variable_type: CollectorInputType):
        """Collects input for customized structure nested variables."""
        language = Language()
        match variable_type:
            case CollectorInputType.PAPER_OBFUSCATION_MODEL_OVERRIDES:
                overrides = {}
                print(f"  {language.get_string('NESTED_COLLECTOR_PAPER_OBFUSCATION_MODEL_OVERRIDES_TITLE')}")
                print(f"  {language.get_string('INFO_NESTED_COLLECTOR_LEAVE_EMPTY_TO_FINISH')}")
                while True:
                    obj_name = input(
                        f"  {language.get_string('NESTED_COLLECTOR_PAPER_OBFUSCATION_MODEL_OVERRIDES_KEY_PROMPT')} ").strip()
                    if obj_name == "":
                        break

                    also_obfuscate_str = input(
                        f"    {language.get_string('NESTED_COLLECTOR_PAPER_OBFUSCATION_ALSO_OBFUSCATE_PROMPT')} ").strip()
                    also_obfuscate = [x.strip() for x in
                                      also_obfuscate_str.split(',')] if also_obfuscate_str else []

                    dont_obfuscate_str = input(
                        f"    {language.get_string('NESTED_COLLECTOR_PAPER_OBFUSCATION_DONT_OBFUSCATE_PROMPT')} ").strip()
                    dont_obfuscate = [x.strip() for x in
                                      dont_obfuscate_str.split(',')] if dont_obfuscate_str else []

                    sanitize_count = NestedCollector._prompt_bool(
                        f"    {language.get_string('NESTED_COLLECTOR_PAPER_OBFUSCATION_SANITIZE_COUNT_PROMPT')} ",
                        default=True)

                    overrides[obj_name] = {
                        "also-obfuscate": also_obfuscate,
                        "dont-obfuscate": dont_obfuscate,
                        "sanitize-count": sanitize_count
                    }
                return overrides if overrides else None
            case CollectorInputType.PAPER_PACKET_LIMITER_OVERRIDES:
                overrides = {}
                print(f"  {language.get_string('NESTED_COLLECTOR_PAPER_PACKET_LIMITER_OVERRIDES_TITLE')}")
                print(f"  {language.get_string('INFO_NESTED_COLLECTOR_LEAVE_EMPTY_TO_FINISH')}")
                while True:
                    packet_name = input(
                        f"  {language.get_string('NESTED_COLLECTOR_PAPER_PACKET_LIMITER_PACKET_NAME_PROMPT')} ").strip()
                    if packet_name == "":
                        break

                    action_str = input(
                        f"    {language.get_string('NESTED_COLLECTOR_PAPER_PACKET_LIMITER_ACTION_PROMPT')} ").strip().upper()
                    action = action_str if action_str else "KICK"

                    interval = NestedCollector._prompt_float(
                        f"    {language.get_string('NESTED_COLLECTOR_PAPER_PACKET_LIMITER_INTERVAL_PROMPT')} ",
                        default=7.0)
                    max_packet_rate = NestedCollector._prompt_float(
                        f"    {language.get_string('NESTED_COLLECTOR_PAPER_PACKET_LIMITER_MAX_PACKET_RATE_PROMPT')} ",
                        default=500.0)

                    overrides[packet_name] = {
                        "action": action,
                        "interval": interval,
                        "max-packet-rate": max_packet_rate
                    }
                return overrides if overrides else None
            case CollectorInputType.PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_ENTITY_TYPE:
                return NestedCollector._collect_dict_of_ints(
                    language.get_string('NESTED_COLLECTOR_PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_TITLE'),
                    language.get_string('NESTED_COLLECTOR_PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_KEY_PROMPT'),
                    language.get_string('NESTED_COLLECTOR_PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_VALUE_PROMPT'),
                    default_val=-1
                )
            case CollectorInputType.PAPER_DOOR_BREAKING_DIFFICULTY_ENTITY_TYPE:
                overrides = {}
                print(f"  {language.get_string('NESTED_COLLECTOR_PAPER_DOOR_BREAKING_DIFFICULTY_TITLE')}")
                print(f"  {language.get_string('INFO_NESTED_COLLECTOR_LEAVE_EMPTY_TO_FINISH')}")
                while True:
                    entity_type = input(
                        f"  {language.get_string('NESTED_COLLECTOR_PAPER_DOOR_BREAKING_DIFFICULTY_ENTITY_TYPE_PROMPT')} ").strip().lower()
                    if entity_type == "":
                        break

                    difficulties_str = input(
                        f"    {language.get_string('NESTED_COLLECTOR_PAPER_DOOR_BREAKING_DIFFICULTY_DIFFICULTIES_PROMPT')} ").strip()
                    difficulties = [x.strip() for x in difficulties_str.split(',')] if difficulties_str else []

                    overrides[entity_type] = difficulties
                return overrides if overrides else None
            case CollectorInputType.PAPER_ALT_ITEM_DESPAWN_RATE_ITEM_TYPE:
                return NestedCollector._collect_dict_of_ints(
                    language.get_string('NESTED_COLLECTOR_PAPER_ALT_ITEM_DESPAWN_RATE_TITLE'),
                    language.get_string('NESTED_COLLECTOR_PAPER_ALT_ITEM_DESPAWN_RATE_KEY_PROMPT'),
                    language.get_string('NESTED_COLLECTOR_PAPER_ALT_ITEM_DESPAWN_RATE_VALUE_PROMPT'),
                    default_val=-1
                )
            case CollectorInputType.PAPER_DESPAWN_RANGES_MOB_CATEGORY:
                ranges = {}
                print(f"  {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_RANGES_TITLE')}")
                print(f"  {language.get_string('INFO_NESTED_COLLECTOR_LEAVE_EMPTY_TO_FINISH')}")
                while True:
                    category = input(
                        f"  {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_RANGES_CATEGORY_PROMPT')} ").strip().lower()
                    if category == "":
                        break

                    ranges[category] = {
                        "hard": {
                            "horizontal": NestedCollector._prompt_int(
                                f"    {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_RANGES_HARD_HORIZONTAL_PROMPT')} ",
                                allow_empty=False, custom_str_val="default"),
                            "vertical": NestedCollector._prompt_int(
                                f"    {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_RANGES_HARD_VERTICAL_PROMPT')} ",
                                allow_empty=False, custom_str_val="default")
                        },
                        "soft": {
                            "horizontal": NestedCollector._prompt_int(
                                f"    {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_RANGES_SOFT_HORIZONTAL_PROMPT')} ",
                                allow_empty=False, custom_str_val="default"),
                            "vertical": NestedCollector._prompt_int(
                                f"    {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_RANGES_SOFT_VERTICAL_PROMPT')} ",
                                allow_empty=False, custom_str_val="default")
                        }
                    }
                return ranges if ranges else None
            case CollectorInputType.PAPER_DESPAWN_TIME_ENTITY_TYPE:
                overrides = {}
                print(f"  {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_TIME_TITLE')}")
                print(f"  {language.get_string('INFO_NESTED_COLLECTOR_LEAVE_EMPTY_TO_FINISH')}")
                while True:
                    entity_type = input(
                        f"  {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_TIME_ENTITY_TYPE_PROMPT')} ").strip().lower()
                    if entity_type == "":
                        break

                    val = NestedCollector._prompt_int(
                        f"    {language.get_string('NESTED_COLLECTOR_PAPER_DESPAWN_TIME_VALUE_PROMPT')} ",
                        allow_empty=False, custom_str_val="disabled")
                    overrides[entity_type] = val

                return overrides if overrides else None
            case CollectorInputType.PAPER_FEATURE_SEEDS_FEATURE_NAMESPACE:
                return NestedCollector._collect_dict_of_ints(
                    language.get_string('NESTED_COLLECTOR_PAPER_FEATURE_SEEDS_TITLE'),
                    language.get_string('NESTED_COLLECTOR_PAPER_FEATURE_SEEDS_KEY_PROMPT'),
                    language.get_string('NESTED_COLLECTOR_PAPER_FEATURE_SEEDS_VALUE_PROMPT'),
                    allow_empty_val=False
                )
            case CollectorInputType.PAPER_TICK_RATES_BEHAVIOR_NAME:
                return NestedCollector._collect_nested_dict_of_ints(
                    language.get_string('NESTED_COLLECTOR_PAPER_TICK_RATES_BEHAVIOR_TITLE'),
                    language.get_string('NESTED_COLLECTOR_PAPER_TICK_RATES_BEHAVIOR_OUTER_PROMPT'),
                    language.get_string('NESTED_COLLECTOR_PAPER_TICK_RATES_BEHAVIOR_INNER_PROMPT'),
                    language.get_string('NESTED_COLLECTOR_PAPER_TICK_RATES_BEHAVIOR_VALUE_PROMPT'),
                    allow_empty_inner=False
                )
            case CollectorInputType.PAPER_TICK_RATES_SENSOR_NAME:
                return NestedCollector._collect_nested_dict_of_ints(
                    language.get_string('NESTED_COLLECTOR_PAPER_TICK_RATES_SENSOR_TITLE'),
                    language.get_string('NESTED_COLLECTOR_PAPER_TICK_RATES_SENSOR_OUTER_PROMPT'),
                    language.get_string('NESTED_COLLECTOR_PAPER_TICK_RATES_SENSOR_INNER_PROMPT'),
                    language.get_string('NESTED_COLLECTOR_PAPER_TICK_RATES_SENSOR_VALUE_PROMPT'),
                    allow_empty_inner=False
                )
        return None
