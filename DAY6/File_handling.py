import os

# File Handling in Python - Examples

# 1. Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a Python file handling example.\n')

# 2. Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# 3. Reading line by line
with open('example.txt', 'r') as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())

# 4. Appending to a file
with open('example.txt', 'a') as file:
    file.write('This line is appended.\n')

# 5. Reading all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("\nAll lines as list:")
    print(lines)

# 6. Creating and writing multiple lines
with open('data.txt', 'w') as file:
    data = ['Name: John\n', 'Age: 25\n', 'City: New York\n']
    file.writelines(data)

# 7. Checking if file exists
if os.path.exists('example.txt'):
    print("\nFile exists!")
else:
    print("\nFile does not exist!")

# 8. Deleting a file
if os.path.exists('data.txt'):
    os.remove('data.txt')
    print("File deleted!")