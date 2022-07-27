"""
random module

randomly choosing item
shuffle

"""
import random

# choose an item randomly from a collection
x = ['a', 'b', 'c', 'd', 'e', 'f']
index = random.randint(0, len(x)-1)
print('random index:', x[index])

# choose an item randomly from a collection
c = random.choice(x)
print('choice:', c)

print()

# shuffle a collection
print('original:', x)
random.shuffle(x)
print('shuffled:', x)
