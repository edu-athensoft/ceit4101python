"""
6. Write code to convert a sequence of characters to a string without using string APIs.
Sample input:  ('P', 'y', 't', 'h', 'o', 'n')
Sample output:   'Python'
"""

t1 = ('P', 'y', 't', 'h', 'o', 'n')

s1 = ''

for s in t1:
    s1 += s

print(s1)