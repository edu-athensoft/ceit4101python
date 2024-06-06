"""
1. Write a program to remove duplicates in a list.
my_list = ['p', 'y', 't', 'h', 'o', 'n', 'p', 'y', 't', 'h', 'o', 'n']

"""

my_list = ['p', 'y', 't', 'h', 'o', 'n', 'p', 'y', 't', 'h', 'o', 'n']

result = []
for item in my_list:
    if item not in result:
        result.append(item)

print(result)



