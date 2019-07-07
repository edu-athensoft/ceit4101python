# int -> float
a = float(10)
print(a)

# float -> int
b = int(10.6)
print(b)

# numeric -> str
c = str(10.6)
print(c, type(c))

# str -> numeric
d = float('10.7')
print(d, type(d))

e = int('10')
# e = int('10.7')
print(e, type(e))

s1 = set([1,2,3,1,2])
print(s1)

s2 = tuple({5,6,7,7})
print(s2)

s3 = list('hello world!')
print(s3)

s4 = dict([[1,2],[3,4],[5,6],[7,8]])
print(s4)

s5 = dict([(3,26),(4,44)])
print(s5)

s6 = dict(((3,26),(4,44)))
print(s6)