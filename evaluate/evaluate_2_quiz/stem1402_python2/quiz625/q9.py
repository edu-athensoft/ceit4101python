"""
q9.Write a program to count target strings xyz in a list.
my_list = ['abc xyz', 'abb xyz', 'bab xxx', 'bbb yyz', 'cab xyz']
Constraints:  without using string split()
"""

my_list = ['abc xyz', 'abb xyz', 'bab xxx', 'bbb yyz', 'cab xyz']

TARGET = 'xyz'
newlist = []

DELIMITER = ' '
for item in my_list:
    if ' ' in item:
        pos = item.index(DELIMITER)
        newlist.append(item[:pos])
        newlist.append(item[pos+1:])

result = newlist.count(TARGET)
print(result)
