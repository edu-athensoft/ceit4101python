"""
decorator
with a decorator
"""


def total(amount, tax_rate):
    return amount * (1 + tax_rate/100)


def currency(fn):
    def wrapper(*args, **kwargs):
        return f'${fn(*args, **kwargs)}'
    return wrapper


# test
print('before decorating')
print(total(100, 5))

print('after decorating')
total = currency(total)
print(total(100,5))
