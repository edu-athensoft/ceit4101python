"""
seek(move) the current position
seek(offset, 0)
"""

f = open("file_seek_1.txt", 'r')

# read the first 4 char
print(f"The current position: {f.tell()}")
print(f.read(4))
print(f"The current position: {f.tell()}")

# move cursor to the beginning
# f.seek(2)
f.seek(2,0)
print(f"The current position: {f.tell()}")
print(f.read(4))
print(f"The current position: {f.tell()}")

f.close()