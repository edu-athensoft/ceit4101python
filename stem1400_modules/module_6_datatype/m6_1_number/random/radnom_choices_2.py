"""
usage of random.choices()

random.choices(population, weights=None, cum_weights=None, k=1)
"""
import random

# no weight, equal weight
items = ['apple', 'banana', 'cherry']
selected = random.choices(items, k=3)
print(selected)


# equal weight
weights = [1, 1, 1]
selected = random.choices(items, weights=weights, k=3)
print(selected)

# with weight
weights = [10, 1, 1]
selected = random.choices(items, weights=weights, k=3)
print(selected)

