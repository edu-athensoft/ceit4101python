"""
read selected lines
readlines() returns a list of remaining lines of the entire file
"""


def read_selected_lines(_filename, start=0, stop=-1):
    with open(_filename, 'r') as file:
        # readline
        lines = file.readlines()
        # print(lines)

        if stop > 0:
            lines = lines[start:stop]
            for line in lines:
                print(line, end="")
        else:
            print("no lines selected.")



# test
filename = "myapp.log"
read_selected_lines(filename, start=0, stop=50)