
# Import functions from task_manager.task_utils package
from turtle import title

import task_manager.task_utils as task_utils
None
# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        print()
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            print()
            try:
                task_utils.add_task(title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}\n")

            #return_to_menu()

        elif choice == "2":
            pending_tasks = task_utils.view_pending_tasks()
            if not pending_tasks:
                print("No pending tasks.\n")
                continue
            tasks = task_utils.tasks
            for index, task in enumerate(tasks):
                if task in pending_tasks:
                    print(f"{index + 1}. {task['title']}\n")
            task_index = input("Which task would you like to mark as complete? Enter the index: ")
            print()
            try:
                completed = task_utils.mark_task_as_complete(int(task_index)-1)
            
                
                if completed:
                    #print(f"{tasks[int(task_index) -1]['title']}: marked as complete!\n")
                    print("Task marked as complete!\n")
                else:
                    print("Failed to mark task as complete. Please check the index and try again.\n")
                
                #return_to_menu()

            except ValueError as e:
                            print(f"Error: {e}\n")

        elif choice == "3":
            pending_task = task_utils.view_pending_tasks()
            if pending_task:
                print("Pending Tasks:\n")
                for task in pending_task:
                    print(f"Title: {task['title']}")
                    print(f"Description: {task['description']}")
                    print(f"Due Date: {task['due_date']} \n")
            else:
                print("No pending tasks.\n")

            #return_to_menu()
        
        elif choice == "4":
            #percentage_progress, completed_tasks_count = task_utils.calculate_progress()
            percentage_progress = task_utils.calculate_progress()
            tasks = task_utils.tasks

            if percentage_progress is not None:
                #print(f"Progress: {percentage_progress}% completed:  {completed_tasks_count} out of {len(tasks)} tasks\n")
                print(f"Progress: {percentage_progress}%\n")
            else:
                print("No tasks available.\n")

            #return_to_menu()

        elif choice == "5":
            print("Exiting the program... \n")
            break
        else:
            print("Invalid choice. Please try again\n")

def return_to_menu():
    return input("press enter to continue...")

if __name__ == "__main__":
    main()
