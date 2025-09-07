import os
from pathlib import Path

from mcup.core.config_assemblers import Assembler
from mcup.core.config_assemblers.java_flags_builder import JavaFlagsBuilder
from mcup.core.config_assemblers.script_template_manager import ScriptTemplateManager
from mcup.core.status import StatusCode, Status


class BashStartScriptAssembler(Assembler):
    """Class representing bash start script assembler."""

    @staticmethod
    def validate_configuration(config) -> Status:
        """Validate required configuration keys."""
        required_keys = [
            'server-jar', 'initial-heap', 'max-heap', 'screen-name',
            'max-restarts', 'restart-delay'
        ]

        if not hasattr(config, 'configuration') or not config.configuration:
            return Status(StatusCode.ERROR_CONFIG_VALIDATION_FAILED, "Configuration is empty")

        missing_keys = []
        for key in required_keys:
            if key not in config.configuration:
                missing_keys.append(key)

        if missing_keys:
            return Status(StatusCode.ERROR_CONFIG_MISSING_REQUIRED_KEYS, missing_keys)

        return Status(StatusCode.SUCCESS)

    @staticmethod
    def generate_script_content(config) -> tuple[str, Status]:
        """Generate script content from configuration."""
        try:
            java_command, status = JavaFlagsBuilder.build_java_command(config.configuration)
            if status.status_code != StatusCode.SUCCESS:
                return "", status

            template = ScriptTemplateManager.get_bash_template()

            template_vars = {
                'server_jar': config.configuration['server-jar'],
                'server_jar_clean': str(config.configuration['server-jar']).replace("@", ""),
                'screen_name': config.configuration['screen-name'],
                'max_restarts': config.configuration['max-restarts'],
                'restart_delay': config.configuration['restart-delay'],
                'java_command': java_command
            }

            validation_status = ScriptTemplateManager.validate_template_variables(template, template_vars)
            if validation_status.status_code != StatusCode.SUCCESS:
                return "", validation_status

            script_content = template.format(**template_vars)
            return script_content, Status(StatusCode.SUCCESS)

        except Exception as e:
            return "", Status(StatusCode.ERROR_SCRIPT_TEMPLATE_INVALID, str(e))

    @staticmethod
    def write_script_file(path: Path, config, content: str) -> Status:
        """Handle file writing with error handling."""
        try:
            full_dir = Path(os.path.join(path, config.config_file_path))
            status = Assembler.create_directory_if_needed(full_dir)
            if status.status_code != StatusCode.SUCCESS:
                return status

            full_path = Path(os.path.join(full_dir, config.config_file_name))
            status = Assembler.safe_write_file(full_path, content)
            if status.status_code != StatusCode.SUCCESS:
                return status

            try:
                os.chmod(full_path, 0o755)
            except OSError:
                pass

            return Status(StatusCode.SUCCESS)

        except Exception as e:
            return Status(StatusCode.ERROR_CONFIG_FILE_WRITE_FAILED, [path, str(e)])

    @staticmethod
    def assemble(path: Path, config) -> Status:
        """Assemble the bash start script at the specified path."""
        path_status = Assembler.validate_path(path)
        if path_status.status_code != StatusCode.SUCCESS:
            return path_status

        config_status = Assembler.validate_config(config)
        if config_status.status_code != StatusCode.SUCCESS:
            return config_status

        validation_status = BashStartScriptAssembler.validate_configuration(config)
        if validation_status.status_code != StatusCode.SUCCESS:
            return validation_status

        content, generation_status = BashStartScriptAssembler.generate_script_content(config)
        if generation_status.status_code != StatusCode.SUCCESS:
            return generation_status

        return BashStartScriptAssembler.write_script_file(path, config, content)
