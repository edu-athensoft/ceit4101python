from decimal import getcontext, Decimal

print(16.0 / 7)

# round to 3 decimals
# set the precision
getcontext().prec = 3

output = Decimal(16.0) / Decimal(7)

print(output)
