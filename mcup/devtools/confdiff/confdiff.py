import sys
from collections import OrderedDict
from pathlib import Path
import yaml


class ConfDiff:
    def _load_yaml(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def _compare_dicts(self, old, new, path=""):
        changes = []

        all_keys = set(old.keys()) | set(new.keys())
        for key in sorted(all_keys):
            current_path = f"{path}/{key}" if path else key

            if key not in old:
                changes.append(f"+ {current_path}: {new[key]}")
            elif key not in new:
                changes.append(f"- {current_path}: {old[key]}")
            else:
                old_val = old[key]
                new_val = new[key]

                if isinstance(old_val, dict) and isinstance(new_val, dict):
                    changes.extend(self._compare_dicts(old_val, new_val, current_path))
                elif old_val != new_val:
                    changes.append(f"= {current_path}: {new_val} (old value: {old_val})")

        return changes

    @staticmethod
    def run(args):
        configuration_files = args.configuration_files
        confdiff = ConfDiff()

        version_file_pairs = []
        for arg in configuration_files[1:]:
            if ':' not in arg:
                print(f"Error: Invalid argument format '{arg}'. Expected format: version:path")
                sys.exit(2)
            version, path_str = arg.split(":", 1)
            path = Path(path_str)
            if not path.exists():
                print(f"Error: File not found: {path}")
                sys.exit(3)
            version_file_pairs.append((version, path))

        versions_data = OrderedDict()
        for version, path in version_file_pairs:
            data = confdiff._load_yaml(path)
            if not isinstance(data, dict):
                print(f"Error: Top-level YAML structure must be a mapping (dictionary) in {path}")
                sys.exit(4)
            versions_data[version] = data

        prev_version = None
        prev_data = None
        for version, data in versions_data.items():
            if prev_data is not None:
                diffs = confdiff._compare_dicts(prev_data, data)
                if diffs:
                    print(f"Comparing {prev_version} → {version}")
                    print("-" * (len(f"Comparing {prev_version} → {version}")))
                    for diff in diffs:
                        print(diff)
                    print()
            prev_version = version
            prev_data = data
