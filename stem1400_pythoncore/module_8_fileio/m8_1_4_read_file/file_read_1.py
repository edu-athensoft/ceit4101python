"""
read all content of a text file
"""

f = open("file_read_1.txt", 'r')
content = f.read()
f.close()

print(content)

