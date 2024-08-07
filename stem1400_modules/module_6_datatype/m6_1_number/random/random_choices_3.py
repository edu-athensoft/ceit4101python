"""
random.choices()

random.choices() 是 Python 的 random 模块中的一个函数，用于从一个序列中随机选择元素，支持权重。
与 random.choice() 不同的是，random.choices() 允许有放回地选择多个元素。
"""

import random

# define items
prizes = ['First Prize', 'Second Prize', 'Third Prize', 'Fourth Prize', 'Fifth Prize']

# define weights (probabilities)
# from smallest to largest
weights = [2, 10, 100, 250, 638]

# pull N times
N = 100
draws = random.choices(prizes, weights=weights, k=N)

# output
for item in draws:
    print(f'The winner is: {item}')