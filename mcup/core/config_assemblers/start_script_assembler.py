from mcup.core.config_assemblers import Assembler


class StartScriptAssembler(Assembler):
    """Class representing start script assembler."""
    @staticmethod
    def assemble(path: str, config):
        """Assemble the start script at the specified path."""
        with open(f"{path}/{config.config_file_path}/{config.config_file_name}", "w") as config_file:
            config_file.write(f"screen -dmS {config.configuration['screen-name']} java "
                              f"-Xms{config.configuration['initial-heap']}M "
                              f"-Xmx{config.configuration['max-heap']}M "
                              f"-jar {config.configuration['server-jar']} nogui")
