print(16.0/7)

### round to 2 decimals

# 2: Round decimal with super rounding powers
from decimal import Decimal, ROUND_HALF_UP
# Here are all your options for rounding:
# This one offers the most out of the box control
# ROUND_05UP       ROUND_DOWN       ROUND_HALF_DOWN  ROUND_HALF_UP
# ROUND_CEILING    ROUND_FLOOR      ROUND_HALF_EVEN  ROUND_UP

our_value = Decimal(16.0/7)
output = Decimal(our_value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))

print(output)