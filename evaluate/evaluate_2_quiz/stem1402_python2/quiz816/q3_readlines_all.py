"""
readlines() returns a list of remaining lines of the entire file
"""


def read_file_by_line(_filename):
    with open(_filename, 'r') as file:
        # readline
        lines = file.readlines()
        # print(lines)

        for line in lines:
            print(line, end="")

# test
filename = "myapp.log"
read_file_by_line(filename)