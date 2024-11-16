"""
Reading the Last 10 Bytes
"""

with open("example.txt", "rb") as file:
    file.seek(-10, 2)  # Move 10 bytes before the end of the file
    print(file.read())  # Read the last 10 bytes


