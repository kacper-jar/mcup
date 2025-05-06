from dataclasses import dataclass


@dataclass
class Version:
    """Class representing a semantic version with major, minor, and patch components."""
    major: int
    minor: int
    patch: int = 0

    @classmethod
    def from_string(cls, version_str: str) -> "Version":
        """Create a Version object from a string.

        Supports formats like "1.8" (patch will be 0) and "1.8.2".
        """
        parts = version_str.split(".")
        major = int(parts[0])
        minor = int(parts[1])
        patch = int(parts[2]) if len(parts) > 2 else 0
        return cls(major, minor, patch)

    def __ge__(self, other):
        """Check if this version is greater than or equal to another version."""
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) >= (other.major, other.minor, other.patch)

    def __gt__(self, other):
        """Check if this version is greater than another version."""
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) > (other.major, other.minor, other.patch)

    def __le__(self, other):
        """Check if this version is less than or equal to another version."""
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) <= (other.major, other.minor, other.patch)

    def __lt__(self, other):
        """Check if this version is less than another version."""
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)

    def __eq__(self, other):
        """Check if this version is equal to another version."""
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def get_major(self) -> int:
        """Get the major version component."""
        return self.major

    def get_minor(self) -> int:
        """Get the minor version component."""
        return self.minor

    def get_patch(self) -> int:
        """Get the patch version component."""
        return self.patch

    def get_string(self) -> str:
        """Get the version as a string.

        If patch is 0, returns 'major.minor'.
        Otherwise, returns 'major.minor.patch'.
        """
        if self.patch == 0:
            return f"{self.major}.{self.minor}"
        return f"{self.major}.{self.minor}.{self.patch}"


LATEST_VERSION = Version(1, 21, 5)
