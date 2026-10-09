FILENAME = "tasks.txt"


def add_task(tasks, task):
    tasks.append(task)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        print("\nyour tasks :")
        for t in tasks:
            print("-", t)


def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for t in tasks:
            file.write(t + "\n")


def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks
