from datetime import datetime

def validate_task_title(title):
    size = len(title)
    if size > 500:
        raise ValueError("Title is too long. Please provide a title less than 500 characters.")
    if isinstance(title, str) and title.strip():
        return True
    raise ValueError("Invalid task title. Please provide a non-empty title.")

def validate_task_description(description):
    
    if len(description) > 500:
        raise ValueError("Task description is too long. Please provide a description less than 500 characters.")
    if isinstance(description, str) and description.strip():
        return True
    raise ValueError("Invalid task description. Please provide a non-empty description.")

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
def validate_index_task_as_complete(index, length):
    if index < 0 or index >= length:
        raise ValueError("Invalid task index. Please provide a valid index.")
    
def validate_task_already_completed(index, tasks):
    if tasks[index]["completed"]:
        raise ValueError("Task is already completed. Please select a pending task.")