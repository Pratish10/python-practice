my_tasks = [
    "Learn Python basics",
    "Practice DSA",
    "Build a Django app",
    "Read documentation",
]

print(f"Initial tasks: {my_tasks}")
print(f"First task: {my_tasks[0]}")
print(f"Last task: {my_tasks[-1]}")

my_tasks.append("Review Git commands")
print(f"List after appending: {my_tasks}")

my_tasks.insert(0, "Set up environment")
print(f"List after inserting: {my_tasks}")

my_tasks.remove("Build a Django app")
print(f"List after removing: {my_tasks}")

print(len(my_tasks))

if "Practice DSA" in my_tasks:
    print("Yes, Practice DSA is in the my_tasks list.")
else:
    print("No, Practice DSA is not in the my_tasks list.")
