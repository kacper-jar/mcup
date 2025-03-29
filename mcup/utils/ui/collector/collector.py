from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .collector_section import CollectorSection


class Collector:
    """Class representing Collector, which will collect data for configuration via CLI"""
    def __init__(self):
        self.sections: list[CollectorSection] = []

    def start_collector(self) -> dict:
        """Function for collecting user input into configuration."""
        collector_output = {}

        for section in self.sections:
            print(f"\n{section.get_section_title()}")
            default_cfg_choice = input("Use default configuration? y/n: ")
            for section_input in section.get_section_inputs():
                if default_cfg_choice == "y":
                    # "" makes config file use default var
                    collector_output[section_input.get_variable_name()] = ""
                else:
                    user_input = input(f"{section_input.get_variable_prompt()}: ")
                    collector_output[section_input.get_variable_name()] = user_input

        return collector_output

    def get_sections(self) -> list["CollectorSection"]:
        return self.sections

    def add_section(self, section: "CollectorSection"):
        self.sections.append(section)
