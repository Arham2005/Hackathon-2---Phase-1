from typing import Callable, Dict, List, Any
import shlex

class CommandDispatcher:
    """
    Maps user commands (e.g., "add", "view", "update") to specific actions/methods.
    Parses user input, validates, and invokes the appropriate registered handler.
    """
    def __init__(self):
        self._commands: Dict[str, Callable[..., str]] = {}

    def register_command(self, command_name: str, handler_function: Callable[..., str]) -> None:
        """
        Registers a command with its corresponding handler function.
        The handler function should return a string message to be displayed to the user.
        """
        if not isinstance(command_name, str) or not command_name:
            raise ValueError("Command name must be a non-empty string.")
        if not callable(handler_function):
            raise ValueError("Handler function must be callable.")
        
        if command_name in self._commands:
            raise ValueError(f"Command '{command_name}' is already registered.")
        
        self._commands[command_name] = handler_function

    def dispatch(self, command_line_input: str) -> str:
        """
        Parses the command line input, dispatches the command to its handler,
        and returns the result or an error message.
        """
        if not command_line_input or not command_line_input.strip():
            return "Error: Command cannot be empty."

        # Use shlex to correctly parse arguments, handling quotes
        args: List[str] = shlex.split(command_line_input)
        command_name = args[0].lower()
        command_args = args[1:]

        handler = self._commands.get(command_name)
        if not handler:
            return f"Error: Unknown command '{command_name}'. Type 'help' for available commands."

        try:
            # Dynamically call the handler with its arguments
            # This assumes handlers expect arguments in the order they are provided
            # and that type hinting will guide their usage.
            return handler(*command_args)
        except TypeError as e:
            # This can happen if the number of arguments is wrong
            return f"Error: Invalid arguments for command '{command_name}'. Details: {e}"
        except ValueError as e:
            return f"Error processing command '{command_name}'. Details: {e}"
        except Exception as e:
            return f"An unexpected error occurred while executing '{command_name}'. Details: {e}"
