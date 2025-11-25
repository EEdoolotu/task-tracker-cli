tasks_file = "tasks.json"

def load_tasks():
    json.load("tasks.json")

def save_tasks(tasks):
    json.dump("tasks.json")