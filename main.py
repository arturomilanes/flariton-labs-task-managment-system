
# Import functions from task_manager.task_utils package
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
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            task_utils.add_task(title, description, due_date)
        elif choice == "2":
            for index, task in enumerate(task_utils.tasks):
                print(f"{index}. {task['title']}")
                task_index = int(input("Which task would you like to mark as complete? Enter the index: "))
            task_utils.mark_task_as_complete(task_index)
        elif choice == "3":
            pending_task = task_utils.view_pending_tasks()
            if pending_task:
                print("Pending Tasks:")
                for task in pending_task:
                    print(f"Title: {task['title']}, Description: {task['description']}, Due Date: {task['due_date']}")
            else:
                print("No pending tasks.")
        
        elif choice == "4":
            progress = task_utils.calculate_progress()
            if progress is not None:
                print(f"Progress: {progress}%")
            else:
                print("No tasks available.")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
