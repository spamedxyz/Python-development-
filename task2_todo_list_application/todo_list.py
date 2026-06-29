"""Task 2: To-Do List Application.

Allows users to add tasks, view tasks, mark tasks as complete, remove tasks,
and view progress with a text progress bar.
"""

from __future__ import annotations


def build_progress_bar(completed: int, total: int, width: int = 20) -> str:
    """Return a simple text progress bar."""
    if total == 0:
        return "[" + "-" * width + "] 0%"

    percent = completed / total
    filled = round(width * percent)
    bar = "#" * filled + "-" * (width - filled)
    return f"[{bar}] {percent:.0%}"


def show_tasks(tasks: list[dict[str, object]]) -> None:
    """Display all tasks and completion progress."""
    if not tasks:
        print("\nNo tasks available.")
        return

    completed = sum(1 for task in tasks if task["done"])
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['title']} - {status}")

    print(f"\nProgress: {build_progress_bar(completed, len(tasks))}")
    print(f"Completed {completed} of {len(tasks)} tasks.")


def read_task_number(tasks: list[dict[str, object]], prompt: str) -> int | None:
    """Read and validate a task number from the user."""
    if not tasks:
        print("\nNo tasks available.")
        return None

    show_tasks(tasks)
    try:
        task_number = int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None

    if 1 <= task_number <= len(tasks):
        return task_number - 1

    print("Invalid task number.")
    return None


def main() -> None:
    """Run the interactive to-do list application."""
    tasks: list[dict[str, object]] = []

    while True:
        print("\n====== To-Do List Application ======")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                print("Task added successfully.")
            else:
                print("Task title cannot be empty.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            index = read_task_number(tasks, "Enter task number to mark as done: ")
            if index is not None:
                tasks[index]["done"] = True
                print("Task marked as done.")

        elif choice == "4":
            index = read_task_number(tasks, "Enter task number to remove: ")
            if index is not None:
                removed = tasks.pop(index)
                print(f"Removed task: {removed['title']}")

        elif choice == "5":
            print("\nThank you for using the To-Do List Application.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
