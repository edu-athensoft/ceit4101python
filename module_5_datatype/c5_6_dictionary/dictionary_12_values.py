# values() Parameters
# The values() method returns a view object that displays a list of all values in a given dictionary.

# Get all values from the dictionary




# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.values())



# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4, 'watermelon': 4 }

values = sales.values()
print('Original items:', values)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', values)