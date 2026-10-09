# tasks.py
tasks = []

def add_task(title):
    tasks.append(title)

def show_tasks():
    print("your tasks:")
    for task in tasks:
        print("-", task)