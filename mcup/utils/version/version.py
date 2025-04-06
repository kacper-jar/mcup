from dataclasses import dataclass


@dataclass
class Version:
    major: int
    minor: int
    patch: int

    def __ge__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) >= (other.major, other.minor, other.patch)

    def __le__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) <= (other.major, other.minor, other.patch)

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def get_major(self) -> int:
        return self.major

    def get_minor(self) -> int:
        return self.minor

    def get_patch(self) -> int:
        return self.patch

    def get_string(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

LATEST_VERSION = Version(1, 13, 2)
