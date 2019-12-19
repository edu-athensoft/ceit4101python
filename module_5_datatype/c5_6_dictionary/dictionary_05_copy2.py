# Using = Operator to Copy Dictionaries

original = {1:'one', 2:'two'}
new = original

#
print(id(original), id(new))

print(original is new)

new[3]='car'
print('original',original)
print('new',new)

