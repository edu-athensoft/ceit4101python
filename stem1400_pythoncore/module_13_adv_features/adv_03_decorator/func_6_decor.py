"""
decorator with parameters
"""


def mydecor(myparam):
    def wapper(myfunc):
        def inner_wapper(*args, **kwargs):
            print("before "+str(myparam))
            myfunc(*args, **kwargs)
            print("after")

        return inner_wapper

    return wapper


@mydecor("p1")
def biz():
    print("biz()")


@mydecor("p2")
def biz2():
    print("biz2()")

biz()
print()
biz2()