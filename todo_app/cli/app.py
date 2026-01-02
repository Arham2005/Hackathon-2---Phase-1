from typing import Optional, Callable, List
from todo_app.services.task_lifecycle_service import TaskLifecycleService
from todo_app.services.query_engine import QueryEngine
from todo_app.domain.task import Task

class CLIApplication:
    """
    The main entry point for the console application.
    Handles the application loop, user input, and output display.
    """
    def __init__(self, task_lifecycle_service: TaskLifecycleService,
                 query_engine: QueryEngine):
        self._task_lifecycle_service = task_lifecycle_service
        self._query_engine = query_engine
        self._running = False
        self._menu_options = {
            "1": {"name": "Add Task", "command": self._interactive_add_task},
            "2": {"name": "View All Tasks", "command": self._interactive_view_tasks},
            "3": {"name": "Update Task", "command": self._interactive_update_task},
            "4": {"name": "Delete Task", "command": self._interactive_delete_task},
            "5": {"name": "Mark Task Status", "command": self._interactive_mark_task_status},
            "6": {"name": "Show Menu", "command": self._interactive_help},
            "7": {"name": "Exit", "command": self._exit_application}
        }
    
    def _format_task_output(self, task: Task) -> str:
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

    def _format_tasks_list_output(self, tasks: List[Task]) -> str:
        """Helper function to format a list of tasks for display."""
        if not tasks:
            return "No tasks found."
        
        formatted_tasks = [self._format_task_output(task) for task in tasks]
        return "\n".join(formatted_tasks)

    def _display_menu(self) -> None:
        """Displays the main menu options to the user."""
        print("\n--- To-Do Application Menu ---")
        for key, value in self._menu_options.items():
            print(f"{key}. {value['name']}")
        print("----------------------------")

    def _get_user_choice(self) -> Optional[Callable]:
        """Prompts the user for a choice and returns the corresponding command handler."""
        while True:
            try:
                choice = input("Enter your choice: ").strip()
                if choice in self._menu_options:
                    return self._menu_options[choice]["command"]
                else:
                    print("Invalid choice. Please enter a number from the menu.")
            except EOFError:
                return self._exit_application
            except Exception as e:
                print(f"An error occurred while getting input: {e}")
                return None

    def _interactive_add_task(self) -> None:
        """Guides the user through adding a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional): ").strip()
        if not description:
            description = None # Pass None if description is empty
        
        try:
            task = self._task_lifecycle_service.create_new_task(title=title, description=description)
            print(f"Task '{task.title}' added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Failed to add task: {e}")

    def _interactive_view_tasks(self) -> None:
        """Displays all tasks."""
        print("\n--- All Tasks ---")
        tasks = self._query_engine.get_all_tasks()
        print(self._format_tasks_list_output(tasks))

    def _interactive_update_task(self) -> None:
        """Guides the user through updating a task."""
        print("\n--- Update Task ---")
        task_id = input("Enter the ID of the task to update: ").strip()
        title = input("Enter new title (leave empty to keep current): ").strip()
        description = input("Enter new description (leave empty to keep current): ").strip()

        if not title:
            title = None
        if not description:
            description = None
        
        if title is None and description is None:
            print("No changes provided. Task not updated.")
            return

        try:
            updated_task = self._task_lifecycle_service.modify_task(
                task_id=task_id, 
                new_title=title, 
                new_description=description
            )
            print(f"Task '{updated_task.id}' updated successfully.")
        except ValueError as e:
            print(f"Failed to update task: {e}")

    def _interactive_delete_task(self) -> None:
        """Guides the user through deleting a task."""
        print("\n--- Delete Task ---")
        task_id = input("Enter the ID of the task to delete: ").strip()
        try:
            self._task_lifecycle_service.remove_task(task_id=task_id)
            print(f"Task '{task_id}' deleted successfully.")
        except ValueError as e:
            print(f"Failed to delete task: {e}")

    def _interactive_mark_task_status(self) -> None:
        """Guides the user through marking a task's status."""
        print("\n--- Mark Task Status ---")
        task_id = input("Enter the ID of the task to mark: ").strip()
        status_choice = input("Mark as (complete/incomplete): ").strip().lower()

        is_complete: Optional[bool] = None
        if status_choice == "complete":
            is_complete = True
        elif status_choice == "incomplete":
            is_complete = False
        else:
            print("Error: Status must be 'complete' or 'incomplete'.")
            return
        
        try:
            updated_task = self._task_lifecycle_service.set_task_completion_status(task_id=task_id, is_complete=is_complete)
            status_text = "completed" if updated_task.is_complete else "incomplete"
            print(f"Task '{updated_task.id}' marked as {status_text}.")
        except ValueError as e:
            print(f"Failed to mark task status: {e}")

    def _interactive_help(self) -> None:
        """Displays the menu (which serves as help)."""
        print("\n--- Showing Menu ---")
        self._display_menu()

    def _exit_application(self) -> None:
        """Sets the flag to exit the application loop."""
        self._running = False
        print("Exiting To-Do Application. Goodbye!")

    def run(self) -> None:
        """
        Runs the main application loop with a menu-driven interface.
        """
        self._running = True
        print("Welcome to the To-Do Application!")
        print("Please choose an option from the menu.")

        while self._running:
            self._display_menu()
            chosen_command_handler = self._get_user_choice()
            if chosen_command_handler:
                try:
                    # Execute the chosen interactive command method
                    chosen_command_handler()
                except Exception as e:
                    print(f"An unexpected application error occurred: {e}")