"""
string method - split()
"""

# case 1.
text = "This is a long sentence"

# split text at space
print('case 1')
a = text.split()
print(type(a))

print(a)

for word in a:
    print(word)

# case 2.
text = "This is a long sent\tence"
print('case 2')
a = text.split()
print(a)

# case 3.
text = "Th\nis is a lo\nng sent\tence"
print('case 3')
a = text.split()
print(a)
print()

# split() with maxsplit
fruits = 'apple, orange, cherry, banana'
print(fruits.split())

# case 4.
print(fruits.split(', '))

# case 5.
print(fruits.split(', ', 2))

# case 6.
print(fruits.split(', ', 1))

# case 7.
print(fruits.split(', ', 5))

# case 8.
print(fruits.split(', ', 0))


# application

