"""
14. Write code to sort the following student names by last name
my_list = [['Peter', 'Liu'], ['Linda', 'Wang'], ['Kevin', 'Ma'], ['Cindy', 'Chen']]
"""

my_list = [['Peter', 'Liu'], ['Linda', 'Wang'], ['Kevin', 'Ma'], ['Cindy', 'Chen']]
my_list.sort(key=lambda item: item[1])
print(my_list)
