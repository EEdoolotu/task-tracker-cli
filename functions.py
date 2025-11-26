def add_task(args):
    pass

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
