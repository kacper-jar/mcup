# Update Management

The `update` command manually triggers an update of the internal locker file, which contains the definitions for
available server types, versions, and download links.

## Update Locker

Update the local locker file to the latest version from the remote repository.

```bash
mcup update [flags]
```

### Flags

| Flag      | Description                                                                 |
|:----------|:----------------------------------------------------------------------------|
| `--force` | Force the update even if the local locker is already considered up-to-date. |

### Examples

Standard update check:

```bash
mcup update
```

Force an update:

```bash
mcup update --force
```
