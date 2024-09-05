"""
readlines() returns a list of remaining lines of the entire file
"""

f = open("file_readline.txt", 'r')

# readline
lines = f.readlines()
print(lines)

for line in lines:
    print(line, end="")

f.close()