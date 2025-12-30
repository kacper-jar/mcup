# User Configuration

The `config` command group allows you to manage global user configuration settings for `mcup`. These settings persist
across sessions.

## Get Configuration

Retrieve the value of a specific configuration key.

```bash
mcup config get <key>
```

### Arguments

| Argument | Description                        |
|:---------|:-----------------------------------|
| `key`    | The configuration key to retrieve. |

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

## Remove Configuration

Remove a specific configuration key and its value.

```bash
mcup config remove <key>
```

### Arguments

| Argument | Description                      |
|:---------|:---------------------------------|
| `key`    | The configuration key to remove. |

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
