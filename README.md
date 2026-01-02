 Project Overview: In-Memory To-Do Console Application (Phase I)

  This project, developed as Phase I of Hackathon II, implements an In-Memory To-Do Console Application. Its primary
  purpose is to provide a foundational, robust, and extensible system for managing simple to-do tasks directly through a
  command-line interface (CLI).

  Key Aspects:

   * Core Functionality: Users can perform essential task management operations, including adding new tasks, viewing all
     existing tasks, updating task titles and descriptions, deleting tasks by their unique ID, and marking tasks as
     complete or incomplete.
   * Task Entity: Each task is defined minimally, comprising only a unique sequential integer identifier, a title, an
     optional description, and a completion status.
   * In-Memory Design: Adhering to Phase I constraints, all task data is stored purely in memory and is not persisted
     across application runs. The application is built exclusively using the Python standard library, ensuring no
     external dependencies.
   * Architectural Foundation: The application is built upon a layered architecture emphasizing strict separation of
     concerns. It features distinct layers for Presentation (CLI interaction), Application Logic, Business Services,
     Domain Modeling, and State Management. Key reusable components like a TaskManager, TaskLifecycleService,
     QueryEngine, and SequentialIDGenerator ensure a clean, testable, and highly extensible codebase designed for future
     phases.
   * User Experience (UX): The CLI provides a user-friendly, menu-driven interface, guiding users through operations
     with clear prompts and validated inputs, enhancing usability over raw command-line input.

  This Phase I implementation serves as a strategic blueprint, prioritizing architectural integrity and extensibility to
  support the addition of more complex features and persistence mechanisms in subsequent hackathon phases, without
  requiring a rewrite of its core logic.
