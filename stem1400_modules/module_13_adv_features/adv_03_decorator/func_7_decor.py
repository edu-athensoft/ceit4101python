"""
decorator with parameters

2.4.1.5 Decorators
Decorators can accept their own attributes
"""


def mydecor(myparam):
    def wapper(myfunc):
        def inner_wapper(*args, **kwargs):
            print("before " + str(myparam))
            myfunc(*args, **kwargs)
            print("after")

        return inner_wapper

    return wapper


@mydecor("p1")
def biz(*args):
    print(f"biz({args})")


@mydecor("p2")
def biz2(*args):
    print(f"biz2({args})")


biz(1, 2)
print()

biz2('a', 'b')
