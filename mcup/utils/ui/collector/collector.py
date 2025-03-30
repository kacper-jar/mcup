from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .collector_section import CollectorSection
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
            use_default = input("Use default configuration? (y/n): ").strip().lower() == "y"

            for section_input in section_inputs:
                collector_output[section_input.get_variable_name()] = (
                    "" if use_default else input(f"{section_input.get_variable_prompt()}: ")
                )

        return collector_output

    def get_sections(self) -> list["CollectorSection"]:
        return self.sections

    def add_section(self, section: "CollectorSection"):
        self.sections.append(section)
