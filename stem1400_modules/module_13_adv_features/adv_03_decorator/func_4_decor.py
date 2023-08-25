"""
decorator

Decorators should be universal
"""


def simple_decorator(own_function):
    def internal_wrapper(*args, **kwargs):
        print('before')
        own_function(*args, **kwargs)
        print('after')

    return internal_wrapper


@simple_decorator
def combiner(a, b):
    print("combiner()")
    print(a+b)


combiner(1,2)




