print(16.0/7)

### round to 3 decimals

from decimal import getcontext, Decimal

# Set the precision.
getcontext().prec = 3

output = Decimal(16.0)/Decimal(7)

print(output)