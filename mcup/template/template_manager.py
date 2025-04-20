import json
import os


class TemplateManager:
    @staticmethod
    def save_template(template):
        if not os.path.exists(".templates"):
            os.makedirs(".templates")

        template_path = f".templates/{template.get_template_name()}.json"
        with open(template_path, 'w') as file:
            json.dump(template.get_dict(), file, indent=4)
            # TODO: Remove default config values from template, since they are not needed for the template itself.
            print(f"Template '{template.get_template_name()}' saved successfully.")
