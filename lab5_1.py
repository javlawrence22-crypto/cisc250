# Name: Javrick Lawrence
# LAB 5-1
# Date: 2026-5-28
# ============================================================

from lab5_3 import store_task_list, load_task_list

#task 1.1
todo_list = load_task_list()  
 
#task1.2
def add_task(task):
    '''Adds a task to the to-do list.'''
    todo_list.append(task)
    print(f"'{task}' has been added to the to-do list.")

#task 1.3
def show_tasks():
    '''displays all tasks in the to-do list.'''
    index = 1
    for task in todo_list:
        print(f"{index}. {task}")
        index += 1  
    if not todo_list:
        print("The to do list is empty.")

    #task 1.4
def remove_task(task_num):
    """Removes a task using its displayed task number."""
    try:
        task_num = int(task_num)

        if task_num < 1 or task_num > len(todo_list):
            print("Invalid task number.")
        else:
            removed_task = todo_list.pop(task_num - 1)
            print(f"'{removed_task}' has been removed.")

    except ValueError:
        print("Please enter a valid number.")


# Task 2.1
def run_todo_app():
    """Runs the To-Do List application."""

# Task 2.2
    print(" Welcome to the To-Do List App ")

    # Task 2.3
    while True:

     # Task 2.4
        print("\nMenu")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("What would you like to do? Please select a number > ")

         # Task 2.5
        if choice == "1":
            show_tasks()

        elif choice == "2":
            task = input("Enter a task description: ").strip()

            # Task 2.5.1
            if task == "":
                print("Task description cannot be blank.")
            else:
                add_task(task)

        elif choice == "3":

            # Task 2.5.2
            if not todo_list:
                print("No tasks available to remove.")
            else:
                show_tasks()
                task_num = input("Enter the task number to remove: ")
                remove_task(task_num)

        elif choice == "4":

            # Task 2.5.3
            print("Thank you for using the To-Do List App. Goodbye!")
            break

        else:

            # Task 2.5.4
            print("Invalid menu option. Please try again.")

# Task 2.6
if __name__ == "__main__":
    run_todo_app()
    store_task_list(todo_list)