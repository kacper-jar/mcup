# Server Management

The `server` command group allows you to create new Minecraft servers and list available server types and versions.

## Create a Server

Create a new Minecraft server with the specified type and version.

```bash
mcup server create <server_type> <server_version> [path] [flags]
```

### Arguments

| Argument         | Description                                                                                         |
|:-----------------|:----------------------------------------------------------------------------------------------------|
| `server_type`    | The type of server to create (e.g., `paper`, `fabric`).                                             |
| `server_version` | The version of the server to install (e.g., `1.17`, `1.20.1`).                                      |
| `path`           | (Optional) The directory where the server will be created. Defaults to the current directory (`.`). |

### Flags

| Flag                | Description                                                            |
|:--------------------|:-----------------------------------------------------------------------|
| `--no-configs`      | Skip the generation of configuration files (e.g. `server.properties`). |
| `--no-defaults`     | Prompt for all configuration values, ignoring any defaults.            |
| `--all-defaults`    | Use default values for all configuration options without prompting.    |
| `--skip-java-check` | Skip the check for Java installation and version compatibility.        |

### Examples

Create a Paper 1.20.1 server in the current directory:

```bash
mcup server create paper 1.20.1
```

Create a Paper 1.20.1 server in a specific directory:

```bash
mcup server create paper 1.20.1 ./my-server
```

Create a Paper 1.20.1 server using all default configuration values:

```bash
mcup server create paper 1.20.1 --all-defaults
```

## List Available Servers

List all available server types and their supported versions from the local locker.

```bash
mcup server list
```

This command will output a list of server types (like `spigot`, `paper`, `fabric`) and the versions available for each.
