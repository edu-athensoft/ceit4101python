"""
read selected single line
readlines() returns a list of remaining lines of the entire file
"""


def read_selected_single_line(_filename, line_no=0):
    with open(_filename, 'r') as file:
        # readline
        lines = file.readlines()
        # print(lines)

        if line_no < 0:
            line_no = 0
        if line_no >= len(lines):
            line_no = len(lines)-1

        print(lines[line_no], end="")



# test
filename = "myapp.log"
read_selected_single_line(filename)
read_selected_single_line(filename, 20)