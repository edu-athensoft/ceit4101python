"""
Moving to the End of a File
"""

with open("example.txt", "rb") as file:  # Binary mode required for nonzero end-relative seeks
    file.seek(0, 2)  # Move to the end of the file
    print(file.tell())  # Print the position of the file pointer (file size in bytes)

