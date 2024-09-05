"""
read part of content
"""

f = open("file_read_3.txt", 'r')

# read the first 4 char
print(f.read(4), end="")

# read the line-feed character
print(f.read(1), end="")

# read the next 4 char
print(f.read(4), end="")

f.close()

