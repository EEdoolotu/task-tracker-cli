# Task Tracker CLI

A simple command-line task tracker built in Python. This CLI tool allows you to add, list, complete, delete, edit, clear, sort, and search tasks. Tasks are stored persistently in a JSON file (`tasks.json`).

## Features

* Add new tasks
* List all tasks
* Mark tasks as complete
* Delete tasks by ID
* Edit task titles
* Clear all tasks
* Sort tasks by ID, title, or completion status
* Search tasks by keyword (case-insensitive)

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
```

2. Navigate to the project folder:

```bash
cd task-tracker-cli
```

3. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

## Usage

Run commands using Python:

```bash
python main.py <command> [arguments]
```

### Examples

```bash
python main.py add "Go to the gym"
python main.py list
python main.py complete 3
python main.py delete 2
python main.py edit 1 "Buy groceries"
python main.py clear
python main.py sort title
python main.py search gym
```

## JSON Storage

Tasks are stored in `tasks.json` in the project directory. Each task has:

* `id`: integer
* `title`: string
* `completed`: boolean

## Resources

* [Task Tracker Project Reference](https://roadmap.sh/projects/task-tracker)

## Contributing

Feel free to fork the project and submit pull requests for improvements.

## License

This project is open source and free to use.
