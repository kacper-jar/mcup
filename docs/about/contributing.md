# Contributing

Thank you for your interest in contributing to **mcup**! We appreciate your help in making this project better. This
guide will help you get started with setting up your development environment, making changes, and submitting a pull
request.

## Getting Started

### Fork the Repository

First, create a fork of the [mcup repository](https://github.com/kacper-jar/mcup) on GitHub. This gives you your own
copy of the project to work on.

### Clone Your Fork

Clone your forked repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/mcup.git
cd mcup
```

### Set Up Development Environment

It is recommended to use a virtual environment to manage dependencies:

=== "Linux / macOS"
    ```bash
    # Create a virtual environment
    python3 -m venv .venv
    
    # Activate the virtual environment
    source .venv/bin/activate
    ```

=== "Windows"
    ```bat
    # Create a virtual environment
    python -m venv .venv

    # Activate the virtual environment
    .venv/Scripts/activate
    ```

Install the project dependencies and the project itself in editable mode:

```bash
pip install -e .
```

## Project Structure

Here is a quick overview of the project's structure to help you navigate the codebase:

- `.github/`: GitHub-related configuration files (workflows, issue templates).
- `debian/`: Files for building the `.deb` package.
- `mcup/`: The main source code directory.
    - `mcup.core`: Core application logic (handlers, utils, status codes).
    - `mcup.cli`: Command-line interface code (commands, UI components).
    - `mcup.devtools`: Development tools to assist with testing and maintenance.
- `rpm/`: Files for building the `.rpm` package.
- `docs/`: Documentation files (MkDocs).

## Running Locally

You can run the CLI directly from the source code to test your changes.

### Using Entry Point (Recommended)

The easiest way to run the CLI is by using the installed `mcup` command within your virtual environment.
Since you installed the package in editable mode (`pip install -e .`), any changes you make to the code are immediately
reflected.

1. Ensure your virtual environment is activated.
2. Run the command:

```bash
mcup [command]
```

### Using Helper Scripts

We provide helper scripts that handle the execution for you, which can be useful if you haven't activated your virtual
environment manually.

=== "Linux / macOS"
    ```bash
    ./mcup.sh [command]
    ```

=== "Windows"
    ```bat
    mcup.bat [command]
    ```

### Using Python Module

Alternatively, you can run the package directly using Python:

```bash
python3 -m mcup [command]
```

## Building the Project

To build the distributable packages (DEB, RPM), use the provided build script.

```bash
./build.sh
```

This will generate the packages in the `dist` directory.

!!! note
    You can skip specific package builds using flags:

    *   `--skip-deb`: Skip building the Debian package.
    *   `--skip-rpm`: Skip building the RPM package.

## Commit Message Convention

We follow the **Conventional Commits** style to keep our commit history clear and easy to understand.

Each commit message should start with a **type prefix**, followed by a colon and a short description:

```
<type>: <short description>
```

### Common Types

| Type         | Description                                | Example                                          |
|:-------------|:-------------------------------------------|:-------------------------------------------------|
| **feat**     | A new feature                              | `feat: add support for YAML config loading`      |
| **fix**      | A bug fix                                  | `fix: prevent crash when config file is missing` |
| **docs**     | Documentation only changes                 | `docs: update usage section in README.md`        |
| **style**    | Code style changes (formatting, etc)       | `style: reformat code with Black`                |
| **refactor** | Refactoring code without changing behavior | `refactor: extract validation logic`             |
| **test**     | Adding or updating tests                   | `test: add unit tests for CLI argument parser`   |
| **build**    | Changes to build scripts or dependencies   | `build: upgrade rich library`                    |
| **chore**    | Other changes                              | `chore: update license year`                     |

### Optional Scope

You can optionally specify a scope in parentheses to indicate which part of the codebase is affected:

```
fix(config): handle missing default values
```

### How to Write a Good Commit Message

- Keep the message concise (under 72 characters).
- Use the imperative mood ("fix bug" not "fixed bug").
- Explain *what* and *why* briefly.

## Submitting a Pull Request

1. Create a new branch for your feature or fix: `git checkout -b feat/my-new-feature`.
2. Make your changes and test them locally.
3. Commit your changes following the [Commit Message Convention](#commit-message-convention).
4. Push your branch to your fork: `git push origin feat/my-new-feature`.
5. Open a Pull Request on the main repository.
6. Provide a clear description of your changes and why they are necessary.

We will review your PR and provide feedback. Thank you for contributing!
