# How update() works in Python?
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

# adds element with key 3
d1 = {3: "three"}
d.update(d1)
print(d)

print("update with key/value pairs")
# add key/value pairs
t1 = [(6, 'six')]
# t1 = (6, 'six')
d.update(t1)
print(d)

t2 = ((8, 'eight'), (7,'seven'))
d.update(t2)
print(d)

t3 = ((9, 'nine'),)
d.update(t3)
print(d)

d.update(x=99,y=999)
print(d)
