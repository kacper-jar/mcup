# Contributing to This Project

Thanks for your interest in contributing! This document outlines how you can help make the project better, including how to write commit messages.

---

## Commit Message Convention

We follow the **Conventional Commits** style to keep our commit history clear and easy to understand.

### Commit Message Format

Each commit message should start with a **type prefix**, followed by a colon and a short description:

```
<type>: <short description>
```

### Common Types


| Type         | Description                                          | Example                                               |
|--------------|------------------------------------------------------|-------------------------------------------------------|
| **feat**     | A new feature                                        | `feat: add support for YAML config loading`           |
| **fix**      | A bug fix                                            | `fix: prevent crash when config file is missing`      |
| **docs**     | Documentation only changes                           | `docs: update usage section in README.md`             |
| **style**    | Code style changes (e.g. formatting, spacing)        | `style: reformat code with Black`                     |
| **refactor** | Refactoring code without changing behavior           | `refactor: extract validation logic to helper module` |
| **perf**     | A code change that improves performance              | `perf: reduce memory usage during data processing`    |
| **test**     | Adding or updating tests                             | `test: add unit tests for CLI argument parser`        |
| **build**    | Changes to build scripts or dependencies             | `build: add poetry support for dependency management` |
| **ci**       | Changes to CI/CD configuration                       | `ci: run tests on Python 3.12 in GitHub Actions`      |
| **chore**    | Other changes that don’t modify source or test files | `chore: update license year to 2025`                  |
| **revert**   | Reverts a previous commit                            | `revert: feat: add YAML config support`               |                                                            | `revert: feat: add user login`                 |

### Optional Scope

You can optionally specify a scope in parentheses to indicate which part of the codebase is affected:

```
fix(config): handle missing default values
```

---

## How to Write a Good Commit Message

- Keep the message concise (under 72 characters).
- Use the imperative mood ("fix bug" not "fixed bug" or "fixes bug").
- Explain *what* and *why* briefly, not just *how*.

---

## General Contribution Guidelines

- **Fork the repository** and create your feature branch from `main`.
- **Write clear, concise commit messages** as described above.
- **Test your changes** thoroughly before submitting.
- **Open a Pull Request** explaining what you’ve changed and why.
- Be respectful and open to feedback.

---

Thanks again for contributing! If you have any questions, feel free to ask.

---

*This project uses [Conventional Commits](https://www.conventionalcommits.org/) for commit message guidelines.*