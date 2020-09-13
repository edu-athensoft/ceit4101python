from decimal import Decimal, ROUND_HALF_UP

our_value = Decimal(16.0/7)
output = Decimal(our_value.quantize(Decimal('.001'), rounding=ROUND_HALF_UP))

print(output)

# import decimal
#
# our_value = decimal.Decimal(16.0/7)
# output = decimal.Decimal(our_value.quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))


# from decimal import Decimal as D, ROUND_HALF_UP as rhu
#
# our_value = D(16.0/7)
# output = D(our_value.quantize(D('.01'), rounding=rhu))
