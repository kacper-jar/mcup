import pytest
import requests
import subprocess
from mcup.core.handlers.server_handler import ServerHandler
from mcup.core.config_assemblers.assembler_linker_config import AssemblerLinkerConfig


@pytest.fixture
def mock_server_path(tmp_path):
    """Create a temporary directory for server files."""
    return tmp_path / "server"


@pytest.fixture
def mock_assembler_linker_config():
    """Create a mock AssemblerLinkerConfig for testing."""
    return AssemblerLinkerConfig()


@pytest.fixture
def mock_progress(mocker):
    """Mock the Progress class from rich.progress."""
    mock_progress_class = mocker.patch('mcup.core.handlers.server_handler.Progress')
    mock_progress_instance = mock_progress_class.return_value.__enter__.return_value
    mock_task = mocker.Mock()
    mock_progress_instance.add_task.return_value = mock_task

    return mock_progress_instance, mock_task


def test_create_download_success(mock_server_path, mock_assembler_linker_config, mock_progress, mocker):
    """Test creating a server by downloading the JAR file (success case)."""
    mock_version = mocker.Mock()
    mock_version.__ge__ = lambda self, other: False
    mocker.patch('mcup.core.handlers.server_handler.Version.from_string', return_value=mock_version)

    mocker.patch('pathlib.Path.exists', return_value=False)

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.headers.get.return_value = "1000"
    mock_response.iter_content.return_value = [b"chunk1", b"chunk2"]
    mocker.patch('requests.get', return_value=mock_response)

    mock_open = mocker.patch('builtins.open', mocker.mock_open())

    mock_makedirs = mocker.patch('os.makedirs')

    mocker.patch('builtins.print')

    mock_assembler_linker = mocker.patch('mcup.core.handlers.server_handler.AssemblerLinker')
    mock_assembler_linker_instance = mock_assembler_linker.return_value

    handler = ServerHandler()

    handler.create(
        server_path=mock_server_path,
        server_version="1.19.4",
        source="DOWNLOAD",
        target="https://example.com/paper-1.19.4.jar",
        assembler_linker_config=mock_assembler_linker_config
    )

    mock_makedirs.assert_called_once_with(mock_server_path)

    requests.get.assert_called_once_with("https://example.com/paper-1.19.4.jar", stream=True)

    expected_file_path = mock_server_path / "paper-1.19.4.jar"
    mock_open.assert_called_with(expected_file_path, "wb")

    mock_assembler_linker.assert_called_once_with(mock_assembler_linker_config)

    mock_assembler_linker_instance.link.assert_called_once()
    mock_assembler_linker_instance.assemble_linked_files.assert_called_once_with(mock_server_path)


def test_create_download_failure(mock_server_path, mock_assembler_linker_config, mock_progress, mocker):
    """Test creating a server by downloading the JAR file (failure case)."""

    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch('requests.get', return_value=mock_response)

    mock_makedirs = mocker.patch('os.makedirs')

    handler = ServerHandler()

    with pytest.raises(Exception, match="Failed to download server."):
        handler.create(
            server_path=mock_server_path,
            server_version="1.19.4",
            source="DOWNLOAD",
            target="https://example.com/paper-1.19.4.jar",
            assembler_linker_config=mock_assembler_linker_config
        )

    mock_makedirs.assert_called_once_with(mock_server_path)

    requests.get.assert_called_once_with("https://example.com/paper-1.19.4.jar", stream=True)


def test_create_buildtools_success(mock_server_path, mock_assembler_linker_config, mock_progress, mocker):
    """Test creating a server using BuildTools (success case)."""

    mock_version = mocker.Mock()
    mock_version.__ge__ = lambda self, other: False
    mock_version.__gt__ = lambda self, other: False
    mock_version.__lt__ = lambda self, other: False
    mocker.patch('mcup.core.handlers.server_handler.Version.from_string', return_value=mock_version)

    mocker.patch('pathlib.Path.exists', return_value=False)

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.headers.get.return_value = "1000"
    mock_response.iter_content.return_value = [b"chunk1", b"chunk2"]
    mocker.patch('requests.get', return_value=mock_response)

    mock_open = mocker.patch('builtins.open', mocker.mock_open())

    mock_makedirs = mocker.patch('os.makedirs')
    mocker.patch('os.path.exists', return_value=True)

    mock_check_output = mocker.patch('subprocess.check_output', return_value='java version "17.0.1"')
    mock_run = mocker.patch('subprocess.run')

    mocker.patch('builtins.print')

    mock_assembler_linker = mocker.patch('mcup.core.handlers.server_handler.AssemblerLinker')
    mock_assembler_linker_instance = mock_assembler_linker.return_value

    mocker.patch('shutil.rmtree')
    mocker.patch('os.remove')

    mocker.patch('os.path.isfile', return_value=False)
    mocker.patch('os.path.isdir', return_value=False)

    handler = ServerHandler()

    handler.create(
        server_path=mock_server_path,
        server_version="1.19.4",
        source="BUILDTOOLS",
        target="spigot",
        assembler_linker_config=mock_assembler_linker_config
    )

    mock_makedirs.assert_called_once_with(mock_server_path)

    requests.get.assert_called_once_with(
        "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar",
        stream=True
    )

    expected_file_path = mock_server_path / "BuildTools.jar"
    mock_open.assert_called_with(expected_file_path, "wb")

    mock_check_output.assert_called_once_with(["java", "-version"], stderr=subprocess.STDOUT, text=True)

    mock_run.assert_called_once_with(
        ["java", "-jar", expected_file_path, "--compile", "spigot", "--rev", "1.19.4"],
        cwd=mock_server_path,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    mock_assembler_linker.assert_called_once_with(mock_assembler_linker_config)

    mock_assembler_linker_instance.link.assert_called_once()
    mock_assembler_linker_instance.assemble_linked_files.assert_called_once_with(mock_server_path)


def test_create_buildtools_download_failure(mock_server_path, mock_assembler_linker_config, mock_progress, mocker):
    """Test creating a server using BuildTools when download fails."""
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch('requests.get', return_value=mock_response)

    mock_makedirs = mocker.patch('os.makedirs')

    handler = ServerHandler()

    with pytest.raises(Exception, match="Failed to download Spigot BuildTools."):
        handler.create(
            server_path=mock_server_path,
            server_version="1.19.4",
            source="BUILDTOOLS",
            target="spigot",
            assembler_linker_config=mock_assembler_linker_config
        )

    mock_makedirs.assert_called_once_with(mock_server_path)

    requests.get.assert_called_once_with(
        "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar",
        stream=True
    )


def test_create_buildtools_jar_not_found(mock_server_path, mock_assembler_linker_config, mock_progress, mocker):
    """Test creating a server using BuildTools when the JAR file is not found after building."""
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.headers.get.return_value = "1000"
    mock_response.iter_content.return_value = [b"chunk1", b"chunk2"]
    mocker.patch('requests.get', return_value=mock_response)

    mocker.patch('builtins.open', mocker.mock_open())
    mocker.patch('os.makedirs')

    def mock_exists(path):
        if str(path).endswith("BuildTools.jar"):
            return True
        if str(path).endswith("spigot-1.19.4.jar"):
            return False
        return True

    mocker.patch('os.path.exists', side_effect=mock_exists)

    mocker.patch('subprocess.check_output', return_value='java version "17.0.1"')
    mock_run = mocker.patch('subprocess.run')

    handler = ServerHandler()

    with pytest.raises(FileNotFoundError, match="Server JAR file not found."):
        handler.create(
            server_path=mock_server_path,
            server_version="1.19.4",
            source="BUILDTOOLS",
            target="spigot",
            assembler_linker_config=mock_assembler_linker_config
        )

    expected_file_path = mock_server_path / "BuildTools.jar"
    mock_run.assert_called_once_with(
        ["java", "-jar", expected_file_path, "--compile", "spigot", "--rev", "1.19.4"],
        cwd=mock_server_path,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
