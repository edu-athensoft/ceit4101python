"""
readline()
read lines by for-loop
"""

f = open("file_readline.txt", 'r')

# readline
for line in f:
    print(line, end = '')

f.close()