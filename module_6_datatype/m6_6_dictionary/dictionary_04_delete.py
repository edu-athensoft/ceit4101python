# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}

# remove a particular item
# Output: 16
print(squares.pop(4))
# print(squares.pop(4)) # raise an KeyError
print(squares.pop(4,'no such key'))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# try out that using popitem() more than the length of dictionary
# if out-of-bound or overflow, an error raises

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
del squares[5]

# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
# print(squares)