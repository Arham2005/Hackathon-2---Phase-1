from typing import Optional
from todo_app.domain.task import Task
from todo_app.state_management.task_manager import TaskManager
from todo_app.utils.id_generator import SequentialIDGenerator
from todo_app.utils.input_validator import InputValidator

class TaskLifecycleService:
    """
    Encapsulates the business rules for task operations (add, update, delete, mark complete/incomplete).
    """
    def __init__(self, task_manager: TaskManager, id_generator: SequentialIDGenerator):
        self._task_manager = task_manager
        self._id_generator = id_generator

    def create_new_task(self, title: str, description: Optional[str]) -> Task:
        """
        Creates and adds a new task.
        """
        InputValidator.is_not_empty(title, "Task title")
        task_id = self._id_generator.generate_id()
        new_task = Task(id=task_id, title=title, description=description, is_complete=False)
        self._task_manager.add_task(new_task)
        return new_task

    def modify_task(self, task_id: str, new_title: Optional[str], new_description: Optional[str]) -> Task:
        """
        Updates task details.
        """
        existing_task = self._task_manager.get_task(task_id)
        if not existing_task:
            raise ValueError(f"Task with ID '{task_id}' not found.")

        updated_title = new_title if new_title is not None else existing_task.title
        updated_description = new_description if new_description is not None else existing_task.description
        
        # Ensure at least one field is being updated
        if updated_title == existing_task.title and updated_description == existing_task.description:
            raise ValueError("No changes detected. Title and description are the same as current values.")

        updated_task = Task(
            id=existing_task.id,
            title=updated_title,
            description=updated_description,
            is_complete=existing_task.is_complete
        )
        self._task_manager.update_task(updated_task)
        return updated_task

    def remove_task(self, task_id: str) -> None:
        """
        Deletes a task.
        """
        self._task_manager.delete_task(task_id)

    def set_task_completion_status(self, task_id: str, is_complete: bool) -> Task:
        """
        Marks task as complete/incomplete.
        """
        existing_task = self._task_manager.get_task(task_id)
        if not existing_task:
            raise ValueError(f"Task with ID '{task_id}' not found.")
        
        if existing_task.is_complete == is_complete:
            status_str = "completed" if is_complete else "incomplete"
            raise ValueError(f"Task with ID '{task_id}' is already {status_str}.")

        updated_task = Task(
            id=existing_task.id,
            title=existing_task.title,
            description=existing_task.description,
            is_complete=is_complete
        )
        self._task_manager.update_task(updated_task)
        return updated_task
