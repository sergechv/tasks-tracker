#!/usr/bin/env python3
import argparse
import json
from datetime import datetime


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
    parser = argparse.ArgumentParser(prog="Prog")
    subparsers = parser.add_subparsers(dest="command")
    add_parser = subparsers.add_parser("add", help="Add a task to the list of tasks")
    add_parser.add_argument("description", type=str)
    update_parser = subparsers.add_parser("update", help="Update the status of a task")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("status", choices=["to-do", "in-progress", "done"])
    list_parser = subparsers.add_parser(
        "list", help="list all tasks or filter by status"
    )
    list_parser.add_argument("-s", "--status", choices=["to-do", "in-progress", "done"])
    delete_parser = subparsers.add_parser("delete", help="Delete a task by its id")
    delete_parser.add_argument("id", type=int)
    args = parser.parse_args()
    dt = datetime.now().replace(microsecond=0).isoformat()

    def add(tasks, args):
        description = args.description
        new_id = 0

        if tasks:
            new_id = max(tasks.keys()) + 1
        else:
            new_id = 1

        new_task = {
            "id": new_id,
            "description": description,
            "status": "to-do",
            "createdAt": dt,
            "updatedAt": dt,
        }

        tasks[new_id] = new_task
        save_tasks(tasks)

        print(f'"{description}" succesfully added!')

    if args.command == "add":
        add(tasks, args)

    def list_tasks(tasks, args):
        tasks_list = list(tasks.values())

        for item in tasks_list:
            if item["status"] == args.status or not args.status:
                print(
                    f"{item['description']} id: {item['id']} status: {item['status']}"
                )

    if args.command == "list":
        list_tasks(tasks, args)

    def update_list(tasks, args):
        try:
            tasks[args.id]["status"] = args.status
            tasks[args.id]["updatedAt"] = dt
            save_tasks(tasks)
            print("Task updated")

        except KeyError:
            print(f"Invalid key, '{args.id}' does not exists")

    if args.command == "update":
        update_list(tasks, args)

    def delete_tasks(tasks, args):
        try:
            del tasks[args.id]
            save_tasks(tasks)
            print("Tasks deleted")
            raise KeyError
        except KeyError:
            print("Not a valid id")

    if args.command == "delete":
        delete_tasks(tasks, args)


if __name__ == "__main__":
    main()
