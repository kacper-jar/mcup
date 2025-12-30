# Installation

`mcup` can be installed on Linux using package managers, or manually on any platform (Linux, macOS, Windows) by cloning
the repository.

## Linux

### Snap

!!! warning "Snap Support Dropped"
**Support for the Snap package has been dropped.**

    We have decided to discontinue Snap support due to significant maintenance overhead caused by the sandboxed environment and performance issues compared to native packages.
    
    Existing Snap installations will no longer receive updates. We strongly recommend migrating to the **.deb** or **.rpm** packages.

### Debian / Ubuntu (.deb)

!!! note
An APT release is planned. In the meantime, please install mcup using the `.deb` file.

1. Download the latest `.deb` package from [GitHub Releases](https://github.com/kacper-jar/mcup/releases).
2. Install it using `dpkg`:

   ```sh
   sudo dpkg -i ./mcup_*.deb
   sudo apt-get install -f
   ```

   !!! important
   Replace `./mcup_*.deb` with the actual path to your downloaded file.

### RPM-based Distributions (.rpm)

Download the latest `.rpm` package from [GitHub Releases](https://github.com/kacper-jar/mcup/releases).

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

!!! important
Replace `./mcup_*.rpm` with the actual path to your downloaded file.

## Manual Installation (All Platforms)

You can install `mcup` manually by cloning the repository. This works on Linux, macOS, and Windows.

**Prerequisites:**

- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/)

**Steps:**

1. Clone the repository:

   ```sh
   git clone https://github.com/kacper-jar/mcup.git
   cd mcup
   ```

2. Run the appropriate startup script:

   === "Linux / macOS"
   ```sh
   ./mcup.sh <args>
   ```

   === "Windows"
   ```sh
   mcup.bat <args>
   ```
