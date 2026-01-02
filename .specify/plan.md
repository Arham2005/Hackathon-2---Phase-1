# Hackathon II - Phase I: In-Memory Todo Console Application Plan

## 1. Introduction
This document outlines the architectural plan for Phase I of the In-Memory Todo Console Application, adhering to the project's Constitution, Gemini Agent Execution Contract, and the Phase I Specification. The primary goal is to establish a robust, extensible, and testable foundation, prioritizing clear separation of concerns and single authoritative state.

## 2. High-Level Architecture

The application will follow a layered architecture to ensure strict separation of concerns:

-   **Presentation Layer (CLI Interface):** Handles user interaction, displays menus, captures input, and presents output. It will dispatch commands to the Application/Command Layer.
-   **Application/Command Layer:** Interprets user commands, orchestrates business logic, and manages the flow of data between layers. It will use a Command Dispatcher/Router.
-   **Service/Business Logic Layer:** Contains the core business rules and operations for managing tasks. This layer interacts with the Domain and State Management Layers. It will implement the Task Lifecycle Service.
-   **Domain Layer:** Defines the core `Task` entity and its attributes, without any behavior.
-   **State Management Layer:** Manages the authoritative in-memory collection of `Task` objects. This layer is the sole owner and modifier of the task state, exposed through a `TaskManager`.
-   **Utility/Shared Components:** Provides common functionalities like input validation and unique ID generation.

## 3. Component Breakdown

### 3.1. Core Components

#### 3.1.1. `Task` Entity (Domain Layer)
-   **Purpose:** Represents a single Todo item.
-   **Attributes:** `id` (unique string), `title` (string), `description` (string, optional), `is_complete` (boolean).
-   **Behavior:** Pure data structure. No business logic or state mutation methods.

#### 3.1.2. `TaskManager` (State Management Layer)
-   **Purpose:** Manages the authoritative in-memory collection of `Task` objects. It is the single source of truth for all task data.
-   **Responsibilities:**
    -   Store a collection of `Task` objects (e.g., a dictionary mapping IDs to Task objects).
    -   Provide methods for adding, retrieving (by ID or all), updating, and deleting `Task` objects.
    -   Ensure unique ID generation for new tasks.
    -   All mutations to the task state must go through `TaskManager` methods.
-   **Interfaces:** Exposes methods like `add_task(task)`, `get_task(id)`, `get_all_tasks()`, `update_task(task)`, `delete_task(id)`.

#### 3.1.3. `TaskLifecycleService` (Service/Business Logic Layer)
-   **Purpose:** Encapsulates the business rules for task operations (add, update, delete, mark complete/incomplete).
-   **Dependencies:** Relies on `TaskManager` for state manipulation.
-   **Responsibilities:**
    -   Implement logic for `add_task` (e.g., assign ID, set default status).
    -   Implement logic for `update_task` (e.g., validate fields, apply changes).
    -   Implement logic for `delete_task`.
    -   Implement logic for `mark_task_complete/incomplete`.
-   **Interfaces:** Exposes methods like `create_new_task(title, description)`, `modify_task(id, new_title, new_description)`, `remove_task(id)`, `set_task_completion_status(id, status)`.

#### 3.1.4. `QueryEngine` (Service/Business Logic Layer)
-   **Purpose:** Provides read-only access to task data, potentially with filtering or formatting.
-   **Dependencies:** Relies on `TaskManager` for raw data.
-   **Responsibilities:**
    -   Retrieve all tasks.
    -   Potentially format tasks for display (though display is Presentation Layer's job).
-   **Interfaces:** Exposes `get_all_tasks_for_display()`.

#### 3.1.5. `InputValidator` (Utility/Shared Components)
-   **Purpose:** Validates user input according to defined rules (e.g., non-empty strings, valid IDs).
-   **Responsibilities:**
    -   Provide static methods for various validation checks.

### 3.2. Orchestration Components

#### 3.2.1. `CommandDispatcher` / `Router` (Application/Command Layer)
-   **Purpose:** Maps user commands (e.g., "add", "view", "update") to specific actions/methods in the Service Layer.
-   **Responsibilities:**
    -   Register command handlers.
    -   Parse user input to identify the command and its arguments.
    -   Invoke the appropriate handler with validated arguments.
-   **Interfaces:** `register_command(command_name, handler_function)`, `dispatch(user_input)`.

#### 3.2.2. `CLIApplication` (Presentation Layer)
-   **Purpose:** The main entry point for the console application.
-   **Dependencies:** `CommandDispatcher`, `InputValidator`, `QueryEngine`.
-   **Responsibilities:**
    -   Display the main menu.
    -   Read user input.
    -   Delegate input parsing and command execution to `CommandDispatcher`.
    -   Display results and error messages.
    -   Manage the application loop.

## 4. Interaction Flow Example (Add Task)

1.  `CLIApplication` displays menu, prompts for input.
2.  User enters "add <title> <description>".
3.  `CLIApplication` passes input to `CommandDispatcher`.
4.  `CommandDispatcher` identifies "add" command and extracts arguments.
5.  `InputValidator` validates title and description.
6.  `CommandDispatcher` invokes `TaskLifecycleService.create_new_task(title, description)`.
7.  `TaskLifecycleService` generates a unique ID, creates a `Task` object, and calls `TaskManager.add_task(task)`.
8.  `TaskManager` stores the new `Task`.
9.  `TaskLifecycleService` returns success/failure.
10. `CommandDispatcher` relays result to `CLIApplication`.
11. `CLIApplication` displays success message.

## 5. Architectural Considerations

### 5.1. Uniqueness and ID Generation
-   Unique IDs will be generated within the `TaskManager` or `TaskLifecycleService` (to be decided, leaning towards `TaskLifecycleService` to keep `TaskManager` focused purely on storage and retrieval) to ensure each task has a distinct identifier. Python's `uuid` module is suitable.

### 5.2. Error Handling
-   Explicit error handling will be implemented at each layer, with meaningful exceptions propagated up to the `CLIApplication` for user-friendly display.

### 5.3. Testability
-   Each component will be designed to be independently testable, leveraging dependency injection where appropriate.

### 5.4. Extensibility
-   The layered architecture and explicit interfaces will allow for easy extension in future phases (e.g., replacing `TaskManager` with a persistent storage solution, adding new commands, or introducing new task attributes) without requiring significant refactoring of core logic.

## 6. Directory Structure (Proposed)

```
.
├───main.py                 # Application entry point
├───todo_app/
│   ├───__init__.py
│   ├───domain/
│   │   └───task.py         # Task entity definition
│   ├───state_management/
│   │   └───task_manager.py # TaskManager implementation
│   ├───services/
│   │   ├───task_lifecycle_service.py # Business logic for tasks
│   │   └───query_engine.py         # Read-only task queries
│   ├───cli/
│   │   ├───__init__.py
│   │   ├───commands.py           # Command definitions
│   │   ├───command_dispatcher.py # CommandDispatcher implementation
│   │   └───app.py                # CLIApplication main loop and UI
│   └───utils/
│       └───input_validator.py    # Input validation utilities
│       └───id_generator.py       # Unique ID generation (if separate)
```
