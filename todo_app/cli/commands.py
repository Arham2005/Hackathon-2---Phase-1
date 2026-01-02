from typing import Optional, Callable, List
from todo_app.services.task_lifecycle_service import TaskLifecycleService
from todo_app.services.query_engine import QueryEngine
from todo_app.domain.task import Task
from datetime import datetime

# These service instances will be injected at runtime
_task_lifecycle_service: Optional[TaskLifecycleService] = None
_query_engine: Optional[QueryEngine] = None

def init_command_handlers(lifecycle_service: TaskLifecycleService, query_engine: QueryEngine):
    """
    Initializes the command handlers with the necessary service instances.
    This function should be called once during application startup.
    """
    global _task_lifecycle_service, _query_engine
    _task_lifecycle_service = lifecycle_service
    _query_engine = query_engine

def _check_services_initialized():
    if _task_lifecycle_service is None or _query_engine is None:
        raise RuntimeError("Command handlers not initialized. Call init_command_handlers first.")

def _format_task_output(task: Task) -> str:
    """Helper function to format a single task for display."""
    status = "✅ Complete" if task.is_complete else "⏳ Incomplete"
    description_line = f"  Description: {task.description}" if task.description else ""
    return (
        f"ID: {task.id}\n"
        f"  Title: {task.title}\n"
        f"{description_line}\n"
        f"  Status: {status}\n"
        "--------------------"
    )

def _format_tasks_list_output(tasks: List[Task]) -> str:
    """Helper function to format a list of tasks for display."""
    if not tasks:
        return "No tasks found."
    
    formatted_tasks = [_format_task_output(task) for task in tasks]
    return "\n".join(formatted_tasks)


def add_task_command(title: str, description: Optional[str] = None) -> str:
    """
    Adds a new task.
    Usage: add <title> [description]
    """
    _check_services_initialized()
    try:
        task = _task_lifecycle_service.create_new_task(title=title, description=description)
        return f"Task '{task.title}' added successfully with ID: {task.id}"
    except ValueError as e:
        return f"Failed to add task: {e}"

def view_tasks_command() -> str:
    """
    Views all tasks.
    Usage: view
    """
    _check_services_initialized()
    tasks = _query_engine.get_all_tasks()
    return _format_tasks_list_output(tasks)

def update_task_command(task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> str:
    """
    Updates an existing task's title or description.
    Usage: update <task_id> [title] [description]
    Note: Both title and description are optional, but at least one must be provided.
    """
    _check_services_initialized()
    if title is None and description is None:
        return "Error: At least one of 'title' or 'description' must be provided to update a task."
    try:
        updated_task = _task_lifecycle_service.modify_task(
            task_id=task_id, 
            new_title=title, 
            new_description=description
        )
        return f"Task '{updated_task.id}' updated successfully."
    except ValueError as e:
        return f"Failed to update task: {e}"

def delete_task_command(task_id: str) -> str:
    """
    Deletes a task by ID.
    Usage: delete <task_id>
    """
    _check_services_initialized()
    try:
        _task_lifecycle_service.remove_task(task_id=task_id)
        return f"Task '{task_id}' deleted successfully."
    except ValueError as e:
        return f"Failed to delete task: {e}"

def mark_task_status_command(task_id: str, status: str) -> str:
    """
    Marks a task as complete or incomplete.
    Usage: mark <task_id> <complete|incomplete>
    """
    _check_services_initialized()
    is_complete: Optional[bool] = None
    if status.lower() == "complete":
        is_complete = True
    elif status.lower() == "incomplete":
        is_complete = False
    else:
        return "Error: Status must be 'complete' or 'incomplete'."
    
    try:
        updated_task = _task_lifecycle_service.set_task_completion_status(task_id=task_id, is_complete=is_complete)
        status_text = "completed" if updated_task.is_complete else "incomplete"
        return f"Task '{updated_task.id}' marked as {status_text}."
    except ValueError as e:
        return f"Failed to mark task status: {e}"

def help_command() -> str:
    """
    Displays available commands and their usage.
    Usage: help
    """
    help_text = "Available commands:\n"
    help_text += "  add <title> [description] - Adds a new task.\n"
    help_text += "  view - Views all tasks.\n"
    help_text += "  update <task_id> [title] [description] - Updates an existing task's title or description.\n"
    help_text += "  delete <task_id> - Deletes a task by ID.\n"
    help_text += "  mark <task_id> <complete|incomplete> - Marks a task as complete or incomplete.\n"
    help_text += "  help - Displays this help message.\n"
    help_text += "  exit - Exits the application.\n"
    return help_text
