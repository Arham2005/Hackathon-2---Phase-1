from typing import List
from todo_app.domain.task import Task
from todo_app.state_management.task_manager import TaskManager

class QueryEngine:
    """
    Provides read-only access to task data.
    """
    def __init__(self, task_manager: TaskManager):
        self._task_manager = task_manager

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieves all tasks from the TaskManager.
        """
        return self._task_manager.get_all_tasks()
