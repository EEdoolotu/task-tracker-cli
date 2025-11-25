import sys
import json
import functions

def open_file():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        

def save_file(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

commands = {
        "add" : functions.add_task,
        "list" : functions.list_tasks,
        "complete" : functions.complete_task,
        "delete" : functions.delete_task,
        "edit" : functions.edit_task,
        "clear" : functions.clear_tasks,
        "sort" : functions.sort_tasks,
        "search" : functions.search_tasks
    }

def main():
    if len(sys.argv) < 2:
        print("Please provide a command")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    tasks = open_file()


    if command in commands:
        commands[command](tasks, args)
        save_file(tasks)
    else:
        print(f"Unknown command: {command}")



if __name__ == "__main__":
    main()
