"""
random module

generating random numbers


"""
import random

# generate a raw random number
r = random.random()
print(r)

# generate a random number of int type within a range
a = random.randrange(10, 20)
print(a)

# generate a random number of int type within a range
b = random.randint(1, 6)
print(b)

# generate a random number of float type
f = random.uniform(10, 20)
print(f)
