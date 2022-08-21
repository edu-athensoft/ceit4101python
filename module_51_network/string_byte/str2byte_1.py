"""
str to bytes
"""

s = 'this is my message'

# str to bytes
byte_data = s.encode('utf-8')

# bytes
print(type(byte_data))
