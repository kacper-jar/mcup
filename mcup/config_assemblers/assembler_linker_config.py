from mcup.configs import ConfigFile


class AssemblerLinkerConfig:
    def __init__(self):
        self.configuration_files: list[ConfigFile] = []

    def add_configuration_file(self, configuration_file: ConfigFile):
        self.configuration_files.append(configuration_file)

    def get_configuration_files(self):
        return self.configuration_files

    def get_configuration_file_count(self):
        return len(self.configuration_files)
