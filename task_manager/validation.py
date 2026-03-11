from datetime import datetime

def validate_task_title(title):
    if isinstance(title, str) and title.strip():
        return True
    raise ValueError("Invalid task title. Please provide a non-empty title.")

def validate_task_description(description):
    if isinstance(description, str) and description.strip():
        return True
    raise ValueError("Invalid task description. Please provide a non-empty description.")

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")