# Task Tracker

A beginner-friendly console task tracker built with Python using only the standard library. Manage your daily tasks with a simple numbered menu interface, persistent JSON storage, and robust error handling.

## Features

- **Numbered Menu Interface**: Easy-to-navigate console menu with 5 options
- **Add Tasks**: Create new tasks with descriptions
- **List Tasks**: View all tasks with completion status
- **Mark Complete**: Mark an incomplete task as complete; this action does not toggle it back to incomplete
- **Delete Tasks**: Remove completed or unwanted tasks
- **Persistent Storage**: All tasks saved to `tasks.json` and restored on startup
- **Error Handling**: Gracefully handles invalid input, malformed JSON, and EOF/interrupt signals at the main menu prompt
- **No Dependencies**: Uses only Python standard library (`json`, `os`, `datetime`)

## Requirements

- Python 3.6 or higher

## Installation

No installation required! Simply clone the repository:

```bash
git clone https://github.com/Bigdbetd/task-tracker-copilot-assignment.git
cd task-tracker-copilot-assignment
```

## Usage

### Running the Application

**Windows:**
```cmd
python app.py
```

**macOS/Linux:**
```bash
python3 app.py
```

### Menu Options

When you run the app, you'll see:
```
========================================
TASK TRACKER
========================================
1. Add Task
2. List Tasks
3. Mark Task Complete
4. Delete Task
5. Exit
========================================
```

### Example Workflow

**Adding Tasks:**
```
Select an option (1-5): 1
Enter task description: Buy groceries
✓ Task added: 'Buy groceries'

Select an option (1-5): 1
Enter task description: Finish project report
✓ Task added: 'Finish project report'

Select an option (1-5): 1
Enter task description: Call mom
✓ Task added: 'Call mom'
```

**Listing Tasks:**
```
Select an option (1-5): 2

============================================================
YOUR TASKS
============================================================
  [ ] 1. Buy groceries
  [ ] 2. Finish project report
  [ ] 3. Call mom
============================================================
```

**Marking a Task Complete:**
```
Select an option (1-5): 3

============================================================
YOUR TASKS
============================================================
  [ ] 1. Buy groceries
  [ ] 2. Finish project report
  [ ] 3. Call mom
============================================================
Enter task number to mark complete: 1
✓ Task 1 marked as complete!

Select an option (1-5): 2

============================================================
YOUR TASKS
============================================================
  [✓] 1. Buy groceries
  [ ] 2. Finish project report
  [ ] 3. Call mom
============================================================
```

Marking a task complete only changes it from incomplete to complete. Running the action again reports that the task is already complete; it does not change the task back to incomplete.

**Deleting a Task:**
```
Select an option (1-5): 4

============================================================
YOUR TASKS
============================================================
  [✓] 1. Buy groceries
  [ ] 2. Finish project report
  [ ] 3. Call mom
============================================================
Enter task number to delete: 1
✓ Task 'Buy groceries' deleted!

Select an option (1-5): 2

============================================================
YOUR TASKS
============================================================
  [ ] 2. Finish project report
  [ ] 3. Call mom
============================================================
```

**Exiting the Application:**
```
Select an option (1-5): 5

Goodbye! 👋
```

## Data Persistence

All tasks are automatically saved to `tasks.json` after each operation (add, complete, delete). Because the application uses the relative path `tasks.json`, the file is created in the process's current working directory—the directory from which `python app.py` is run—not necessarily the directory containing `app.py`.

**Example `tasks.json` structure:**
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "completed": false,
    "created_at": "2026-09-28T10:30:45.123456"
  },
  {
    "id": 2,
    "title": "Finish project report",
    "completed": true,
    "created_at": "2026-09-28T10:31:12.456789"
  }
]
```

**Recovery from Corruption:**
- If `tasks.json` is missing or malformed, the app will display a warning and start with an empty task list
- The file will be recreated when you add a new task
- No data is lost permanently if you back up your `tasks.json` file

## Input Handling

The app handles invalid input gracefully:

- **Invalid menu choice** (e.g., `6`, `abc`): Shows an error message and returns to the menu
- **Empty task description**: Rejected with an error prompt to enter a valid description
- **Non-numeric task ID** (e.g., `foo`): Shows a validation error and returns to the menu
- **Nonexistent task ID** (e.g., task 99 doesn't exist): Displays a "not found" error
- **Malformed JSON**: App warns you and starts with a fresh task list
- **Ctrl+C** or **Ctrl+D** (EOF): When entered at the main menu prompt, the app exits gracefully with a goodbye message. These signals are not caught around the add, complete, or delete input prompts.

## Project Structure

```
task-tracker-copilot-assignment/
├── app.py           # Main application
├── tasks.json       # Persistent task storage, created in the current working directory
├── README.md        # This file
├── REFLECTION.md    # Project reflection
└── evidence/        # Supporting project evidence
```

`REFLECTION.md` and `evidence/` are included in the intended project structure for the project materials you add.

## License

This project is provided as-is for educational purposes.
