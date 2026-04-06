# Installation

`mcup` is natively distributed and compiled uniquely across multiple platforms to make it as easy as possible to install.
The easiest way to install it is to grab the compiled binaries from the [GitHub Releases](https://github.com/kacper-jar/mcup/releases) page.

## Prerequisites

Before installing `mcup` and running Minecraft servers, ensure you have the following system requirements:

- **Java**: `mcup` manages Minecraft servers, which require Java to run. Please ensure you have the correct Java version
installed for the Minecraft versions you intend to run (e.g., Java 17 for Minecraft 1.18+, Java 21 for 1.20.5+ or Java 
25 for 26.1+).

## Windows

**Setup Executable (Recommended):**

1. Download `mcup-*-windows-setup.exe` from [GitHub Releases](https://github.com/kacper-jar/mcup/releases).
2. Running the installer will automatically configure the application entirely through a wizard GUI and automatically
append `mcup` to your system `PATH` variables.
3. Once finished, open your command prompt or PowerShell and run:
```cmd
mcup
```

**Standalone / Portable:**

If you don't have Administrator privileges, you can use the standalone portable build instead:

1. Download `mcup-*-windows-amd64.zip` from [GitHub Releases](https://github.com/kacper-jar/mcup/releases).
2. Extract the archive to a folder of your choice.
3. Optionally, add that folder to your system `PATH` to use `mcup` from any terminal.
4. Run `mcup.exe` directly, or from your terminal:
```cmd
mcup
```

Alternatively, you can use the [Python Module](#python-module-universal) method.

## macOS

`mcup` provides native standalone binaries for macOS, supporting both Intel and Apple Silicon architectures.

1. Download the appropriate `.zip` for your architecture from [GitHub Releases](https://github.com/kacper-jar/mcup/releases):
    - **Apple Silicon (M1, M2, etc.):** `mcup-*-macos-arm64.zip`
    - **Intel:** `mcup-*-macos-x64.zip`
2. Extract the archive and move the binary to your executable path:
```sh
unzip mcup-*-macos-*.zip
chmod +x ./mcup
sudo mv ./mcup /usr/local/bin/mcup
```

## Linux

### Standalone Binary (distro-agnostic)

You can download the compiled native standalone binary that comes fully packed with everything needed to run `mcup`:

1. Download the appropriate `.zip` for your architecture from [GitHub Releases](https://github.com/kacper-jar/mcup/releases):
    - **AMD64 / x86_64:** `mcup-*-linux-amd64.zip`
    - **ARM64 / AArch64:** `mcup-*-linux-arm64.zip`
2. Extract the archive and make the binary executable:
```sh
unzip mcup-*-linux-*.zip
chmod +x ./mcup
sudo mv ./mcup /usr/local/bin/mcup
```

### Debian / Ubuntu (.deb)

1. Download the appropriate `.deb` from [GitHub Releases](https://github.com/kacper-jar/mcup/releases):
    - **AMD64:** `mcup_*_amd64.deb`
    - **ARM64:** `mcup_*_arm64.deb`
2. Install it using `dpkg`:
```sh
sudo dpkg -i mcup_*_*.deb
sudo apt-get install -f
```

### RPM-based Distributions (.rpm)

Download the `.rpm` from [GitHub Releases](https://github.com/kacper-jar/mcup/releases) 
and install natively depending on your distribution:

- **AMD64 / x86_64:** `mcup-*-1.x86_64.rpm`
- **ARM64 / AArch64:** `mcup-*-1.aarch64.rpm`

**Fedora / RHEL 8+ / Rocky / Alma:**
```sh
sudo dnf install mcup-*.rpm
```

**Older RHEL / CentOS (6-7):**
```sh
sudo yum localinstall mcup-*.rpm
```

**openSUSE:**
```sh
sudo zypper install mcup-*.rpm
```

### Arch Linux (.pkg.tar.zst)

1. Download the appropriate package from [GitHub Releases](https://github.com/kacper-jar/mcup/releases):
    - **AMD64 / x86_64:** `mcup-*-1-x86_64.pkg.tar.zst`
    - **ARM64 / AArch64:** `mcup-*-1-aarch64.pkg.tar.zst`
2. Install it using `pacman`:
```sh
sudo pacman -U mcup-*-1-*.pkg.tar.zst
```

## Python Module (Universal)

If you prefer installing `mcup` directly into an active Python environment on any OS (macOS, Linux, Windows), 
download the latest `.whl` wheel from [GitHub Releases](https://github.com/kacper-jar/mcup/releases).

Install it using pip from a command prompt:

```sh
pip install mcup-*-py3-none-any.whl
```

!!! tip
    If the `pip` command is not available, try using `python3 -m pip install ...` instead.

!!! warning "PATH Variable"
    If you install via `pip`, the `mcup` binary is placed in your Python environment's scripts directory
    (e.g., `~/.local/bin` on Linux/macOS or `Scripts` on Windows). 
    Ensure this directory is in your system `PATH` to avoid "Command not found" errors.

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
    If you don't want to install the package system-wide during source execution, you can completely sidestep
    installation and run `mcup` directly as a Python module:
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
