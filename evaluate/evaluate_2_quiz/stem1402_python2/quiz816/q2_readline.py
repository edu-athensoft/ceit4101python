"""
readline()
read all lines
"""

def read_file_by_line(_filename):
    with open(_filename, 'r') as file:
        # readline
        while True:
            line = file.readline()
            if line:
                print(line, end="")
            else:
                break

# test
filename = "file_readline.txt"
read_file_by_line(filename)