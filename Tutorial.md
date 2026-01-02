# To-Do Application CLI Tutorial (Updated Version)

Welcome to the updated tutorial for the In-Memory To-Do Application! This guide will explain how to interact with the application through its new menu-driven command-line interface (CLI) and use its various features.

---

## How to Interact:
Once the application is running (by executing `python main.py` in your terminal), you will be greeted with a welcome message, followed by the main menu. Instead of typing commands directly, you will choose options by entering the corresponding number from the menu. The application will then guide you through any necessary inputs for the selected action.

The menu will remain visible after each operation, allowing you to perform multiple actions until you choose to exit.

---

## Available Actions (Menu Options):

Here's a detailed breakdown of each menu option:

### 1. `Add Task`
*   **Purpose:** Creates a new to-do task.
*   **Interaction:**
    1.  Select option `1` from the main menu.
    2.  The application will prompt you to "Enter task title: ". Type your task's title and press Enter.
    3.  Next, it will prompt you to "Enter task description (optional): ". Type your description (or leave it empty) and press Enter.
*   **Example Session:**
    ```
    --- To-Do Application Menu ---
    1. Add Task
    2. View All Tasks
    3. Update Task
    4. Delete Task
    5. Mark Task Status
    6. Show Menu
    7. Exit
    ----------------------------
    Enter your choice: 1

    --- Add New Task ---
    Enter task title: Buy groceries
    Enter task description (optional): Milk, eggs, and bread
    Task 'Buy groceries' added successfully with ID: 1
    ```
*   **Expected Output:** A success message confirming the task addition and its unique ID (e.g., `Task 'Buy groceries' added successfully with ID: 1`).
*   **Error Handling:** If the title is empty, it will return an error message.

### 2. `View All Tasks`
*   **Purpose:** Displays a list of all current to-do tasks, including their ID, title, description, and completion status.
*   **Interaction:**
    1.  Select option `2` from the main menu.
*   **Example Session:**
    ```
    --- To-Do Application Menu ---
    1. Add Task
    2. View All Tasks
    3. Update Task
    4. Delete Task
    5. Mark Task Status
    6. Show Menu
    7. Exit
    ----------------------------
    Enter your choice: 2

    --- All Tasks ---
    ID: 1
      Title: Buy groceries
      Description: Milk, eggs, and bread
      Status: ⏳ Incomplete
    --------------------
    ID: 2
      Title: Walk the dog
      Description: Take Fido to the park
      Status: ⏳ Incomplete
    --------------------
    ```
*   **Expected Output:** A formatted list of tasks. If no tasks exist, it will state "No tasks found."

### 3. `Update Task`
*   **Purpose:** Modifies the title or description (or both) of an existing task, identified by its unique ID.
*   **Interaction:**
    1.  Select option `3` from the main menu.
    2.  The application will prompt for the "ID of the task to update: ".
    3.  Then, it will ask for a "new title (leave empty to keep current): ".
    4.  Finally, it will ask for a "new description (leave empty to keep current): ".
*   **Important:** You must provide at least one of `new title` or `new description` to perform an update.
*   **Example Session:**
    ```
    --- To-Do Application Menu ---
    ... (menu displayed) ...
    Enter your choice: 3

    --- Update Task ---
    Enter the ID of the task to update: 1
    Enter new title (leave empty to keep current): Buy healthy groceries
    Enter new description (leave empty to keep current): 
    Task '1' updated successfully.
    ```
*   **Expected Output:** A success message confirming the update (e.g., `Task '1' updated successfully.`).
*   **Error Handling:** Returns an error if the task ID is not found or no changes are provided.

### 4. `Delete Task`
*   **Purpose:** Removes a task from the list permanently.
*   **Interaction:**
    1.  Select option `4` from the main menu.
    2.  The application will prompt for the "ID of the task to delete: ".
*   **Example Session:**
    ```
    --- To-Do Application Menu ---
    ... (menu displayed) ...
    Enter your choice: 4

    --- Delete Task ---
    Enter the ID of the task to delete: 2
    Task '2' deleted successfully.
    ```
*   **Expected Output:** A success message confirming the deletion (e.g., `Task '2' deleted successfully.`).
*   **Error Handling:** Returns an error if the task ID is not found.

### 5. `Mark Task Status`
*   **Purpose:** Changes a task's completion status to either complete or incomplete.
*   **Interaction:**
    1.  Select option `5` from the main menu.
    2.  The application will prompt for the "ID of the task to mark: ".
    3.  Then, it will ask "Mark as (complete/incomplete): ".
*   **Example Session:**
    ```
    --- To-Do Application Menu ---
    ... (menu displayed) ...
    Enter your choice: 5

    --- Mark Task Status ---
    Enter the ID of the task to mark: 1
    Mark as (complete/incomplete): complete
    Task '1' marked as completed.
    ```
*   **Expected Output:** A success message confirming the status change (e.g., `Task '1' marked as completed.`).
*   **Error Handling:** Returns an error if the task ID is not found or an invalid status is provided.

### 6. `Show Menu`
*   **Purpose:** Redisplays the main menu options.
*   **Interaction:**
    1.  Select option `6` from the main menu.
*   **Example Session:**
    ```
    --- To-Do Application Menu ---
    ... (menu displayed) ...
    Enter your choice: 6

    --- Showing Menu ---
    --- To-Do Application Menu ---
    1. Add Task
    2. View All Tasks
    3. Update Task
    4. Delete Task
    5. Mark Task Status
    6. Show Menu
    7. Exit
    ----------------------------
    ```

### 7. `Exit`
*   **Purpose:** Terminates the application. Remember that this is an in-memory application, so all data will be lost upon exit.
*   **Interaction:**
    1.  Select option `7` from the main menu.
*   **Example Session:**
    ```
    --- To-Do Application Menu ---
    ... (menu displayed) ...
    Enter your choice: 7
    Exiting To-Do Application. Goodbye!
    ```
*   **Expected Output:** A goodbye message and the application closing.
---

This concludes the updated tutorial on how to use the In-Memory To-Do Application with its new menu-driven interface.
