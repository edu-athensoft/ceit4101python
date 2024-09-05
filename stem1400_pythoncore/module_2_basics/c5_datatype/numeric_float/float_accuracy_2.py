# accuracy of float
# method 2: using decimal module

# from decimal import *

from decimal import Decimal
from decimal import getcontext

getcontext().prec = 6
a = Decimal(1) / Decimal(7)
print(a)

getcontext().prec = 28
b = Decimal(1) / Decimal(7)
print(b)

getcontext().prec = 2
print(Decimal('3.00'))
print(Decimal(3.00))
print(Decimal(3.0))
print(Decimal(3))