"""
5. Reading File Line-by-Line Using read(size)
Write a Python function called read_lines_in_chunks that opens
a text file named "notes.txt" and reads it line by line, but each line
should be read in chunks of size characters, where size is provided as
an argument to the function. If a line is longer than size characters,
the function should read the line in multiple chunks and print each chunk.
"""

def read_lines_in_chunks(size):
    try:
        with open("myapp.log", "r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                for i in range(0, len(line), size):
                    print(line[i:i+size])
    except FileNotFoundError:
        print("File not found")

# Test case
read_lines_in_chunks(10)
