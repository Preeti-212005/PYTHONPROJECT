import csv
import os


TASKS_FILE = "tasks.csv"


def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:  # Ensure row has two fields: title and completed status
                    title, completed = row
                    tasks.append({"title": title, "completed": completed.lower() == 'true'})
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task["title"], task["completed"]])


def display_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nCurrent Task List:")
        for i, task in enumerate(tasks):
            status = "Complete" if task["completed"] else "Incomplete"
            print(f"{i+1}. {task['title']} [{status}]")


def add_task(tasks):
    title = input("Enter the task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")
    save_tasks(tasks)


def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_num < len(tasks):
            new_title = input(f"Enter new title for task '{tasks[task_num]['title']}': ")
            tasks[task_num]["title"] = new_title
            print("Task updated successfully!")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted_task = tasks.pop(task_num)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def mark_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete/incomplete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = not tasks[task_num]["completed"]
            status = "Complete" if tasks[task_num]["completed"] else "Incomplete"
            print(f"Task marked as {status}.")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main_menu():
    tasks = load_tasks()
    
    while True:
        print("\n--- Task Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete/Incomplete")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task(tasks)
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
