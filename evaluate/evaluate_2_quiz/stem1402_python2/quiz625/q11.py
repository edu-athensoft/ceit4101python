"""
11. Write a program to count target strings aaa in a list.
my_list = ['aaa 1B2', 'H3B aaa', 'H3A aaa', 'aaa 2X8', 'H4A 2D8']

"""

my_list = ['aaa 1B2', 'H3B aaa', 'H3A aaa', 'aaa 2X8', 'H4A 2D8']

TARGET = 'aaa'
newlist = []

DELIMITER = ' '
for item in my_list:
    if ' ' in item:
        pos = item.index(DELIMITER)
        newlist.append(item[:pos])
        newlist.append(item[pos+1:])

result = newlist.count(TARGET)
print(result)
