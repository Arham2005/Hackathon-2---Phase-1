# Hackathon II - Phase I: In-Memory Todo Console Application Tasks

This document lists the atomic units of work for implementing Phase I of the In-Memory Todo Console Application, derived from the `specify/plan.md` and `specify/specify.md` documents. Each task is designed to be small, single-purpose, and independently verifiable.

## 1. Project Setup and Initial Structure

-   **Task 1.1:** Create the root directory `todo_app/` and its immediate subdirectories (`domain/`, `state_management/`, `services/`, `cli/`, `utils/`).
-   **Task 1.2:** Create empty `__init__.py` files in `todo_app/`, `todo_app/domain/`, `todo_app/state_management/`, `todo_app/services/`, `todo_app/cli/`, `todo_app/utils/` to establish Python packages.
-   **Task 1.3:** Create the `main.py` entry point file.

## 2. Domain Layer

-   **Task 2.1:** Implement the `Task` entity class in `todo_app/domain/task.py` with attributes: `id` (string), `title` (string), `description` (string, optional), `is_complete` (boolean). Ensure it's a pure data structure with no business logic.

## 3. Utility Components

-   **Task 3.1:** Implement `UUIDGenerator` in `todo_app/utils/id_generator.py` for generating unique string IDs (using `uuid.uuid4()`).
-   **Task 3.2:** Implement `InputValidator` class in `todo_app/utils/input_validator.py` with static methods for basic input validation (e.g., `is_not_empty`, `is_valid_uuid`).

## 4. State Management Layer

-   **Task 4.1:** Implement `TaskManager` class in `todo_app/state_management/task_manager.py`.
    -   Initialize with an empty dictionary to store tasks (`{id: Task_object}`).
    -   Implement `add_task(task: Task)`: Adds a task. Raises error if ID already exists.
    -   Implement `get_task(task_id: str) -> Optional[Task]`: Retrieves a task by ID.
    -   Implement `get_all_tasks() -> List[Task]`: Returns a list of all tasks.
    -   Implement `update_task(updated_task: Task)`: Updates an existing task. Raises error if task does not exist.
    -   Implement `delete_task(task_id: str)`: Deletes a task by ID. Raises error if task does not exist.

## 5. Service/Business Logic Layer

-   **Task 5.1:** Implement `TaskLifecycleService` class in `todo_app/services/task_lifecycle_service.py`.
    -   Initialize with `TaskManager` and `UUIDGenerator` dependencies.
    -   Implement `create_new_task(title: str, description: Optional[str]) -> Task`: Creates and adds a new task.
    -   Implement `modify_task(task_id: str, new_title: Optional[str], new_description: Optional[str]) -> Task`: Updates task details.
    -   Implement `remove_task(task_id: str)`: Deletes a task.
    -   Implement `set_task_completion_status(task_id: str, is_complete: bool) -> Task`: Marks task as complete/incomplete.
-   **Task 5.2:** Implement `QueryEngine` class in `todo_app/services/query_engine.py`.
    -   Initialize with `TaskManager` dependency.
    -   Implement `get_all_tasks() -> List[Task]`: Retrieves all tasks from `TaskManager`.

## 6. Application/Command Layer

-   **Task 6.1:** Implement `CommandDispatcher` class in `todo_app/cli/command_dispatcher.py`.
    -   Initialize with a mapping of command names to handler functions.
    -   Implement `register_command(command_name: str, handler_function: Callable)`: Registers a command.
    -   Implement `dispatch(command_line_input: str) -> str`: Parses input, validates, and executes the registered handler. Return a string result.

## 7. Presentation Layer (CLI Interface)

-   **Task 7.1:** Implement `CLIApplication` class in `todo_app/cli/app.py`.
    -   Initialize with `CommandDispatcher`, `TaskLifecycleService`, `QueryEngine`, `InputValidator` dependencies.
    -   Implement `run()`: The main application loop.
        -   Display menu options.
        -   Read user input.
        -   Call `CommandDispatcher.dispatch()` with user input.
        -   Print output/errors.
        -   Handle graceful exit.
-   **Task 7.2:** Define CLI command handlers in `todo_app/cli/commands.py`.
    -   Implement `add_task_command(title: str, description: Optional[str]) -> str`: Uses `TaskLifecycleService` to add a task.
    -   Implement `view_tasks_command() -> str`: Uses `QueryEngine` to get and format all tasks for display.
    -   Implement `update_task_command(task_id: str, title: Optional[str], description: Optional[str]) -> str`: Uses `TaskLifecycleService` to update a task.
    -   Implement `delete_task_command(task_id: str) -> str`: Uses `TaskLifecycleService` to delete a task.
    -   Implement `mark_task_status_command(task_id: str, status: str) -> str`: Uses `TaskLifecycleService` to set task status.

## 8. Main Entry Point

-   **Task 8.1:** In `main.py`:
    -   Instantiate `UUIDGenerator`, `InputValidator`.
    -   Instantiate `TaskManager`.
    -   Instantiate `TaskLifecycleService` and `QueryEngine` with `TaskManager` and `UUIDGenerator`.
    -   Instantiate `CommandDispatcher` and register all command handlers from `todo_app/cli/commands.py`.
    -   Instantiate `CLIApplication` with all dependencies.
    -   Call `CLIApplication.run()`.

## 9. Testing (Implicit for each component)

-   **Task 9.1:** For each implemented component, create corresponding unit tests to verify its functionality and adherence to spec. (This will be a continuous effort alongside implementation tasks).
