def add_task(tasks, args):
    new_task = {
        "id": max((task["id"] for task in tasks), default=0) + 1,
        "title": " ".join(args),
        "completed" : False
    }
    tasks.append(new_task)
    print(f'Task added: {new_task["id"]}. {new_task["title"]}')

def list_tasks(tasks, args):
    complete = "[x]"
    pending = "[ ]"
    for task in tasks:
        if task["completed"]:
            print(f'{task["id"]}. {complete} {task["title"]}')
        else:
            print(f'{task["id"]}. {pending} {task["title"]}')

def complete_task(tasks, args):
    task_id = int(args[0])
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f'Task {task_id} marked as complete.')
            return
        
    print("Could not find task.")

def delete_task(tasks, args):
    if not args:
        print("Please provide a task ID to delete.")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print("Please provide a valid number.")
        return
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            print(f'Task {task_id} deleted')
            return
    print(f'Could not find task with ID {task_id}')

def edit_task(tasks, args):
    if not args:
        print("Please provide a task ID to edit.")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print("Please provide a valid number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = " ".join(args[1:])
            print(f'Task {task_id} marked as edited.')
            return
            
    print(f'Could not find task with ID {task_id}')


def clear_tasks(tasks, args):
    tasks.clear()
    print("Tasks are cleared.")

def sort_tasks(tasks, args):
    if not args:
        print("Please provide a field to sort by.")
        return

    sort_key = args[0].lower()
    if sort_key in ["id", "title", "completed"]:
        tasks.sort(key=lambda task: task[sort_key])
    else:
        print("Please provide a valid field to sort by (id, title, completed).")

    print(f"Tasks sorted by {sort_key}.")


    

def search_tasks(tasks, args):
    if not args:
        print("Please provide a word to search by") 
        return

    search_key = " ".join(args).lower()
    found = False

    for task in tasks:
        if search_key in task["title"].lower():
            status = "[x]" if task["completed"] else "[ ]"
            print(f'{task["id"]}. {status} {task["title"]}')
            found = True

    if not found:    
        print("Could not find the searched item")        
