"""
module 5
chapter 2.7.2
list comprehension - filter
"""

# origin list
origin = list(range(10))
# origin = [x for x in range(10)]
print(origin)

# filter
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

# filter
odd = [x for x in range(20) if x % 2 == 1]
print(odd)

# nested for
combinations = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
print(combinations)



