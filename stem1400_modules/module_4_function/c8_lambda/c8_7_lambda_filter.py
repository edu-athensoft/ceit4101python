"""
lambda

filter()

"""

# Program to filter out only the even items from a list
mylist = [1, 5, 4, 6, 8, 11, 3, 12]

print(filter(lambda x: x % 2 == 0, mylist))

new_list = list(filter(lambda x: x % 2 == 0, mylist))

# Output: [4, 6, 8, 12]
print(new_list)
