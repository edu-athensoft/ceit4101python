"""
Moving to the Start of a File
"""

with open("example.txt", "r") as file:
    file.seek(0)  # Move to the start of the file
    print(file.read(5))  # Read the first 5 characters
