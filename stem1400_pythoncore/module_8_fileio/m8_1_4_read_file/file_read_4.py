"""
read part of content
"""

f = open("file_read_4.txt", 'r')

# read the first 8 char
print(f.read(8), end="")

# read the non-existing char
print(f.read(2), end="")

# print(f.read(10), end="")

f.close()

