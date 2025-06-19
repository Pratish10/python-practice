"""
This script demonstrates Python's exception handling using `try`, `except`, `finally`, and covers three key scenarios:

1. Division with Error Handling:
   - Takes two integer inputs from the user.
   - Performs division and handles potential `ValueError` (non-numeric input) and `ZeroDivisionError`.

2. File Reading with Error Handling:
   - Attempts to open and read from a file named 'non_existent.txt'.
   - Handles `FileNotFoundError` if the file does not exist.
   - Once tested, you can create the file manually with some text and re-run the script to see successful reading.

3. Generic Exception Handling with List Indexing:
   - Asks the user for an index to access an element in a predefined list.
   - Uses a general `Exception` catch block to handle any unexpected errors.
   - Uses a `finally` block to indicate the attempt is complete regardless of success or failure.

This script serves as a practical demonstration of robust error handling in common Python scenarios.
"""

print("--- Division with Error Handling ---")
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result of division: {num1} / {num2} = {result}")
except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("\n--- File Reading with Error Handling ---")
try:
    test_file = "non_existent.txt"
    with open(test_file, "r") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: The file '{test_file}' was not found. Please make sure it exists.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
else:
    print(f"Successfully read content of '{test_file}':\n{content}")
    print("File reading operation completed successfully (from else block).")
finally:
    pass

print("\n--- Generic Exception Handling & Finally ---")
try:
    my_list = [1, 2, 3]
    index = int(input("Enter an index to access an element from the list [1, 2, 3]: "))
    print(f"Element at index {index}: {my_list[index]}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Completed list access attempt (with or without exception).")
