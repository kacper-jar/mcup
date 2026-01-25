import pytest
from unittest.mock import MagicMock
from mcup.core.config_assemblers.assembler_linker import AssemblerLinker
from mcup.core.config_assemblers import AssemblerLinkerConfig
from mcup.core.config_assemblers import (
    ServerPropertiesAssembler, YmlAssembler, BashStartScriptAssembler,
    BatchStartScriptAssembler, EulaAssembler
)
from mcup.core.configs import ConfigFile


class TestAssemblerLinker:

    @pytest.fixture
    def linker(self):
        config = AssemblerLinkerConfig()
        return AssemblerLinker(config)

    def test_link_server_properties(self, linker):
        """Verify server.properties maps to ServerPropertiesAssembler."""
        mock_file = MagicMock(spec=ConfigFile)
        mock_file.get_file_name.return_value = "server.properties"
        mock_file.config_file_name = "server.properties"

        linker.configuration.add_configuration_file(mock_file)
        linker.link()

        linked = linker.get_linked_files()
        assert "server.properties" in linked
        assert isinstance(linked["server.properties"], ServerPropertiesAssembler)

    def test_link_yml_configs(self, linker):
        """Verify .yml files map to YmlAssembler."""
        yml_files = ["bukkit.yml", "spigot.yml", "paper.yml", "paper-global.yml", "paper-world-defaults.yml"]

        for name in yml_files:
            mock_file = MagicMock(spec=ConfigFile)
            mock_file.get_file_name.return_value = name
            mock_file.config_file_name = name
            linker.configuration.add_configuration_file(mock_file)

        linker.link()
        linked = linker.get_linked_files()

        for name in yml_files:
            assert name in linked
            assert isinstance(linked[name], YmlAssembler)

    def test_link_scripts(self, linker):
        """Verify scripts map to appropriate assemblers."""
        bash = MagicMock(spec=ConfigFile)
        bash.get_file_name.return_value = "start.sh"
        bash.config_file_name = "start.sh"
        linker.configuration.add_configuration_file(bash)

        batch = MagicMock(spec=ConfigFile)
        batch.get_file_name.return_value = "start.bat"
        batch.config_file_name = "start.bat"
        linker.configuration.add_configuration_file(batch)

        linker.link()
        linked = linker.get_linked_files()

        assert isinstance(linked["start.sh"], BashStartScriptAssembler)
        assert isinstance(linked["start.bat"], BatchStartScriptAssembler)

    def test_link_eula(self, linker):
        """Verify eula.txt maps to EulaAssembler."""
        eula = MagicMock(spec=ConfigFile)
        eula.get_file_name.return_value = "eula.txt"
        eula.config_file_name = "eula.txt"
        linker.configuration.add_configuration_file(eula)

        linker.link()
        linked = linker.get_linked_files()

        assert isinstance(linked["eula.txt"], EulaAssembler)
