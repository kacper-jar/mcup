import pytest
from mcup.cli.language import Language


class TestLanguage:

    def test_get_existing_string(self):
        """Verify retrieval of known key."""
        lang = Language()
        assert lang.get_string("SUCCESS_SERVER") == "Server created successfully."

    def test_get_non_existing_string(self):
        """Verify returns key when not found."""
        lang = Language()
        key = "NON_EXISTING_KEY_XYZ"
        assert lang.get_string(key) == key

    def test_get_string_with_args(self):
        """Verify formatting."""
        lang = Language()
        result = lang.get_string("SUCCESS_TEMPLATE_CREATE", "my_template")
        assert result == "Template 'my_template' created successfully."

    def test_get_string_extra_args_ignored_if_no_placeholders(self):
        """Verify behavior when args are provided but no placeholders exists."""
        lang = Language()
        result = lang.get_string("SUCCESS_SERVER", "extra_arg")
        assert result == "Server created successfully."

    def test_get_string_missing_args(self):
        """Verify behavior when args are missing."""
        lang = Language()

        with pytest.raises(IndexError):
            lang.get_string("SUCCESS_TEMPLATE_CREATE")
