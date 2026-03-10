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

        mock_input_str = MagicMock(spec=CollectorInput)
        mock_input_str.get_variable_input_type.return_value = CollectorInputType.STRING
        mock_input_str.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = ["text"]
        assert collector._process_input(mock_input_str) == "text"

        mock_input_float = MagicMock(spec=CollectorInput)
        mock_input_float.get_variable_input_type.return_value = CollectorInputType.FLOAT
        mock_input_float.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = ["invalid", "1.5"]
        assert collector._process_input(mock_input_float) == 1.5

        mock_input_mixed = MagicMock(spec=CollectorInput)
        mock_input_mixed.get_variable_input_type.return_value = CollectorInputType.STRING_OR_INT
        mock_input_mixed.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = ["123", "abc"]
        assert collector._process_input(mock_input_mixed) == 123
        assert collector._process_input(mock_input_mixed) == "abc"

        mock_input_fl = MagicMock(spec=CollectorInput)
        mock_input_fl.get_variable_input_type.return_value = CollectorInputType.FLOAT_LIST
        mock_input_fl.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = ["1.1, 2.2"]
        assert collector._process_input(mock_input_fl) == [1.1, 2.2]

        mock_input_bl = MagicMock(spec=CollectorInput)
        mock_input_bl.get_variable_input_type.return_value = CollectorInputType.BOOL_LIST
        mock_input_bl.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = ["y, n, true, false"]
        assert collector._process_input(mock_input_bl) == [True, False, True, False]

        mock_input_paper_overrides = MagicMock(spec=CollectorInput)
        mock_input_paper_overrides.get_variable_input_type.return_value = CollectorInputType.PAPER_OBFUSCATION_MODEL_OVERRIDES
        mock_input_paper_overrides.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = [
            "minecraft:elytra",
            "opt1, opt2",
            "opt3",
            "y",
            ""
        ]
        assert collector._process_input(mock_input_paper_overrides) == {
            "minecraft:elytra": {
                "also-obfuscate": ["opt1", "opt2"],
                "dont-obfuscate": ["opt3"],
                "sanitize-count": True
            }
        }

        assert collector._format_default_value_for_display(
            {"arrow": -1, "ender_pearl": -1}, CollectorInputType.PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_ENTITY_TYPE
        ) == "arrow: -1, ender_pearl: -1"
        assert collector._format_default_value_for_display(
            "unknown", CollectorInputType.PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_ENTITY_TYPE
        ) == "unknown"

        assert collector._format_default_value_for_display(
            {"husk": ["HARD"], "zombie": ["HARD", "NORMAL"]},
            CollectorInputType.PAPER_DOOR_BREAKING_DIFFICULTY_ENTITY_TYPE
        ) == "husk: [HARD], zombie: [HARD, NORMAL]"
        assert collector._format_default_value_for_display(
            "unknown", CollectorInputType.PAPER_DOOR_BREAKING_DIFFICULTY_ENTITY_TYPE
        ) == "unknown"

        assert collector._format_default_value_for_display(
            {"cobblestone": 300},
            CollectorInputType.PAPER_ALT_ITEM_DESPAWN_RATE_ITEM_TYPE
        ) == "cobblestone: 300"
        assert collector._format_default_value_for_display(
            "unknown", CollectorInputType.PAPER_ALT_ITEM_DESPAWN_RATE_ITEM_TYPE
        ) == "unknown"

        assert collector._format_default_value_for_display(
            {"ambient": {"hard": {"horizontal": 128, "vertical": "default"}}},
            CollectorInputType.PAPER_DESPAWN_RANGES_MOB_CATEGORY
        ) == "ambient: [hard: (128, default)]"
        assert collector._format_default_value_for_display(
            {"ambient": {"hard": {"horizontal": 128, "vertical": "default"}, "soft": {"horizontal": 32, "vertical": 32}}, "axolotls": "default"},
            CollectorInputType.PAPER_DESPAWN_RANGES_MOB_CATEGORY
        ) == "ambient: [hard: (128, default), soft: (32, 32)], axolotls: default"
        assert collector._format_default_value_for_display(
            "unknown", CollectorInputType.PAPER_DESPAWN_RANGES_MOB_CATEGORY
        ) == "unknown"

        assert collector._format_default_value_for_display(
            {"llama_spit": "disabled", "snowball": 60},
            CollectorInputType.PAPER_DESPAWN_TIME_ENTITY_TYPE
        ) == "llama_spit: disabled, snowball: 60"
        assert collector._format_default_value_for_display(
            "unknown", CollectorInputType.PAPER_DESPAWN_TIME_ENTITY_TYPE
        ) == "unknown"

        assert collector._format_default_value_for_display(
            {"generate-random-seeds-for-all": False, "minecraft:desert_pyramid": 12345},
            CollectorInputType.PAPER_FEATURE_SEEDS_FEATURE_NAMESPACE
        ) == "minecraft:desert_pyramid: 12345"
        assert collector._format_default_value_for_display(
            {"generate-random-seeds-for-all": True},
            CollectorInputType.PAPER_FEATURE_SEEDS_FEATURE_NAMESPACE
        ) == "unknown"
        assert collector._format_default_value_for_display(
            "unknown", CollectorInputType.PAPER_FEATURE_SEEDS_FEATURE_NAMESPACE
        ) == "unknown"

        mock_input_packet_overrides = MagicMock(spec=CollectorInput)
        mock_input_packet_overrides.get_variable_input_type.return_value = CollectorInputType.PAPER_PACKET_LIMITER_OVERRIDES
        mock_input_packet_overrides.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = [
            "ServerboundMovePlayerPacket",
            "DROP",
            "1.5",
            "100.0",
            "ServerboundInteractPacket",
            "",
            "",
            "",
            ""
        ]
        assert collector._process_input(mock_input_packet_overrides) == {
            "ServerboundMovePlayerPacket": {
                "action": "DROP",
                "interval": 1.5,
                "max-packet-rate": 100.0
            },
            "ServerboundInteractPacket": {
                "action": "KICK",
                "interval": 7.0,
                "max-packet-rate": 500.0
            }
        }

        mock_input_entity_limits = MagicMock(spec=CollectorInput)
        mock_input_entity_limits.get_variable_input_type.return_value = CollectorInputType.PAPER_ENTITY_PER_CHUNK_SAVE_LIMIT_ENTITY_TYPE
        mock_input_entity_limits.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = [
            "arrow",
            "100",
            "ender_pearl",
            "",
            "snowball",
            "invalid",
            "50",
            ""
        ]
        assert collector._process_input(mock_input_entity_limits) == {
            "arrow": 100,
            "ender_pearl": -1,
            "snowball": 50
        }

        mock_input_door_breaking = MagicMock(spec=CollectorInput)
        mock_input_door_breaking.get_variable_input_type.return_value = CollectorInputType.PAPER_DOOR_BREAKING_DIFFICULTY_ENTITY_TYPE
        mock_input_door_breaking.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = [
            "husk",
            "HARD, NORMAL",
            "zombie",
            "HARD",
            "vindicator",
            "",
            ""
        ]
        assert collector._process_input(mock_input_door_breaking) == {
            "husk": ["HARD", "NORMAL"],
            "zombie": ["HARD"],
            "vindicator": []
        }

        mock_input_alt_item_despawn_rate = MagicMock(spec=CollectorInput)
        mock_input_alt_item_despawn_rate.get_variable_input_type.return_value = CollectorInputType.PAPER_ALT_ITEM_DESPAWN_RATE_ITEM_TYPE
        mock_input_alt_item_despawn_rate.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = [
            "cobblestone",
            "300",
            "dirt",
            "",
            "invalid",
            "bad_number",
            "100",
            ""
        ]
        assert collector._process_input(mock_input_alt_item_despawn_rate) == {
            "cobblestone": 300,
            "dirt": -1,
            "invalid": 100
        }

        mock_input_despawn_ranges = MagicMock(spec=CollectorInput)
        mock_input_despawn_ranges.get_variable_input_type.return_value = CollectorInputType.PAPER_DESPAWN_RANGES_MOB_CATEGORY
        mock_input_despawn_ranges.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = [
            "ambient",
            "128",
            "default",
            "32",
            "32",
            "axolotls",
            "invalid",
            "default",
            "default",
            "16",
            "16",
            ""
        ]
        assert collector._process_input(mock_input_despawn_ranges) == {
            "ambient": {
                "hard": {"horizontal": 128, "vertical": "default"},
                "soft": {"horizontal": 32, "vertical": 32}
            },
            "axolotls": {
                "hard": {"horizontal": "default", "vertical": "default"},
                "soft": {"horizontal": 16, "vertical": 16}
            }
        }

        mock_input_despawn_time = MagicMock(spec=CollectorInput)
        mock_input_despawn_time.get_variable_input_type.return_value = CollectorInputType.PAPER_DESPAWN_TIME_ENTITY_TYPE
        mock_input_despawn_time.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = [
            "llama_spit",
            "invalid",
            "disabled",
            "snowball",
            "60",
            ""
        ]
        assert collector._process_input(mock_input_despawn_time) == {
            "llama_spit": "disabled",
            "snowball": 60
        }

        mock_input_feature_seeds = MagicMock(spec=CollectorInput)
        mock_input_feature_seeds.get_variable_input_type.return_value = CollectorInputType.PAPER_FEATURE_SEEDS_FEATURE_NAMESPACE
        mock_input_feature_seeds.get_variable_prompt_key.return_value = "prompt"
        mock_builtin_input.side_effect = [
            "minecraft:desert_pyramid",
            "invalid",
            "123456",
            "minecraft:end_city",
            "654321",
            ""
        ]
        assert collector._process_input(mock_input_feature_seeds) == {
            "minecraft:desert_pyramid": 123456,
            "minecraft:end_city": 654321
        }

    @patch("mcup.cli.ui.elements.collector.collector.UserConfig")
    def test_version_filtering(self, mock_user_config, mock_section, mock_input):
        collector = Collector("Test collector")

        mock_input.variable_min_version = Version(1, 18)
        mock_input.variable_max_version = Version(1, 18)

        mock_section.get_section_inputs.return_value = [mock_input]
        collector.add_section(mock_section)

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
