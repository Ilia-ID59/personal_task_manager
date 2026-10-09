name = input("whats your name ? ")
print(f"welcome {name}")

tasks = []

while True:
    title = input("enter task (or type 'exit' to finish) : ")
    if title == "exit":
        break
    tasks.append(title)

print("your tasks:")
for task in tasks:
    print("-", task)