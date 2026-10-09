from tasks import add_task, show_tasks, save_tasks, load_tasks

name = input("whats your name ? ")
print(f"welcome {name}")

tasks = load_tasks()

while True:
    task = input("enter a task (or type 'exit' to finish) : ")
    if task.lower() == "exit":
        break
    add_task(tasks, task)
    save_tasks(tasks)

show_tasks(tasks)

print("tasks saved")