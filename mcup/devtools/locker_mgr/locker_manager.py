import json
from datetime import datetime, timezone
from pathlib import Path

from mcup.cli.language import Language
from mcup.core.status import StatusCode
from mcup.core.utils.locker import LockerUpdater
from mcup.core.utils.path import PathProvider


class LockerManager:
    @staticmethod
    def _get_locker_file():
        """Get the path to the locker file."""
        return PathProvider().get_config_path() / "locker.json"

    @staticmethod
    def _get_locker_meta_file():
        """Get the path to the locker file."""
        return PathProvider().get_config_path() / "locker-meta.json"

    @staticmethod
    def _get_bool(value):
        if value.lower() in {'false', '0', 'no', 'off'}:
            return False
        elif value.lower() in {'true', '1', 'yes', 'on'}:
            return True
        else:
            raise ValueError("Invalid value for boolean.")

    @staticmethod
    def load_locker():
        """Load the locker.json file."""
        language = Language()
        locker = LockerUpdater()

        update_occurred = False
        for status in locker.load_locker():
            match status.status_code:
                case StatusCode.INFO_LOCKER_MODIFIED:
                    print(language.get_string("INFO_LOCKER_MODIFIED"))
                case StatusCode.INFO_LOCKER_USING_REMOTE:
                    print(language.get_string("INFO_LOCKER_USING_REMOTE", status.status_details['remote_url'],
                                              status.status_details['branch']))
                case StatusCode.INFO_LOCKER_UP_TO_DATE:
                    print(language.get_string("INFO_LOCKER_UP_TO_DATE"))
                case StatusCode.INFO_LOCKER_UPDATING:
                    print(language.get_string("INFO_LOCKER_UPDATING"))
                    update_occurred = True
                case StatusCode.ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED:
                    print(language.get_string("ERROR_LOCKER_RETRIEVE_LATEST_TIMESTAMP_FAILED",
                                              status.status_details))
                    raise Exception()
                case StatusCode.ERROR_LOCKER_META_READ_FAILED:
                    print(language.get_string("ERROR_LOCKER_META_READ_FAILED", status.status_details))
                    raise Exception()
                case StatusCode.ERROR_LOCKER_DOWNLOAD_FAILED:
                    print(language.get_string("ERROR_LOCKER_DOWNLOAD_FAILED", status.status_details))
                    raise Exception()
                case StatusCode.ERROR_LOCKER_META_UPDATE_FAILED:
                    print(language.get_string("ERROR_LOCKER_META_UPDATE_FAILED", status.status_details))
                    raise Exception()
                case StatusCode.SUCCESS:
                    if update_occurred:
                        print(language.get_string("SUCCESS_LOCKER"))
                    return status.status_details
        return None

    @staticmethod
    def save_locker(locker_data, path=None):
        """Save the locker data to locker.json."""
        if path is None:
            locker_file = LockerManager._get_locker_file()
            meta_file = LockerManager._get_locker_meta_file()
        else:
            locker_file = Path(path)
            meta_file = None

        with open(locker_file, 'w') as l_file:
            json.dump(locker_data, l_file, indent=4)

        if meta_file is not None:
            with open(meta_file, 'r') as m_file:
                meta = json.load(m_file)
                remote_url = meta.get("remote")
                branch = meta.get("branch")

            with open(meta_file, 'w') as m_file:
                meta = {
                    "last_updated": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                    "is_modified": True,
                    "remote": remote_url,
                    "branch": branch
                }

                json.dump(meta, m_file, indent=4)

    @staticmethod
    def initialize_locker(args):
        """Initialize locker.json with an empty structure."""
        locker_file = LockerManager._get_locker_file()
        print(f"Creating a new locker file at {locker_file}...")
        locker_data = {"servers": {}}
        LockerManager.save_locker(locker_data)

    @staticmethod
    def add_server(args):
        """Add a new server type."""
        server_type = args.server_type
        locker_data = LockerManager.load_locker()

        if server_type in locker_data["servers"]:
            print(f"Server type {server_type} already exists.")
        else:
            locker_data["servers"][server_type] = []
            print(f"Server type {server_type} added.")
            LockerManager.save_locker(locker_data)

    @staticmethod
    def add_version(args):
        """Add a new version to a server type."""
        server_type = args.server_type
        version = args.version

        locker_data = LockerManager.load_locker()

        if server_type not in locker_data["servers"]:
            print(f"Server type {server_type} does not exist. Please add it first.")
            return

        versions = locker_data["servers"][server_type]
        if any(v['version'] == version for v in versions):
            print(f"Version {version} already exists for {server_type}.")
        else:
            source = None

            if args.server_url:
                source = "DOWNLOAD"

            if args.installer_url:
                if not args.installer_args:
                    print("--installer-url argument requires --installer-args argument.")
                    return
                source = "INSTALLER"

            if source is None:
                print("No valid source type detected. Must provide --server-url or --installer-url.")
                return

            if source == "DOWNLOAD":
                new_version = {
                    "version": version,
                    "source": "DOWNLOAD",
                    "server_url": args.server_url,
                    "supports_plugins": args.supports_plugins,
                    "supports_mods": args.supports_mods,
                    "configs": args.configs,
                    "cleanup": args.cleanup
                }
            elif source == "INSTALLER":
                new_version = {
                    "version": version,
                    "source": "INSTALLER",
                    "installer_url": args.installer_url,
                    "installer_args": args.installer_args,
                    "supports_plugins": args.supports_plugins,
                    "supports_mods": args.supports_mods,
                    "configs": args.configs,
                    "cleanup": args.cleanup
                }

            versions.append(new_version)
            print(f"Version {version} added to {server_type}.")
            LockerManager.save_locker(locker_data)

    @staticmethod
    def update_version(args):
        """Update the URL for an existing version."""
        server_type = args.server_type
        version = args.version

        locker_data = LockerManager.load_locker()

        if server_type not in locker_data["servers"]:
            print(f"Server type {server_type} does not exist.")
            return

        versions = locker_data["servers"][server_type]
        for v in versions:
            if v['version'] == version:
                if args.server_url is not None:
                    if 'server_url' in v:
                        v['server_url'] = args.server_url
                    else:
                        print("Field 'server_url' does not exist in this entry. It might be other source type. "
                              "Skipping this value...")
                if args.installer_url is not None:
                    if 'installer_url' in v:
                        v['installer_url'] = args.installer_url
                    else:
                        print("Field 'installer_url' does not exist in this entry. It might be other source type. "
                              "Skipping this value...")
                if args.installer_args is not None:
                    if 'installer_args' in v:
                        v['installer_args'] = args.installer_args
                    else:
                        print("Field 'installer_args' does not exist in this entry. It might be other source type. "
                              "Skipping this value...")
                if args.supports_plugins is not None:
                    v['supports_plugins'] = LockerManager._get_bool(args.supports_plugins)
                if args.supports_mods is not None:
                    v['supports_mods'] = LockerManager._get_bool(args.supports_mods)
                if args.configs is not None:
                    v['configs'] = args.configs
                if args.cleanup is not None:
                    v['cleanup'] = args.cleanup
                print(f"Version {version} updated for {server_type}.")
                LockerManager.save_locker(locker_data)
                return
        print(f"Version {version} not found for {server_type}.")

    @staticmethod
    def remove_version(args):
        """Remove a version from a server type."""
        server_type = args.server_type
        version = args.version

        locker_data = LockerManager.load_locker()

        if server_type not in locker_data["servers"]:
            print(f"Server type {server_type} does not exist.")
            return

        versions = locker_data["servers"][server_type]
        versions = [v for v in versions if v['version'] != version]
        locker_data["servers"][server_type] = versions
        print(f"Version {version} removed from {server_type}.")
        LockerManager.save_locker(locker_data)

    @staticmethod
    def list_locker(args):
        """List all server types and versions formated."""
        locker_data = LockerManager.load_locker()

        if not locker_data["servers"]:
            print("No server types found.")
            return

        for server_type, versions in locker_data["servers"].items():
            print(f"Server Type: {server_type}")
            if not versions:
                print("  No versions available.")
            for version in versions:
                print(f"  Version: {version['version']}")
                print(f"    Source: {version['source']}")
                if version['source'] == "DOWNLOAD":
                    print(f"    URL: {version['server_url']}")
                if version['source'] == "INSTALLER":
                    print(f"    Installer URL: {version['installer_url']}")
                    print(f"    Installer Arguments: {version['installer_args']}")
                print(f"    Supports Plugins: {'Yes' if version['supports_plugins'] else 'No'}")
                print(f"    Supports Mods: {'Yes' if version['supports_mods'] else 'No'}")
                print(f"    Configs: {version['configs']}")
                print(f"    Cleanup: {version['cleanup']}")
            print("-" * 40)

    @staticmethod
    def export_locker(args):
        """Export the locker file."""
        destination = Path(args.destination)

        locker_path = PathProvider().get_config_path() / "locker.json"

        if not locker_path.exists():
            print(f'Locker file "{locker_path}" does not exist.')
            return

        try:
            destination.parent.mkdir(parents=True, exist_ok=True)

            locker_data = LockerManager.load_locker()
            LockerManager.save_locker(locker_data, destination)

            print(f"Locker file exported successfully to {destination}.")
        except Exception as e:
            print(f"Failed to export locker file: {e}")
