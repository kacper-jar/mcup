from mcup.core.utils.locker import LockerManager


class UpdateCommand:
    @staticmethod
    def run(args):
        """Handles 'mcup update' command."""
        LockerManager().update_locker()
