FILENAME = "tasks.txt"


def add_task(tasks, title, priority):
    task = {"title": title, "priority": priority}
    tasks.append(task)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        print("\nyour tasks :")
        for t in tasks:
            print("-", t["title"], "| priority:", t["priority"])


def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for t in tasks:
            file.write(t["title"] + "|" + t["priority"] + "\n")


def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split("|")
                title = parts[0]
                if len(parts) > 1:
                    priority = parts[1]
                else:
                    priority = "medium"
                tasks.append({"title": title, "priority": priority})
    except FileNotFoundError:
        pass
    return tasks