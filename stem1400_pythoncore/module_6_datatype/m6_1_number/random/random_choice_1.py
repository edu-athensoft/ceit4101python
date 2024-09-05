"""
random.choice(sequence)

choose an item from a list
evenly distributed, does not support weights

"""
import random

my_list = [1, 2, 3, 4, 5]
selected_element = random.choice(my_list)
print(selected_element)