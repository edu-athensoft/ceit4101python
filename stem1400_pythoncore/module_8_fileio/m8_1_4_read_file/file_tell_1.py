"""
get the current position
"""

f = open("file_tell_1.txt", 'r')

# read the first 4 char
print(f"The current position: {f.tell()}")
print(f.read(4))

# read the line-feed character
print(f"The current position: {f.tell()}")
print(f.read(1))

# read the next 4 char
print(f"The current position: {f.tell()}")
print(f.read(4))

print(f"The current position: {f.tell()}")
f.close()