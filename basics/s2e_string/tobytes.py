# -*- coding: utf-8 -*-


# Chapter - fundamentals
# python encode to byte


x = b'ABC'
print(x)

a = 'ABC'.encode('ascii')
#b'ABC'
print(a)

b = '中文'.encode('utf-8')
#b'\xe4\xb8\xad\xe6\x96\x87'
print(b)

# c = '中文'.encode('ascii')
#error
print('\u4e2d')


