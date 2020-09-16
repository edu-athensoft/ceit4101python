from decimal import Decimal as D

print(D(1.1)+D(2.2))

res = D('1.1') + D('2.2')
print(type(res))

print(res)


res = D('1.2') * D('2.50')
print(res)

res = D('1.2') * D('2.5')
print(res)

res = D('1.2') * D('2.500')
print(res)

