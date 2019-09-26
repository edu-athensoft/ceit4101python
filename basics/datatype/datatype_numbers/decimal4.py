print(16.0/7)

### round to 2 decimals
from decimal import Decimal

# First we take a float and convert it to a decimal
x = Decimal(16.0/7)

# Then we round it to 2 places
output = round(x,2)
print(output)