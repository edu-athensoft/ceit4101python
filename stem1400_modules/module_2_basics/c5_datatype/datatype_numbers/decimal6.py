print(16.0/7)

### round to 2 decimals

# 3: Round decimal by setting precision
# If you use deimcal, you need to import
from decimal import getcontext, Decimal

# Set the precision.
getcontext().prec = 3

# Execute 1/7, however cast both numbers as decimals
output = Decimal(16.0)/Decimal(7)

# Your output will return w/ 6 decimal places, which
# we set above.
print(output)