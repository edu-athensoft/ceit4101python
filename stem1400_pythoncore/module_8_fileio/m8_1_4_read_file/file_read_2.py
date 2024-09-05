"""
read part of content
"""

f = open("file_read_2.txt", 'r')

# read the first 4 char
print(f.read(4))

# read the next 4 char
print(f.read(4))

# read the next 4 char
print(f.read(4))

f.close()

