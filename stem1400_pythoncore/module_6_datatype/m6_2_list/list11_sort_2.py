"""
sorting lists
sort()
"""

my_list = [[4, 'a'], [1, 'z'], [2, 'b'], [3, 'y'], [5, 'x']]
print(my_list)

# sort by 1st element
my_list.sort()
print(my_list)

# sort by 2nd element
my_list.sort(key=lambda item: item[1])
print(my_list)
