"""
estimated time
"""

# estimated time


from datetime import *


def duration(*args):
    def wrapper(func):
        def inner_wapper(*args, **kwargs):
            start_time = datetime.now()
            print(f"started at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
            func(*args, **kwargs)
            end_time = datetime.now()
            print(f"ended at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"duration: {(end_time - start_time).microseconds} us")

        return inner_wapper

    return wrapper


@duration()
def foo():
    print("foo()")


foo()