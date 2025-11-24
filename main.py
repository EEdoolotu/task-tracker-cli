import sys
import json

def open_file(file):
    with open(f"{file}", "r") as file:
        tasks = json.load(f"{file}")

def save_file(file):
    with open(f"{file}", "w") as file:
        json.dump(tasks, f"{file}", indent=4)

def main():
    print("Hello from task-tracker-cli!")


if __name__ == "__main__":
    main()
