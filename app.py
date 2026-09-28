import json
import os
from datetime import datetime


TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json, return empty list if file doesn't exist or is malformed."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
            # Ensure tasks is a list
            if isinstance(tasks, list):
                return tasks
            else:
                print("Warning: tasks.json is malformed. Starting with an empty task list.")
                return []
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted. Starting with an empty task list.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []


def save_tasks(tasks):
    """Save tasks to tasks.json."""
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks: {e}")


def get_next_id(tasks):
    """Calculate the next unique task ID (max existing ID + 1)."""
    if not tasks:
        return 1
    
    max_id = max(task.get("id", 0) for task in tasks)
    return max_id + 1


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("TASK TRACKER")
    print("=" * 40)
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 40)


def add_task(tasks):
    """Add a new task to the list."""
    task_title = input("Enter task description: ").strip()
    
    if not task_title:
        print("Error: Task description cannot be empty.")
        return
    
    task = {
        "id": get_next_id(tasks),
        "title": task_title,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print(f"✓ Task added: '{task_title}'")


def list_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks yet! Add one to get started.")
        return
    
    print("\n" + "=" * 60)
    print("YOUR TASKS")
    print("=" * 60)
    
    for task in tasks:
        status = "✓" if task["completed"] else " "
        task_id = task.get("id", 0)
        title = task.get("title", "Untitled")
        print(f"  [{status}] {task_id}. {title}")
    
    print("=" * 60)


def mark_complete(tasks):
    """Mark a task as complete."""
    if not tasks:
        print("No tasks to complete.")
        return
    
    list_tasks(tasks)
    
    try:
        task_id = int(input("Enter task number to mark complete: ").strip())
        
        # Find task by ID
        task_found = False
        for task in tasks:
            if task.get("id") == task_id:
                if task["completed"]:
                    print(f"Task {task_id} is already marked complete.")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print(f"✓ Task {task_id} marked as complete!")
                task_found = True
                break
        
        if not task_found:
            print(f"Error: Task {task_id} not found.")
    
    except ValueError:
        print("Error: Please enter a valid task number.")


def delete_task(tasks):
    """Delete a task from the list."""
    if not tasks:
        print("No tasks to delete.")
        return
    
    list_tasks(tasks)
    
    try:
        task_id = int(input("Enter task number to delete: ").strip())
        
        # Find and remove task by ID
        task_found = False
        for i, task in enumerate(tasks):
            if task.get("id") == task_id:
                removed_title = task.get("title", "Untitled")
                tasks.pop(i)
                save_tasks(tasks)
                print(f"✓ Task '{removed_title}' deleted!")
                task_found = True
                break
        
        if not task_found:
            print(f"Error: Task {task_id} not found.")
    
    except ValueError:
        print("Error: Please enter a valid task number.")


def main():
    """Main application loop."""
    tasks = load_tasks()
    
    print("\n✨ Welcome to Task Tracker! ✨")
    
    while True:
        try:
            display_menu()
            choice = input("Select an option (1-5): ").strip()
            
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                list_tasks(tasks)
            elif choice == "3":
                mark_complete(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                print("\nGoodbye! 👋")
                break
            else:
                print("Error: Invalid option. Please enter a number between 1 and 5.")
        
        except EOFError:
            print("\n\nGoodbye! 👋")
            break
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break


if __name__ == "__main__":
    main()
