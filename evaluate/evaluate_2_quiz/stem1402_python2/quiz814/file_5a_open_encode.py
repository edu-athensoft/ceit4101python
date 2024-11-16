"""
encodings
"utf-8"
"ascii"
"iso-8859-1"
cp1252
"""

FILE_NAME = "file5_encode_en.txt"
FILE_NAME = "file5_encode_fr.txt"
print(FILE_NAME)


# on linux
f = open(FILE_NAME, mode = 'r', encoding='utf-8')
content = f.read()
f.close()
print(content)


# on windows
f = open(FILE_NAME, mode = 'r', encoding='cp1252')
content = f.read()
f.close()
print(content)

# ascii
f = open(FILE_NAME, mode = 'r', encoding='iso-8859-1')
content = f.read()
f.close()
print(content)

# on old computers
# f = open(FILE_NAME, mode = 'r', encoding='ascii')
# content = f.read()
# f.close()
# print(content)

