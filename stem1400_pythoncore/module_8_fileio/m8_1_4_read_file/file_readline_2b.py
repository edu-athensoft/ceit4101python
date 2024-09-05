"""
readline()
read all lines
"""

f = open("file_readline.txt", 'r')

# readline
while True:
    line = f.readline()
    if line:
        print(line, end="")
    else:
        break

f.close()