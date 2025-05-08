import json
import os

from mcup.core.template import Template
from mcup.core.utils.path import PathProvider


class TemplateManager:
    """Class handling template operations."""
    @staticmethod
    def save_template(template: Template):
        """Save template to templates directory."""
        path_provider = PathProvider()

        if not os.path.exists(path_provider.get_templates_path()):
            os.makedirs(path_provider.get_templates_path())

        template_path = f"{path_provider.get_templates_path()}/{template.get_template_name()}.json"
        with open(template_path, 'w') as file:
            json.dump(template.get_dict(), file, indent=4)
