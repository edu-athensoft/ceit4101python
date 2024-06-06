"""
random.sample()
unlike choices(), it does not allow to choose duplicate items
"""

import random

# data
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# choose 3 fruits randomly
selected_fruits = random.sample(fruits, k=3)
print(selected_fruits)