"""
This script demonstrates basic file handling operations in Python, including:
- Writing multiple lines to a new text file
- Reading and printing file content
- Appending new lines to the same file
- Reading and displaying the updated content

Key Steps:
1. Create and write initial content to 'my_document.txt'.
2. Read and print the contents of the file after writing.
3. Append additional lines to the file.
4. Read and print the contents of the file again to verify the appended lines.

This example provides a clear illustration of using modes:
- 'w' (write) to create or overwrite a file
- 'r' (read) to read file contents
- 'a' (append) to add to the end of an existing file
"""

# Writing example
lines_to_write = [
    "First line of text.",
    "Second line with more details.",
    "Third and final line for this demo.",
]

new_lines_to_append = ["\nAppended line one.", "Appended line two."]

with open("my_document.txt", "w") as f:
    for i in lines_to_write:
        f.write(f"{i}\n")

print("File has been created and written: my_document.txt")

print("--- Content of my_document.txt ---")
with open("my_document.txt", "r") as f:
    content = f.read()
    print(content)

with open("my_document.txt", "a") as f:
    for i in new_lines_to_append:
        f.write(i)

print("--- Content After Appending ---")
with open("my_document.txt", "r") as f:
    content = f.read()
    print(content)
