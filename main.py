import os
from dotenv import load_dotenv
from tasks import add_task, show_tasks, save_tasks, load_tasks

load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

open_admin = input("do u want to open admin mode ? yes/no : ")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password : ")
    if entered_password == admin_password:
        print("admin hi...")
    else:
        print("wrong password")  

name = input("whats your name ? ")
print(f"welcome {name}")

tasks = load_tasks()

while True:
    title = input("enter a task (or type 'exit' to finish) : ")
    if title.lower() == "exit":
        break

    priority = input("priority (low/medium/high) : ").lower()
    while priority != "low" and priority != "medium" and priority != "high":
        print("invalid priority, choose low, medium or high")
        priority = input("priority (low/medium/high) : ").lower()

    add_task(tasks, title, priority)
    save_tasks(tasks)

show_tasks(tasks)

print("tasks saved")
