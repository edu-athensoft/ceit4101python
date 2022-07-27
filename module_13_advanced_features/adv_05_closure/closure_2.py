"""
module: 15
closure

closure
outer function returns the nested function with argument(s) passed to

"""


def print_msg(msg):
    # outer enclosing function

    def printer():
        # the nested function
        print(msg)

    # printer()
    return printer  # returns the nested function


# Now let's try calling this function.
another = print_msg("Hello Athensoft!")
another()
