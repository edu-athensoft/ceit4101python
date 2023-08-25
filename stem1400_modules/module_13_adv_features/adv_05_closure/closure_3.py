"""
module: 15
closure

closure
the closure still works after the original function was removed

"""


def print_msg(msg):
    # outer enclosing function

    def printer():
        # the nested function
        print(msg)

    # printer()
    return printer  # returns the nested function


# calling this function.
another = print_msg("Hello Athensoft!")
another()

# remove original function
del print_msg

# still works
print("after del print_msg function")
another()
print("it still works")


