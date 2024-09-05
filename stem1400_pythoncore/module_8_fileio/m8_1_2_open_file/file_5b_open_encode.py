"""
encoding
"""

FILE_NAME = "file5_encode_zh.txt"
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


# on old computers
# f = open(FILE_NAME, mode = 'r', encoding='ascii')
# content = f.read()
# f.close()
# print(content)
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe8 in position 70: ordinal not in range(128)