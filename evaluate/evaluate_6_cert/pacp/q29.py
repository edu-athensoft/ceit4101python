"""
q29. what is the output?

output:
<generator object f at 0x0178EDF0>

"""

def f(n):
  for i in range(1, n+1):
    yield i

print(f(2))

# result = f(2)
# print(result)

