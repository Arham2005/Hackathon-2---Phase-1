from dataclasses import dataclass, field
from typing import Optional

@dataclass(frozen=True)
class Task:
    """
    Represents a single Todo item.
    This is a pure data structure with no business logic.
    """
    id: str
    title: str
    description: Optional[str] = None
    is_complete: bool = False
