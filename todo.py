tasks = []
next_id = 1

def add_task():
    global next_id
    description = input("Enter task description: ")
    tasks.append({'id': next_id, 'description': description, 'status': 'pending'})
    print(f"Task '{description}' added with ID {next_id}.")
    next_id += 1

def view_tasks():
    if tasks:
        print("\n----To-Do List---")
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, status: {task['status']}")
    else:
        print("No tasks available.")

def remove_task(search_term):
    if search_term.isdigit():
        id_to_remove = int(search_term)
        task = next((task for task in tasks if task['id'] == id_to_remove), None)
    else:
        task = next((task for task in tasks if search_term.lower() in task['description'].lower()), None)

    if task:
        tasks.remove(task)
        print(f"Task '{task['description']}' removed.")
    else:
        print("Task not found.")

def mark_task_completed():
    search_term = input("Enter task ID or part of the description: ")
    if search_term.isdigit():
        id_to_complete = int(search_term)
        task = next((task for task in tasks if task['id'] == id_to_complete), None)
    else:
        task = next((task for task in tasks if search_term.lower() in task['description'].lower()), None)

    if task:
        task['status'] = 'completed'
        print(f"Task '{task['description']}' marked as completed.")
    else:
        print("Task not found.")

def edit_task():
    search_term = input("Enter task ID or part of the description: ")
    if search_term.isdigit():
        id_to_edit = int(search_term)
        task = next((task for task in tasks if task['id'] == id_to_edit), None)
    else:
        task = next((task for task in tasks if search_term.lower() in task['description'].lower()), None)

    if task:
        new_description = input(f"Enter new description for task '{task['description']}': ")
        task['description'] = new_description
        print(f"Task ID {task['id']} updated.")
    else:
        print("Task not found.")

def search_task():
    print("\n---- Search Results---")
    search_term = input("Enter keyword to search for tasks: ")
    found_task = [task for task in tasks if search_term.lower() in task['description'].lower()]
    if found_task:
        print("\n---Search Results---")
        for task in found_task:
            print(f"ID: {task['id']}, Description: {task['description']}, status: {task['status']}")
    else:
        print("No tasks found matching the search term.")

def filter_task():
    status = input("Filter tasks by status (pending/completed): ")
    filtered_tasks = [task for task in tasks if task['status'] == status]
    if filtered_tasks:
        print(f"Tasks with status '{status}':")
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, status: {task['status']}")
    else:
        print(f"No tasks found with status '{status}'.")

def clear_all_tasks():
    confirmation = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
    if confirmation == 'yes':
        tasks.clear()
        print("All tasks cleared.")
    else:
        print("Action cancelled.")

def sort_tasks():
    sort_by = input("Sort tasks by (id/status): ").lower()
    if sort_by == 'id':
        tasks.sort(key=lambda task: task['id'])
        print("Tasks sorted by ID.")
    elif sort_by == 'status':
        tasks.sort(key=lambda task: task['status'])
        print("Tasks sorted by status.")
    else:
        print("Invalid option.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            search_term = input("Enter task ID or part of the description to remove: ")
            remove_task(search_term)
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            edit_task()
        elif choice == "6":
            search_task()
        elif choice == "7":
            filter_task()
        elif choice == "8":
            clear_all_tasks()
        elif choice == "9":
            sort_tasks()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
