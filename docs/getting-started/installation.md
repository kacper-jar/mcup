# Installation

`mcup` is natively distributed and compiled uniquely across multiple platforms to make it as easy as possible to install.
The easiest way to install it is to grab the compiled binaries from the [GitHub Releases](https://github.com/kacper-jar/mcup/releases) page.

!!! note "macOS Users"
    There are no native macOS binaries available. The only way to install `mcup` on macOS is via the [Python Module](#python-module-universal) or by building from [Source](#manual-installation-from-source).

## Prerequisites

Before installing `mcup` and running Minecraft servers, ensure you have the following system requirements:

- **Java**: `mcup` manages Minecraft servers, which require Java to run. Please ensure you have the correct Java version installed for the Minecraft versions you intend to run (e.g., Java 25 for Minecraft 26.1+).

## Windows

**Setup Executable (Recommended):**

1. Download `mcup-windows-setup.exe` from the latest release.
2. Running the installer will automatically configure the application entirely through a wizard GUI and automatically append `mcup` to your system `PATH` variables.
3. Once finished, open your command prompt or PowerShell and run:
```cmd
mcup
```

**Standalone / Portable:**

If you don't have Administrator privileges, you can download the standalone executable (`mcup-windows.exe` or equivalent) or use the [Python Module](#python-module-universal) method.

## Linux

### Standalone Binary (distro-agnostic)

You can download the compiled native standalone binary that comes fully packed with everything needed to run `mcup`:

1. Download the linux `mcup` binary from [GitHub Releases](https://github.com/kacper-jar/mcup/releases).
2. Move it to your local bin directory and make it executable:
```sh
chmod +x ./mcup
sudo mv ./mcup /usr/local/bin/mcup
```

### Debian / Ubuntu (.deb)

!!! note
    An official APT release is planned down the line. In the meantime, please install using the provided `.deb` package.

1. Download the latest `.deb` package.
2. Install it using `dpkg`:
```sh
sudo dpkg -i ./mcup_*.deb
sudo apt-get install -f
```

### RPM-based Distributions (.rpm)

Download the latest `.rpm` package and install natively depending on your architecture:

**Fedora / RHEL 8+ / Rocky / Alma:**
```sh
sudo dnf install ./mcup_*.rpm
```

**Older RHEL / CentOS (6-7):**
```sh
sudo yum localinstall ./mcup_*.rpm
```

**openSUSE:**
```sh
sudo zypper install ./mcup_*.rpm
```

## Python Module (Universal)

If you prefer installing `mcup` directly into an active Python environment on any OS (macOS, Linux, Windows), 
download the latest `.whl` wheel from the active repository release.

Install it using pip from a command prompt:

```sh
pip install ./mcup-*.whl
```

!!! tip
    If the `pip` command is not available, try using `python3 -m pip install ...` instead.

!!! warning "PATH Variable"
    If you install via `pip`, the `mcup` binary is placed in your Python environment's scripts directory (e.g., `~/.local/bin` on Linux/macOS or `Scripts` on Windows). Ensure this directory is in your system's `PATH` to avoid "Command not found" errors.

## Manual Installation (From Source)

You can assemble and execute `mcup` strictly from the underlying source files by downloading the repository directly.

**Prerequisites:**

- [Git](https://git-scm.com/)
- [Python 3.10+](https://www.python.org/)

**Steps:**

1. Clone the repository:
```sh
git clone https://github.com/kacper-jar/mcup.git
cd mcup
```

2. Install the package locally:
```sh
pip install .
```

3. Run mcup:
```sh
mcup <args>
```

!!! tip
    If you don't want to install the package system-wide during source execution, you can completely sidestep installation and run `mcup` directly as a Python module:
    ```sh
    python3 -m mcup <args>
    ```

## Verification

To verify that `mcup` was successfully installed, open a fresh terminal or command prompt and run:
```sh
mcup --version
```
It should print the application version. You can also view all available commands by running `mcup --help`.

## What's Next?
- [Creating Your First Server](creating-first-server.md)
