from typing import Optional

class InputValidator:
    """
    Provides static methods for basic input validation.
    """

    @staticmethod
    def is_not_empty(value: Optional[str], field_name: str) -> None:
        """
        Checks if a string value is not None and not empty after stripping whitespace.
        Raises ValueError if validation fails.
        """
        if value is None or not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")

