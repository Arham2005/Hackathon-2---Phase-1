from typing import Dict, List, Optional
from todo_app.domain.task import Task

class TaskManager:
    """
    Manages the authoritative in-memory collection of Task objects.
    It is the single source of truth for all task data.
    """
    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    def add_task(self, task: Task) -> None:
        """
        Adds a task to the manager. Raises ValueError if ID already exists.
        """
        if task.id in self._tasks:
            raise ValueError(f"Task with ID '{task.id}' already exists.")
        self._tasks[task.id] = task

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Retrieves a task by ID. Returns None if not found.
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Returns a list of all tasks.
        """
        return list(self._tasks.values())

    def update_task(self, updated_task: Task) -> None:
        """
        Updates an existing task. Raises ValueError if task does not exist.
        """
        if updated_task.id not in self._tasks:
            raise ValueError(f"Task with ID '{updated_task.id}' does not exist.")
        self._tasks[updated_task.id] = updated_task

    def delete_task(self, task_id: str) -> None:
        """
        Deletes a task by ID. Raises ValueError if task does not exist.
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID '{task_id}' does not exist.")
        del self._tasks[task_id]
