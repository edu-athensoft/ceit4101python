"""
Skipping Bytes
"""

with open("example.txt", "r") as file:
    file.seek(10)  # Move 10 characters from the start
    print(file.read(5))  # Read the next 5 characters

