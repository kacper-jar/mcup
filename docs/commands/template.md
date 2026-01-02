# Template Management

The `template` command group allows you to manage server templates, which pre-configure server settings and files for
quick deployment.

## Create a Template

Create a new template based on a specific server type and version. This will prompt you to configure the server settings
which will be saved into the template.

```bash
mcup template create <server_type> <server_version> <template_name>
```

### Arguments

| Argument         | Description                                          |
|:-----------------|:-----------------------------------------------------|
| `server_type`    | The type of server for the template (e.g., `paper`). |
| `server_version` | The version of the server (e.g., `1.20.1`).          |
| `template_name`  | A unique name for your new template.                 |

### Examples

Create a template named `survival-1.20` for a Paper 1.20.1 server:

```bash
mcup template create paper 1.20.1 survival-1.20
```

## Use a Template

Create a new server using an existing template.

```bash
mcup template use <template_name> [path]
```

### Arguments

| Argument        | Description                                                                                         |
|:----------------|:----------------------------------------------------------------------------------------------------|
| `template_name` | The name of the template to use.                                                                    |
| `path`          | (Optional) The directory where the server will be created. Defaults to the current directory (`.`). |

### Examples

Create a server from the `survival-1.20` template in the current directory:

```bash
mcup template use survival-1.20
```

Create a server from the `survival-1.20` template in a specific directory:

```bash
mcup template use survival-1.20 ./my-server
```

## List Templates

List all available templates.

```bash
mcup template list
```

## Import a Template

Import a template from a JSON file.

```bash
mcup template import <path>
```

### Arguments

| Argument | Description                               |
|:---------|:------------------------------------------|
| `path`   | Path to the template JSON file to import. |

### Examples

Import a template from `backup.json`:

```bash
mcup template import ./backup.json
```

## Export a Template

Export an existing template to a JSON file.

```bash
mcup template export <template_name> <destination>
```

### Arguments

| Argument        | Description                                                   |
|:----------------|:--------------------------------------------------------------|
| `template_name` | The name of the template to export.                           |
| `destination`   | The destination path or directory for the exported JSON file. |

### Examples

Export the `survival-1.20` template to `backup.json`:

```bash
mcup template export survival-1.20 ./backup.json
```

## Delete a Template

Delete an existing template.

```bash
mcup template delete <template_name>
```

### Arguments

| Argument        | Description                         |
|:----------------|:------------------------------------|
| `template_name` | The name of the template to delete. |

### Examples

Delete the `survival-1.20` template:

```bash
mcup template delete survival-1.20
```

## Refresh a Template

Update the download links and metadata within a template to match the current locker version.

```bash
mcup template refresh <template_name>
```

### Arguments

| Argument        | Description                          |
|:----------------|:-------------------------------------|
| `template_name` | The name of the template to refresh. |

### Examples

Refresh the `survival-1.20` template:

```bash
mcup template refresh survival-1.20
```
