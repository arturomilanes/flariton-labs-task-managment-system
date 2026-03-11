from datetime import datetime

# Import validation functions
import validation 

# Define tasks list
tasks = {"title": "Groceries",
 "description": "Shop at Market Basket for food", 
 "due_date": "2024-06-26",
 "completed": True}


# Implement add_task function
def add_task(title, description, due_date):
    if validation.validate_task_title(title) and validation.validate_task_description(description) and validation.validate_due_date(due_date):  
        task = { "title": title,
                "description": description,
                "due_date": due_date,
                "completed": False}
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Failed to add task. Please check the input values.")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return
    pending_tasks=[]
    for task in tasks:
        if task["completed"] == False:
            pending_tasks.append(task)
    return pending_tasks

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return 
    pending_tasks = view_pending_tasks(tasks)
    total_tasks_count = len(tasks)
    completed_tasks_count = total_tasks_count - len(pending_tasks)

    progress_decimal = round(completed_tasks_count/total_tasks_count, 2)

    progress = progress_decimal * 100
    return progress