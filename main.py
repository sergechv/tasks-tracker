#!/usr/bin/env python3
import json
from datetime import datetime
import sys


def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            original_tasks = json.load(f)
            tasks = {int(key): value for key, value in original_tasks.items()}
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def main():
    tasks = load_tasks()

    def add(tasks):
        description = sys.argv[2]
        new_id = 0
        dt = datetime.now().replace(microsecond=0).isoformat()

        if tasks:
            new_id = max(tasks.keys()) + 1
        else:
            new_id = 1

        new_task = {
            "id": new_id,
            "description": description,
            "status": "to-do",
            "createdAt": dt,
            "updatedAt": dt
        }

        tasks[new_id] = new_task
        save_tasks(tasks)
        
        print(f'"{description}" succesfully added!')
    
    if sys.argv[1] == "add":
        add(tasks)

    def list_tasks(tasks):
        if len(sys.argv) < 3:
            tasks_list = list(tasks.values())
            for item in tasks_list:
                print(f'{item["description"]}')

    if sys.argv[1] == "list":
        list_tasks(tasks)


if __name__ == "__main__":
    main()
