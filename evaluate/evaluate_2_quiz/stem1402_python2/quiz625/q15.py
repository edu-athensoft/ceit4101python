"""
14. Write code to sort the following student names by last name
my_list = ['Peter Liu', 'Linda Wang', 'Kevin Ma', 'Cindy Chen']
"""

my_list = ['Peter Liu', 'Linda Wang', 'Kevin Ma', 'Cindy Chen']

# by first name
my_list.sort()
print(my_list)


my_list = ['Peter Liu', 'Linda Wang', 'Kevin Ma', 'Cindy Chen']
# by last name
my_list.sort(key=lambda item: item[item.index(' ')+1:])
print(my_list)