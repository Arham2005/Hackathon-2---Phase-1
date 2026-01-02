from todo_app.cli.app import CLIApplication
from todo_app.services.query_engine import QueryEngine
from todo_app.services.task_lifecycle_service import TaskLifecycleService
from todo_app.state_management.task_manager import TaskManager
from todo_app.utils.id_generator import SequentialIDGenerator

def main():
    # Instantiate core components
    task_manager = TaskManager()
    id_generator = SequentialIDGenerator()

    # Instantiate services
    task_lifecycle_service = TaskLifecycleService(task_manager, id_generator)
    query_engine = QueryEngine(task_manager)

    # Instantiate and run the CLI application
    app = CLIApplication(task_lifecycle_service, query_engine)
    app.run()

if __name__ == "__main__":
    main()