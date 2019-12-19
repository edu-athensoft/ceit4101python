# Get all items of a dictionary with items()

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

my_items = sales.items();

print(my_items, type(my_items))


# How items() works when a dictionary is modified?
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

items = sales.items()
print('Original items:', items)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)

