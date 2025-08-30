from typing import TYPE_CHECKING

from mcup.cli.language import Language
from mcup.core.user_config import UserConfig
from .collector_input_type import CollectorInputType
from .collector_input_mode import CollectorInputMode

if TYPE_CHECKING:
    from .collector_section import CollectorSection
    from mcup.core.utils.version import Version
    from mcup.core.configs import ConfigFile


class Collector:
    """Class representing Collector, which will collect data for configuration via CLI"""

    def __init__(self, title: str):
        self.title: str = title
        self.sections: list[CollectorSection] = []
        self.config_file: "ConfigFile"

    def set_config_file(self, config_file: "ConfigFile"):
        """Set the associated config file for getting default values."""
        self.config_file = config_file

    def start_collector(self, version: "Version", no_defaults, advanced_mode_enabled) -> dict:
        """Collects user input into a configuration dictionary."""
        user_config = UserConfig()
        language = Language()

        collector_output = {}

        for section in self.sections:
            section_inputs = [
                s_input for s_input in section.get_section_inputs()
                if s_input.variable_min_version <= version <= s_input.variable_max_version
            ]

            filtered_section_inputs = [
                s_input for s_input in section_inputs
                if advanced_mode_enabled or s_input.get_variable_input_mode() == CollectorInputMode.BASIC
            ]

            skipped_section_inputs = [
                s_input for s_input in section_inputs
                if s_input not in filtered_section_inputs
            ]

            if skipped_section_inputs is not None:
                for skipped_section_input in skipped_section_inputs:
                    collector_output[skipped_section_input.get_variable_name()] = ""

            if not filtered_section_inputs:
                continue

            print(f"\n{self.get_title()} - {section.get_section_title()}")
            if section.get_section_header_key() != "":
                print(language.get_string(section.get_section_header_key()))

            self._show_default_configuration_preview(filtered_section_inputs, version)

            use_default = False if no_defaults else (input("Use default configuration? (Y/n): ").strip().lower()
                                                     in ["y", ""])

            for section_input in filtered_section_inputs:
                collector_output[section_input.get_variable_name()] = (
                    "" if use_default else self._process_input(section_input)
                )

        return collector_output

    def _show_default_configuration_preview(self, filtered_section_inputs, version: "Version"):
        """Show a preview of the default configuration for the current section."""
        if not filtered_section_inputs:
            return

        print("Default configuration preview:")
        print("-" * 40)

        variable_names = [section_input.get_variable_name() for section_input in filtered_section_inputs]

        if self.config_file is not None:
            default_values = self.config_file.get_default_values_for_variables(variable_names, version)

            for section_input in filtered_section_inputs:
                variable_name = section_input.get_variable_name()
                default_value = default_values.get(variable_name)

                formatted_value = self._format_default_value_for_display(default_value,
                                                                         section_input.get_variable_input_type())

                print(f"  {variable_name}: {formatted_value}")
        else:
            for section_input in filtered_section_inputs:
                variable_name = section_input.get_variable_name()
                print(f"  {variable_name}: <use system default>")

        print("-" * 40)

    def _format_default_value_for_display(self, value, input_type: "CollectorInputType") -> str:
        """Format a default value for user-friendly display."""
        if value is None or value == "":
            return "<empty>"

        match input_type:
            case CollectorInputType.BOOL:
                return "true" if value else "false"
            case CollectorInputType.STRING_LIST | CollectorInputType.INT_LIST | CollectorInputType.FLOAT_LIST | CollectorInputType.BOOL_LIST:
                if isinstance(value, list):
                    if input_type == CollectorInputType.BOOL_LIST:
                        return ", ".join("true" if item else "false" for item in value)
                    else:
                        return ", ".join(str(item) for item in value)
                else:
                    return str(value)
            case _:
                return str(value)

    def _process_input(self, section_input):
        """Process user input for a given input type."""
        variable_type = section_input.get_variable_input_type()

        match variable_type:
            case CollectorInputType.STRING:
                example_input = "text"
            case CollectorInputType.INT:
                example_input = "number"
            case CollectorInputType.STRING_OR_INT:
                example_input = "text or number"
            case CollectorInputType.FLOAT:
                example_input = "floating point number"
            case CollectorInputType.BOOL:
                example_input = "true/false"
            case CollectorInputType.STRING_LIST:
                example_input = "texts divided by commas"
            case CollectorInputType.FLOAT_LIST:
                example_input = "floating point numbers divided by commas"
            case CollectorInputType.INT_LIST:
                example_input = "numbers divided by commas"
            case CollectorInputType.BOOL_LIST:
                example_input = "true/false divided by commas"
            case _:
                example_input = ""

        language = Language()

        while True:
            var = input(f"{language.get_string(section_input.get_variable_prompt_key())} ({example_input}): ")

            if var == "":
                return var

            match variable_type:
                case CollectorInputType.STRING:
                    return var
                case CollectorInputType.INT:
                    try:
                        return int(var)
                    except ValueError:
                        print("Invalid integer value. Please try again.")
                        continue
                case CollectorInputType.STRING_OR_INT:
                    try:
                        return int(var)
                    except ValueError:
                        return var
                case CollectorInputType.FLOAT:
                    try:
                        return float(var)
                    except ValueError:
                        print("Invalid floating point number value. Please try again.")
                        continue
                case CollectorInputType.BOOL:
                    if var.lower() in ["y", "yes", "true"]:
                        return True
                    elif var.lower() in ["n", "no", "false"]:
                        return False
                    else:
                        print("Invalid boolean value. Please try again.")
                        continue
                case CollectorInputType.STRING_LIST:
                    return var.split(',')
                case CollectorInputType.INT_LIST:
                    try:
                        return [int(item.strip()) for item in var.split(',')]
                    except ValueError:
                        print("Invalid integer value in list. Please try again.")
                        continue
                case CollectorInputType.FLOAT_LIST:
                    try:
                        return [float(item.strip()) for item in var.split(',')]
                    except ValueError:
                        print("Invalid floating point number value in list. Please try again.")
                        continue
                case CollectorInputType.BOOL_LIST:
                    bool_list = []
                    valid_list = True
                    for item in var.split(','):
                        item = item.strip().lower()
                        if item in ["y", "yes", "true"]:
                            bool_list.append(True)
                        elif item in ["n", "no", "false"]:
                            bool_list.append(False)
                        else:
                            print(f"Invalid boolean value '{item}' in list. Please try again.")
                            valid_list = False
                            break
                    if valid_list:
                        return bool_list
                    continue
            return None

    def get_version_appropriate_defaults(self, version: "Version") -> dict:
        """Get default configuration values only for properties that are valid for the specified version."""
        collector_output = {}

        for section in self.sections:
            section_inputs = [
                s_input for s_input in section.get_section_inputs()
                if s_input.variable_min_version <= version <= s_input.variable_max_version
            ]

            for section_input in section_inputs:
                collector_output[section_input.get_variable_name()] = ""

        return collector_output

    def get_title(self) -> str:
        """Get collector title."""
        return self.title

    def get_sections(self) -> list["CollectorSection"]:
        """Get collector sections."""
        return self.sections

    def add_section(self, section: "CollectorSection"):
        """Add a collector section."""
        self.sections.append(section)
