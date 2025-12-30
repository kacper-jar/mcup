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

## Delete a Template

Delete an existing template.

```bash
mcup template delete <template_name>
```

### Arguments

| Argument        | Description                         |
|:----------------|:------------------------------------|
| `template_name` | The name of the template to delete. |

## Refresh a Template

Update the download links and metadata within a template to match the current locker version.

```bash
mcup template refresh <template_name>
```

### Arguments

| Argument        | Description                          |
|:----------------|:-------------------------------------|
| `template_name` | The name of the template to refresh. |
