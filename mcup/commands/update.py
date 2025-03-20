from mcup.utils import LockerUpdater

class UpdateCommand:
    @staticmethod
    def run(args):
        """Handles 'mcup update' command."""
        LockerUpdater().update_locker()