from datetime import datetime

# Import validation functions
import task_manager.validation as validation

# Define tasks list
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    if (validation.validate_task_title(title) and 
        validation.validate_task_description(description) and 
        validation.validate_due_date(due_date)): 

        task = { "title": title,
                "description": description,
                "due_date": due_date,
                "completed": False}
        tasks.append(task)
        print("Task added successfully!\n")
    else:
        print("Failed to add task. Please check the input values.")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    validation.validate_index_task_as_complete(index, len(tasks))

    validation.validate_task_already_completed(index, tasks)
    
    tasks[index]["completed"] = True
    return tasks[index]["completed"]
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    if not tasks:
        return
    pending_tasks=[]
    for task in tasks:
        if task["completed"] == False:
            pending_tasks.append(task)
    return pending_tasks

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 
    pending_tasks = view_pending_tasks(tasks)
    total_tasks_count = len(tasks)
    completed_tasks_count = total_tasks_count - len(pending_tasks)

    progress_decimal = round(completed_tasks_count/total_tasks_count, 2)

    progress = progress_decimal * 100
    return progress, completed_tasks_count