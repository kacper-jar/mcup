from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .collector_section import CollectorSection
    from . import CollectorInputType
    from mcup.utils.version import Version


class Collector:
    """Class representing Collector, which will collect data for configuration via CLI"""
    def __init__(self):
        self.sections: list[CollectorSection] = []

    def start_collector(self, version: "Version") -> dict:
        """Collects user input into a configuration dictionary."""
        collector_output = {}

        for section in self.sections:
            section_inputs = [
                s_input for s_input in section.get_section_inputs()
                if s_input.variable_min_version <= version <= s_input.variable_max_version
            ]

            if not section_inputs:
                continue

            print(f"\n{section.get_section_title()}")
            if section.get_section_header() != "":
                print(section.get_section_header())
            use_default = input("Use default configuration? (Y/n): ").strip().lower() in ["y", ""]

            for section_input in section_inputs:
                collector_output[section_input.get_variable_name()] = (
                    "" if use_default else self._process_input(section_input)
                )

        return collector_output

    def _process_input(self, section_input):
        """Process user input for a given input type."""
        variable_type = section_input.get_variable_input_type()

        match variable_type:
            case CollectorInputType.STRING:
                example_input = "text"
            case CollectorInputType.INT:
                example_input = "number"
            case CollectorInputType.BOOL:
                example_input = "true/false"
            case CollectorInputType.STRING_LIST:
                example_input = "texts divided by commas"
            case CollectorInputType.INT_LIST:
                example_input = "numbers divided by commas"
            case CollectorInputType.BOOL_LIST:
                example_input = "true/false divided by commas"

        var = input(f"{section_input.get_variable_prompt()} ({example_input}): ")

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
            case CollectorInputType.BOOL:
                if var.lower() in ["y", "yes", "true"]:
                    return True
                elif var.lower() in ["n", "no", "false"]:
                    return False
                else:
                    print("Invalid boolean value. Please try again.")
            case CollectorInputType.STRING_LIST:
                return var.split(',')
            case CollectorInputType.INT_LIST:
                try:
                    return [int(item.strip()) for item in var.split(',')]
                except ValueError:
                    print("Invalid integer value in list. Please try again.")
            case CollectorInputType.BOOL_LIST:
                bool_list = []
                for item in var.split(','):
                    item = item.strip().lower()
                    if item in ["y", "yes", "true"]:
                        bool_list.append(True)
                    elif item in ["n", "no", "false"]:
                        bool_list.append(False)
                    else:
                        print(f"Invalid boolean value '{item}' in list. Please try again.")
                        return None
                return bool_list
        return None

    def get_sections(self) -> list["CollectorSection"]:
        return self.sections

    def add_section(self, section: "CollectorSection"):
        self.sections.append(section)
