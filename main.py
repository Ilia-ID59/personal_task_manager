from tasks import add_task, show_tasks

name = input("whats your name ? ")
print(f"welcome {name}")

while True:
    title = input("enter task (or type 'exit' to finish) : ")
    if title == "exit":
        break
    add_task(title)

show_tasks()