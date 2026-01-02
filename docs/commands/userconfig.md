# User Configuration

The `config` command group allows you to manage global user configuration settings for `mcup`. These settings persist
across sessions.

## Known Configuration Keys

| Key                    | Description                                                        | Default Value  |
|:-----------------------|:-------------------------------------------------------------------|:---------------|
| `java.path`            | The path to the Java executable to use for running servers.        | `java`         |
| `logging.level`        | The logging level for the CLI output (e.g., `DEBUG`, `INFO`).      | `INFO`         |
| `devtools.enabled`     | Enable developer tools commands (`confdiff`, `lockermgr`).         | `false`        |
| `advancedmode.enabled` | Enable advanced fields in the server configuration wizard.         | `false`        |
| `locker.remote`        | The URL of the remote locker file to use for updates.              | (Standard URL) |
| `locker.branch`        | The branch of the remote locker repository to use (if applicable). | `main`         |

## Get Configuration

Retrieve the value of a specific configuration key.

```bash
mcup config get <key>
```

### Arguments

| Argument | Description                        |
|:---------|:-----------------------------------|
| `key`    | The configuration key to retrieve. |

### Examples

Get the current Java path:

```bash
mcup config get java.path
```

## Set Configuration

Set the value for a specific configuration key.

```bash
mcup config set <key> <value>
```

### Arguments

| Argument | Description                     |
|:---------|:--------------------------------|
| `key`    | The configuration key to set.   |
| `value`  | The value to assign to the key. |

### Examples

Set the Java path to a specific executable:

```bash
mcup config set java.path /usr/bin/java17
```

Enable developer tools:

```bash
mcup config set devtools.enabled true
```

## Remove Configuration

Remove a specific configuration key and its value. This will revert the key to its default value if one exists.

```bash
mcup config remove <key>
```

### Arguments

| Argument | Description                      |
|:---------|:---------------------------------|
| `key`    | The configuration key to remove. |

### Examples

Remove the custom Java path setting:

```bash
mcup config remove java.path
```

## Clear Configuration

Clear all user configuration settings, resetting them to defaults.

```bash
mcup config clear
```

## List Configuration

List all current configuration keys and their values.

```bash
mcup config list
```
