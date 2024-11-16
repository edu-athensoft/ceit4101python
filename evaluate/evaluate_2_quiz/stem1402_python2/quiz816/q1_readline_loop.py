"""
readline()
read lines by for-loop
"""

def read_line(_filename):
    with open(_filename, 'r') as file:
        # readline
        for line in file:
            print(line, end = '')

# test
filename = "myapp.log"
read_line(filename)
