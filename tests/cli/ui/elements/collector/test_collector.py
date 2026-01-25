import pytest
from unittest.mock import MagicMock, patch
from mcup.cli.ui.elements.collector.collector import Collector
from mcup.cli.ui.elements.collector.collector_input import CollectorInput
from mcup.cli.ui.elements.collector.collector_section import CollectorSection
from mcup.cli.ui.elements.collector.collector_input_type import CollectorInputType
from mcup.cli.ui.elements.collector.collector_input_mode import CollectorInputMode
from mcup.core.utils.version import Version


class TestCollector:

    @pytest.fixture
    def mock_section(self):
        return MagicMock(spec=CollectorSection)

    @pytest.fixture
    def mock_input(self):
        inp = MagicMock(spec=CollectorInput)
        inp.get_variable_name.return_value = "test_var"
        inp.get_variable_prompt_key.return_value = "prompt_key"
        inp.variable_min_version = Version(1, 0)
        inp.variable_max_version = Version(999, 999)
        inp.get_variable_input_mode.return_value = CollectorInputMode.BASIC
        return inp

    @patch("builtins.input")
    @patch("mcup.cli.ui.elements.collector.collector.Language")
    def test_process_input_validation(self, mock_language, mock_builtin_input):
        collector = Collector("Test Title")

        mock_input_int = MagicMock(spec=CollectorInput)
        mock_input_int.get_variable_input_type.return_value = CollectorInputType.INT
        mock_input_int.get_variable_prompt_key.return_value = "prompt"

        mock_builtin_input.side_effect = ["invalid", "123"]
        result = collector._process_input(mock_input_int)
        assert result == 123

        mock_input_bool = MagicMock(spec=CollectorInput)
        mock_input_bool.get_variable_input_type.return_value = CollectorInputType.BOOL
        mock_input_bool.get_variable_prompt_key.return_value = "prompt"

        mock_builtin_input.side_effect = ["not_bool", "y"]
        result = collector._process_input(mock_input_bool)
        assert result is True

        mock_input_list = MagicMock(spec=CollectorInput)
        mock_input_list.get_variable_input_type.return_value = CollectorInputType.INT_LIST
        mock_input_list.get_variable_prompt_key.return_value = "prompt"

        mock_builtin_input.side_effect = ["1, a", "1, 2, 3"]
        result = collector._process_input(mock_input_list)
        assert result == [1, 2, 3]

    @patch("mcup.cli.ui.elements.collector.collector.UserConfig")
    def test_version_filtering(self, mock_user_config, mock_section, mock_input):
        collector = Collector("Test collector")

        mock_input.variable_min_version = Version(1, 18)
        mock_input.variable_max_version = Version(1, 18)

        mock_section.get_section_inputs.return_value = [mock_input]
        collector.add_section(mock_section)

        # Test with 1.17 (should be skipped)
        # We need to mock _show_default_configuration_preview and inputs to avoid actual interaction if it reaches there
        # But start_collector logic filters before loop if section is empty? No, filters inside loop.

        with patch.object(collector, '_process_input') as mock_process:
            result = collector.start_collector(Version(1, 17), no_defaults=True, advanced_mode_enabled=False)
            assert "test_var" not in result
            mock_process.assert_not_called()

        with patch("builtins.print"), patch("builtins.input", return_value="y"):
            mock_input.variable_min_version = Version(1, 18)
            mock_input.variable_max_version = Version(1, 18)
            mock_section.get_section_inputs.return_value = [mock_input]

            result = collector.start_collector(Version(1, 18), no_defaults=True, advanced_mode_enabled=False)

            with patch.object(collector, '_process_input', return_value="processed"):
                result = collector.start_collector(Version(1, 18), no_defaults=True, advanced_mode_enabled=False)
                assert result["test_var"] == "processed"

    @patch("mcup.cli.ui.elements.collector.collector.UserConfig")
    def test_mode_filtering(self, mock_user_config, mock_section, mock_input):
        collector = Collector("Test collector")

        mock_input.get_variable_input_mode.return_value = CollectorInputMode.ADVANCED
        mock_section.get_section_inputs.return_value = [mock_input]
        collector.add_section(mock_section)

        with patch("builtins.print"):
            result = collector.start_collector(Version(1, 18), no_defaults=True, advanced_mode_enabled=False)
            assert result["test_var"] == ""

        with patch.object(collector, '_process_input', return_value="processed"):
            result = collector.start_collector(Version(1, 18), no_defaults=True, advanced_mode_enabled=True)
            assert result["test_var"] == "processed"
