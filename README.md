# Todo List CLI Application

A simple **command-line todo list manager** written in Python. This tool lets you add, display, remove, edit, and search todo items directly from your terminal.

## Features

- **Add Todo:** Create new todos with unique code, title, year, description, and status.
- **Display Todos:** View all or selected columns of your todo list.
- **Remove Todo:** Delete todos by code, title, time, or status.
- **Edit Todo:** Update title, time, description, or status of existing todos.
- **Search Todo:** Find todos containing a specific value in any field.
- **Interactive Menu:** User-friendly, input-validated command-line interface.

## Getting Started

### Prerequisites

- Python 3.10 or higher (uses `match` statement)
- Windows (uses `system("cls")` for clearing the screen; replace with `system("clear")` on Unix-like systems if needed)

### Run the Application


## Usage

When you start the script, you'll see:

1.[A]dd todo

2.[D]isplay todo

3.[R]emove todo

4.[E]dit todo

5.[S]earch todo

6.[Q]uit


### Actions

| Action   | Description                                    |
|----------|------------------------------------------------|
| Add      | Add a new todo with code, title, time, etc.    |
| Display  | Show all or selected columns of todos          |
| Remove   | Remove a todo by code, title, time, or status  |
| Edit     | Edit title, time, description, or status       |
| Search   | Search todos by any value                      |
| Quit     | Exit the application                           |

## Data Structure

Todos are stored as a list of lists:

todo_list = [
[code, title, time, description, status],
# Example:
[1, "task1", "2025", "", "active"],
]


## Notes

- **Input validation** prevents duplicate codes/titles and ensures valid years (2025–2039) and statuses (`active` or `deactive`).
- To adapt for non-Windows systems, replace `system("cls")` with `system("clear")` or remove it.

## License

Open for educational and personal use.
