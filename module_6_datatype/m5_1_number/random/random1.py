import random

a = random.randrange(10,20)
print(a)

b = random.randint(1,6)
print(b)


x = ['a','b','c','d','e','f']
index = random.randint(0,5)
print(x[index])

print(random.choice(x))

random.shuffle(x)
print(x)

print(random.random())

