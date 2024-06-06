"""
q10.Write a program to count target strings H3A in a list.
my_list = ['H3A 1B2', 'H3B 2A2', 'H3A 4C6', 'H3A 2X8', 'H4A 2D8']
Constraints:  without using string split()
"""

my_list = ['H3A 1B2', 'H3B 2A2', 'H3A 4C6', 'H3A 2X8', 'H4A 2D8']

TARGET = 'H3A'
newlist = []

DELIMITER = ' '
for item in my_list:
    if ' ' in item:
        pos = item.index(DELIMITER)
        newlist.append(item[:pos])
        newlist.append(item[pos+1:])

result = newlist.count(TARGET)
print(result)
