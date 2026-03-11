from .collector_input_type import CollectorInputType


class NestedCollector:
    """Class holding collection logic for nested/complex input types."""

    @staticmethod
    def _prompt_int(prompt: str, default: int | None = None, allow_empty: bool = True,
                    custom_str_val: str | None = None) -> int | str | None:
        """Prompt user for an integer, with optional custom string fallback."""
        while True:
            val_str = input(prompt).strip()
            if val_str == "":
                if allow_empty:
                    return default
                else:
                    print("    Invalid integer value. Please try again.")
                    continue
            if custom_str_val and val_str.lower() == custom_str_val.lower():
                return custom_str_val.lower()
            try:
                return int(val_str)
            except ValueError:
                print("    Invalid integer value. Please try again.")

    @staticmethod
    def _prompt_float(prompt: str, default: float | None = None, allow_empty: bool = True) -> float | None:
        """Prompt user for a float."""
        while True:
            val_str = input(prompt).strip()
            if val_str == "":
                if allow_empty:
                    return default
                else:
                    print("    Invalid floating point number value. Please try again.")
                    continue
            try:
                return float(val_str)
            except ValueError:
                print("    Invalid floating point number value. Please try again.")

    @staticmethod
    def _prompt_bool(prompt: str, default: bool | None = None, allow_empty: bool = True) -> bool | None:
        """Prompt user for a boolean."""
        while True:
            val_str = input(prompt).strip()
            if val_str == "":
                if allow_empty:
                    return default
                else:
                    print("    Invalid boolean value. Please try again.")
                    continue
            if val_str.lower() in ["y", "yes", "true"]:
                return True
            elif val_str.lower() in ["n", "no", "false"]:
                return False
            else:
                print("    Invalid boolean value. Please try again.")

    @staticmethod
    def _collect_dict_of_ints(title: str, key_prompt: str, value_prompt: str, default_val: int | None = None,
                              allow_empty_val: bool = True) -> dict | None:
        """Helper to collect a mapping of strings to integers."""
        overrides = {}
        print(f"  {title}")
        print("  Leave empty and press Enter to finish.")
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
        result = {}
        print(f"  {title}")
        print("  Leave empty and press Enter to finish.")
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
        match variable_type:
            case CollectorInputType.PAPER_OBFUSCATION_MODEL_OVERRIDES:
                overrides = {}
                print("  Enter Minecraft Namespaced IDs to configure overrides (e.g. 'minecraft:elytra').")
                print("  Leave empty and press Enter to finish.")
                while True:
                    obj_name = input("  Minecraft Namespaced ID (text): ").strip()
                    if obj_name == "":
                        break

                    also_obfuscate_str = input("    also-obfuscate (texts divided by commas): ").strip()
                    also_obfuscate = [x.strip() for x in
                                      also_obfuscate_str.split(',')] if also_obfuscate_str else []

                    dont_obfuscate_str = input("    dont-obfuscate (texts divided by commas): ").strip()
                    dont_obfuscate = [x.strip() for x in
                                      dont_obfuscate_str.split(',')] if dont_obfuscate_str else []

                    sanitize_count = NestedCollector._prompt_bool("    sanitize-count (true/false): ", default=True)

                    overrides[obj_name] = {
                        "also-obfuscate": also_obfuscate,
                        "dont-obfuscate": dont_obfuscate,
                        "sanitize-count": sanitize_count
                    }
                return overrides if overrides else None
            case CollectorInputType.PAPER_PACKET_LIMITER_OVERRIDES:
                overrides = {}
                print(
                    "  Enter packet class names to configure limit overrides (e.g. 'ServerboundMovePlayerPacket').")
                print("  Leave empty and press Enter to finish.")
                while True:
                    packet_name = input("  Packet name (text): ").strip()
                    if packet_name == "":
                        break

                    action_str = input("    action (DROP, KICK): ").strip().upper()
                    action = action_str if action_str else "KICK"

                    interval = NestedCollector._prompt_float("    interval (number): ", default=7.0)
                    max_packet_rate = NestedCollector._prompt_float("    max-packet-rate (number): ", default=500.0)

                    overrides[packet_name] = {
                        "action": action,
                        "interval": interval,
                        "max-packet-rate": max_packet_rate
                    }
                return overrides if overrides else None
            case CollectorInputType.PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_ENTITY_TYPE:
                return NestedCollector._collect_dict_of_ints(
                    "Enter entity limits.",
                    "Entity type (text):",
                    "Amount (number):",
                    default_val=-1
                )
            case CollectorInputType.PAPER_DOOR_BREAKING_DIFFICULTY_ENTITY_TYPE:
                overrides = {}
                print("  Enter door breaking difficulty.")
                print("  Leave empty and press Enter to finish.")
                while True:
                    entity_type = input("  Entity type (text): ").strip().lower()
                    if entity_type == "":
                        break

                    difficulties_str = input("    Difficulties (texts divided by commas): ").strip()
                    difficulties = [x.strip() for x in difficulties_str.split(',')] if difficulties_str else []

                    overrides[entity_type] = difficulties
                return overrides if overrides else None
            case CollectorInputType.PAPER_ALT_ITEM_DESPAWN_RATE_ITEM_TYPE:
                return NestedCollector._collect_dict_of_ints(
                    "Enter alternative item despawn rate per item.",
                    "Item type (text):",
                    "Amount (number):",
                    default_val=-1
                )
            case CollectorInputType.PAPER_DESPAWN_RANGES_MOB_CATEGORY:
                ranges = {}
                print("  Enter despawn ranges per mob category.")
                print("  Leave empty and press Enter to finish.")
                while True:
                    category = input("  Mob category (text): ").strip().lower()
                    if category == "":
                        break

                    ranges[category] = {
                        "hard": {
                            "horizontal": NestedCollector._prompt_int(
                                "    Horizontal number of blocks away from player to be forcibly despawned (default or int): ",
                                allow_empty=False, custom_str_val="default"),
                            "vertical": NestedCollector._prompt_int(
                                "    Vertical number of blocks away from player to be forcibly despawned (default or int): ",
                                allow_empty=False, custom_str_val="default")
                        },
                        "soft": {
                            "horizontal": NestedCollector._prompt_int(
                                "    Horizontal number of blocks away from player to be randomly picked to despawn (default or int): ",
                                allow_empty=False, custom_str_val="default"),
                            "vertical": NestedCollector._prompt_int(
                                "    Vertical number of blocks away from player to be randomly picked to despawn (default or int): ",
                                allow_empty=False, custom_str_val="default")
                        }
                    }
                return ranges if ranges else None
            case CollectorInputType.PAPER_DESPAWN_TIME_ENTITY_TYPE:
                overrides = {}
                print("  Enter despawn time per entity type.")
                print("  Leave empty and press Enter to finish.")
                while True:
                    entity_type = input("  Entity type (text): ").strip().lower()
                    if entity_type == "":
                        break

                    val = NestedCollector._prompt_int("    Time (seconds as number or 'disabled'): ", allow_empty=False,
                                                      custom_str_val="disabled")
                    overrides[entity_type] = val

                return overrides if overrides else None
            case CollectorInputType.PAPER_FEATURE_SEEDS_FEATURE_NAMESPACE:
                return NestedCollector._collect_dict_of_ints(
                    "Enter feature seeds per feature namespace.",
                    "Feature namespace (text):",
                    "Seed (number):",
                    allow_empty_val=False
                )
            case CollectorInputType.PAPER_TICK_RATES_BEHAVIOR_NAME:
                return NestedCollector._collect_nested_dict_of_ints(
                    "Enter tick rates behavior per entity type.",
                    "Entity type (e.g. villager):",
                    "Behavior name (text):",
                    "Value (number):",
                    allow_empty_inner=False
                )
            case CollectorInputType.PAPER_TICK_RATES_SENSOR_NAME:
                return NestedCollector._collect_nested_dict_of_ints(
                    "Enter tick rates sensor per entity type.",
                    "Entity type (e.g. villager):",
                    "Sensor name (text):",
                    "Value (number):",
                    allow_empty_inner=False
                )
        return None
