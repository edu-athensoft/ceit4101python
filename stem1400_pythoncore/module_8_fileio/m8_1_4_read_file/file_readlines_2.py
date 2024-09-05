"""
readlines() returns a list of remaining lines of the entire file
"""

f = open("file_readline.txt", 'r')

# readline specified lines
lines = f.readlines()
print(lines[0:3])

f.close()