"""
This script demonstrates the use of three important control flow statements in Python:
- break
- continue
- pass

Sections:
1. 'break':
 Iterates through numbers 1 to 9.
 If the number 7 is encountered, it prints a message and exits the loop early.

2. 'continue':
 Iterates through numbers 1 to 9.
 Skips printing the numbers 3 and 7 by continuing to the next iteration when encountered.



3. 'pass':
 A function `process_data` demonstrates the use of `pass` as a placeholder.
 - If `data` is None, it prints a message but continues.
 - If `data` is an empty list, it prints a message and exits early.
 - Otherwise, it proceeds to process and print the data.

This script is useful for understanding how to control loop flow and use placeholders in functions.
"""

print("--- Using break ---")

for i in range(1, 10):
    if i == 7:
        print("Number 7 encountered, breaking loop.")
        break
    print(i)

print("--- Using continue ---")

for i in range(1, 10):
    if i in (3, 7):
        print(f"Skipping number {i}.")
        continue
    print(i)


print("--- Using pass ---")


def process_data(data):
    if data is None:
        print("data was None but processing continues")
        pass

    if type(data) is list and len(data) == 0:
        print("Empty list received, no processing needed.")
        return
    else:
        print(f"Processing data: {data}")


process_data(None)
process_data([])
process_data([1, 2, 3])
