from dataclasses import dataclass


@dataclass
class Version:
    """Class representing a semantic version with major, minor, and patch components."""
    major: int
    minor: int
    patch: int

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
        """Get the version as a string in the format 'major.minor.patch'."""
        return f"{self.major}.{self.minor}.{self.patch}"


LATEST_VERSION = Version(1, 21, 5)
