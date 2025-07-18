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

### 📦 Snap (Linux)

Install from the Snap Store:

```sh
sudo snap install mcup
```

Or install from a local `.snap` file (download from [GitHub Releases](https://github.com/kacper-jar/mcup/releases)):

```sh
sudo snap install --dangerous ./mcup_*.snap
```

> [!IMPORTANT]
> Replace `./mcup_*.snap` with the actual path to your downloaded file.

### 🧊 APT / .deb (Linux)

> [!NOTE]
> An APT release is planned.
> In the meantime, please use the Snapcraft version or install mcup using the `.deb` file.

Install from a local `.deb` package (download from [GitHub Releases](https://github.com/kacper-jar/mcup/releases)):

```sh
sudo dpkg -i ./mcup_*.deb
sudo apt-get install -f
```

> [!IMPORTANT]
> Replace `./mcup_*.deb` with the actual path to your downloaded file.

### 🔧 Manual (All platforms)

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

- `server create [path]` – Create a new Minecraft server in the specified path (defaults to current directory)
- `template use <template_name> [path]` – Create a server based on a saved template
- `template create <template_name> ` – Create a new server template
- `template import <path>` – Import a template from a file
- `template export <template_name>` – Export a template to a file
- `template delete <template_name>` – Remove a stored template
- `template list` – List all stored templates
- `template refresh <template_name>` – Update a stored template with new download links from a locker file
- `update` – Update the locker file with the latest server metadata

## Build

To build the project locally, clone this repository and run:

```sh
./build.sh
```

> [!NOTE]
> You can disable Snap package creation by passing the `--skip-snap` flag:
> 
> ```sh
> ./build.sh --skip-snap
> ```

> [!IMPORTANT]
> If you're using LXD (only Snap builds), make sure your user is added to the `lxd` group:
> 
> ```sh
> sudo usermod -aG lxd $USER
> newgrp lxd
> ```

## Locker System

`mcup` maintains a list of supported server types and versions via a **locker file**, which contains metadata for downloading and configuring different server flavors.

### Locker Files

- `locker.json`: Main file with server data (downloaded from [GitHub repo](https://github.com/kacper-jar/mcup-locker-file))
- `locker-meta.json`: Local file storing `last_updated` to avoid unnecessary downloads

Locker updates check the last commit date on GitHub to determine if a new version should be downloaded.

## Project Structure

- `.github/` - GitHub-related configuration files
- `debian/` - Files for building the `.deb` package
- `mcup/` - Project source code
  - `mcup.core` – Main application logic code
  - `mcup.cli` – CLI UI code
  - `mcup.devtools` - Development tools to speed up development
- `snap/` - Files for building the `.snap` package

## Contributing

Contributions are welcome! Please follow guidelines in [CONTRIBUTING.md](https://github.com/kacper-jar/mcup/blob/master/CONTRIBUTING.md).

For major changes, open an issue first to discuss what you’d like to change.

## License

This project is licensed under the MIT License.

---
Made with ❤️ by [Kacper Jarosławski](https://github.com/kacper-jar)
