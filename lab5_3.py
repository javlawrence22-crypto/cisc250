# Name: Javrick Lawrence
# LAB 5-3
# Date: 2026-5-28
# ============================================================

from pathlib import Path
import json


# Task 1: Save the task list
def store_task_list(task_list):
    """Saves the task list to a JSON file."""

    file_path = Path("task_list.json")

    # convert list to JSON string
    json_data = json.dumps(task_list)

    # write to file
    file_path.write_text(json_data)

    print("Task list has been saved successfully.")


# Task 2: Load the task list
def load_task_list():
    """Loads the task list from a JSON file. Returns empty list if file does not exist."""

    file_path = Path("task_list.json")

    if file_path.exists():
        data = file_path.read_text()
        return json.loads(data)
    else:
        return []