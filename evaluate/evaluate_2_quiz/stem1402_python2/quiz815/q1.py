"""
1. Reading the Entire File
Write a Python function called read_entire_file that opens a text file named
"sample.txt" in read mode and returns its entire content as a string.
Use the read() method to do this.

If the file does not exist,
catch the exception and return the message "File not found".
"""


def read_entire_file():
    try:
        with open("q1_sample.txt", "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"

# Test case
print(read_entire_file())
# Expected output: Contents of "sample.txt" or "File not found"
