import os

# os.listdir list dirs and files
d = [d for d in os.listdir('.')]
print(d)

d = [d for d in os.listdir('../')]
print(d)

d = [d for d in os.listdir('../../')]
print(d)