"""
number converting
"""


d1 = 100

# dec to binary as string
b1 = bin(d1)
print(b1, type(b1))

# dec to octal as string
b2 = oct(d1)
print(b2, type(b2))

# dec to hex as string
b3 = hex(d1)
print(b3, type(b3))

print('\n')

# ==========================
# bin to dec
b1 = 0b1100100
print(b1, type(b1))

str_b1 = '0b1100100'
d1 = int(str_b1, 2)
print(f"binary string to decimal: {d1}")

# bin to oct
o1 = oct(b1)
print(o1, type(o1))

# bin to hex
h1 = hex(b1)
print(h1, type(h1))

print('\n')

# ==========================
# oct to dec
o1 = 0o144
print(o1, type(o1))

str_o1 = '0o144'
d1 = int(str_o1, 8)
print(f"octal string to decimal: {d1}")


# oct to bin
b1 = oct(o1)
print(b1, type(b1))

# oct to hex
h1 = hex(o1)
print(h1, type(h1))

print('\n')

# ==========================
# hex to dec
h1 = 0x64
print(h1, type(h1))

str_h1 = '0x64'
d1 = int(str_h1, 16)
print(f"hexadecimal string to decimal: {d1}")

# hex to bin
b1 = bin(h1)
print(b1, type(b1))

# hex to oct
o1 = oct(h1)
print(o1, type(o1))


