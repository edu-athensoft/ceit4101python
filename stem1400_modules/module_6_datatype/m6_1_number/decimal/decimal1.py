"""
Module 5. Data Types
chapter 1.3 - Python Decimal
"""


# 1.1 + 2.2 != 3.3
print("=== example 1 ===")
a = 1.1
b = 2.2
c = 3.3
print("a+b = ",a+b)
print("c = ",c)
print("a+b == c ?",a+b == c)
print("a+b > c ?",a+b > c)
print("a+b < c ?",a+b < c)
print()

# 3.3 == 3.3
d = 3.3
print(f"c={c}, d={d}")
print("c == d ?",c == d)
print("c is d ?", c is d)
print()

# other example
print("=== example 2 ===")
f11 = 1.0
f12 = 0.1
f2 = 0.9
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("f11 == f2 + f12 ?",f11 == f2 + f12)
print("f11-f12 == f2 ?",f11-f12 == f2)
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()

# decimal
print("=== example 3 ===")
f11 = 1.0
f12 = 0.3
f2 = 0.7
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("f11 == f2 + f12 ?",f11 == f2 + f12)
print("f11-f12 == f2 ?",f11-f12 == f2)
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()

# faction
print("=== example 4 ===")
f11 = 1.0
f12 = 0.33
f2 = 0.67
print("f11={}, f12={} and f2={}".format(f11,f12,f2))
print("f11 == f2 + f12 ?",f11 == f2 + f12)
print("f11-f12 == f2 ?",f11-f12 == f2)
print("f11-f12 > f2 ?",f11-f12 > f2)
print("f11-f12 < f2 ?",f11-f12 < f2)
print()


print(1.33+1.67)
print(1.11+1.25)    #
print(1.11+1.33)    #
print(0.1 + 0.2)    #
print(0.5 + 0.1)
print(0.1 + 0.2)    #
print(1.88+1.11)
print(2.11+1.33)
print(2.11+2.22)
print(1.111+1.333)
print(1.111+3.333)

# 0.1 + 0.2 might not exactly equal 0.3.
# 4.1 + 2.2 might not exactly equal 6.3.
# 5.5 + 1.1 might not exactly equal 6.6.

