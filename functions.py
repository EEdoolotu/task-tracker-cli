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

def complete_task(args):
    pass

def delete_task(args):
    pass

def edit_task(args):
    pass

def clear_tasks(args):
    pass

def sort_tasks(args):
    pass

def search_tasks(args):
    pass
