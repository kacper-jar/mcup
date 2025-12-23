# mcup

**mcup** is a command-line tool for quickly creating Minecraft servers.
Inspired by tools like `rustup` and `npm init`, `mcup` simplifies the setup process and allows for templated server creation with support for multiple server types (e.g., vanilla, Spigot).
Made for both advanced server managers and beginners setting up their first server.

## Features

- Fast server setup with a single command
- Template system for custom or reusable server setups
- Locker system for managing supported server versions and download links
- Designed for Linux (Also supports Windows and macOS)

## Installation

### Snap (Linux)

> [!WARNING]
> Support for the Snap package has been dropped.
>
> We have decided to discontinue Snap support due to significant maintenance overhead caused by the sandboxed
> environment and performance issues compared to native packages.
>
> Existing Snap installations will no longer receive updates. We strongly recommend migrating to the
> **.deb** or **.rpm** packages.

### APT / .deb (Linux)

> [!NOTE]
> An APT release is planned.
> In the meantime, please install mcup using the `.deb` file.

Install from a local `.deb` package (download from [GitHub Releases](https://github.com/kacper-jar/mcup/releases)):

```sh
sudo dpkg -i ./mcup_*.deb
sudo apt-get install -f
```

> [!IMPORTANT]
> Replace `./mcup_*.deb` with the actual path to your downloaded file.

### .rpm (Linux)

Install from a local `.rpm` package (download from [GitHub Releases](https://github.com/kacper-jar/mcup/releases)):

**Fedora/RHEL 8+/Rocky/Alma:**

```sh
sudo dnf install ./mcup_*.rpm
```

**Older RHEL/CentOS (6-7):**

```sh
sudo yum localinstall ./mcup_*.rpm
```

**openSUSE:**

```sh
sudo zypper install ./mcup_*.rpm
```

> [!IMPORTANT]
> Replace `./mcup_*.rpm` with the actual path to your downloaded file.

### Manual (All platforms)

Clone this repository and run the appropriate script:

```sh
git clone https://github.com/kacper-jar/mcup.git
cd mcup

# Run the appropriate script
./mcup.sh   # Linux / macOS
mcup.bat    # Windows
```

## Usage

Basic usage pattern:

```sh
mcup <command> [options]
```

### Commands

- `server create <server_type> <server_version> [path]` - Create a new Minecraft server in the specified path (defaults
  to current directory)
- `server list` - List all available server versions
- `template use <template_name> [path]` - Create a server based on a saved template
- `template create <template_name> ` - Create a new server template
- `template import <path>` - Import a template from a file
- `template export <template_name>` - Export a template to a file
- `template delete <template_name>` - Remove a stored template
- `template list` - List all stored templates
- `template refresh <template_name>` - Update a stored template with new download links from a locker file
- `update` - Update the locker file with the latest server metadata
- `about` - Display information about the current version of mcup

## Build

To build the project locally, clone this repository and run:

```sh
./build.sh
```

> [!NOTE]
> You can disable selected package(s) creation by passing the appropriate flag(s):
> * `--no-deb` - Skips building the `.deb` package
> * `--no-rpm` - Skips building the `.rpm` package

## Locker System

`mcup` maintains a list of supported server types and versions via a **locker file**, which contains metadata for
downloading and configuring different server flavors. (downloaded
from [GitHub repo](https://github.com/kacper-jar/mcup-locker-file))

## Project Structure

- `.github/` - GitHub-related configuration files
- `debian/` - Files for building the `.deb` package
- `mcup/` - Project source code
  - `mcup.core` - Main application logic code
  - `mcup.cli` - CLI UI code
  - `mcup.devtools` - Development tools to speed up development
- `rpm/` - Files for building the `.rpm` package

## Contributing

Contributions are welcome! Please follow guidelines in [CONTRIBUTING.md](https://github.com/kacper-jar/mcup/blob/master/CONTRIBUTING.md).

For major changes, open an issue first to discuss what you’d like to change.

## License

This project is licensed under the MIT License.

---
Made with ❤️ by [Kacper Jarosławski](https://github.com/kacper-jar)
