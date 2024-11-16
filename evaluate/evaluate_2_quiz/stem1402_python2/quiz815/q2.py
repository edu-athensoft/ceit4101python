"""
2. Reading a Specific Number of Characters
Write a Python function called read_n_characters that opens a text file named "data.txt"
and reads the first n characters, where n is provided as an argument to the function.

Use the read(size) method to accomplish this. Return the string of characters read from the file.

If the file does not contain enough characters, return all the characters that are available.
"""

def read_n_characters(n):
    try:
        with open("q2_data.txt", "r", encoding="utf-8") as file:
            content = file.read(n)
        return content
    except FileNotFoundError:
        return "File not found"

# Test case
print(read_n_characters(10))
# Expected output: First 10 characters or "File not found"

print(read_n_characters(76))
