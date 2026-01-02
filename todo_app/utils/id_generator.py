class SequentialIDGenerator:
    """
    Generates unique sequential integer IDs. IDs reset on application start.
    """
    def __init__(self):
        self._current_id = 0

    def generate_id(self) -> str:
        """
        Generates a new sequential integer ID as a string.
        """
        self._current_id += 1
        return str(self._current_id)
