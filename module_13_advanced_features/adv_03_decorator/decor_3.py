"""
decorator
with @ symbol
"""


def currency(fn):
    def wrapper(*args, **kwargs):
        return f'${fn(*args, **kwargs)}'
    return wrapper


@currency
def total(amount, tax_rate):
    return amount * (1 + tax_rate/100)


# test
print(total(100, 5))

