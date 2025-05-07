from mcup.core.template.template import Template
from mcup.core.config_assemblers.assembler_linker_config import AssemblerLinkerConfig


def test_init():
    """Test initialization of Template objects."""
    linker_config = AssemblerLinkerConfig()

    template = Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=linker_config
    )

    assert template.template_name == "test_template"
    assert template.template_server_type == "paper"
    assert template.template_server_version == "1.19.4"
    assert template.template_server_source == "DOWNLOAD"
    assert template.template_server_target == "https://example.com/paper-1.19.4.jar"
    assert template.template_linker_config == linker_config


def test_get_template_name():
    """Test get_template_name method."""
    template = Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=AssemblerLinkerConfig()
    )
    
    assert template.get_template_name() == "test_template"


def test_get_template_server_type():
    """Test get_template_server_type method."""
    template = Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=AssemblerLinkerConfig()
    )
    
    assert template.get_template_server_type() == "paper"


def test_get_template_server_version():
    """Test get_template_server_version method."""
    template = Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=AssemblerLinkerConfig()
    )
    
    assert template.get_template_server_version() == "1.19.4"


def test_get_template_server_source():
    """Test get_template_server_source method."""
    template = Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=AssemblerLinkerConfig()
    )
    
    assert template.get_template_server_source() == "DOWNLOAD"


def test_get_template_server_target():
    """Test get_template_server_target method."""
    template = Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=AssemblerLinkerConfig()
    )
    
    assert template.get_template_server_target() == "https://example.com/paper-1.19.4.jar"


def test_get_template_linker_config():
    """Test get_template_linker_config method."""
    linker_config = AssemblerLinkerConfig()
    
    template = Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=linker_config
    )
    
    assert template.get_template_linker_config() == linker_config


def test_get_dict():
    """Test get_dict method."""
    linker_config = AssemblerLinkerConfig()
    
    template = Template(
        template_name="test_template",
        template_server_type="paper",
        template_server_version="1.19.4",
        template_server_source="DOWNLOAD",
        template_server_target="https://example.com/paper-1.19.4.jar",
        template_linker_config=linker_config
    )
    
    template_dict = template.get_dict()
    
    assert template_dict["template_name"] == "test_template"
    assert template_dict["template_server_type"] == "paper"
    assert template_dict["template_server_version"] == "1.19.4"
    assert template_dict["template_server_source"] == "DOWNLOAD"
    assert template_dict["template_server_target"] == "https://example.com/paper-1.19.4.jar"
    assert template_dict["template_linker_config"] == linker_config.to_dict(export_default_config=False)
