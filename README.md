# Tasks-tracker

------

simple CLI tasks tracker to create, list, update and delete tasks. project from roadmap.sh [task tracker](https://roadmap.sh/projects/task-tracker)



------

## Features

- Add: Create a task with a description
- Update: Update the status of a task by its ID
- List: List all tasks or filter by status
- Delete: Delete a task by its ID

------

## Installation

```bash
git clone https://github.com/sergechv/tasks-tracker
cd tasks-tracker
chmod +x main.py
```

------

## Usage

```bash
$ ./main.py add "study python"
$ ./main.py list {to-do, in-progress, done} # all by default
$ ./main.py update id {to-do, in-progress, done}
$ ./main.py delete id
```

------

## License

MIT License
