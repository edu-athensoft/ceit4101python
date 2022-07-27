"""
decorator
without any decorator
"""


def total(amount, tax_rate):
    return amount * (1 + tax_rate/100)


# test
print(total(100, 5))
