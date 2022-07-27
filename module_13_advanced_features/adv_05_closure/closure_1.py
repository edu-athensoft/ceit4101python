"""
module: 15
closure

not closure yet, but nested function

"""


def print_msg(msg):
    # outer enclosing function

    def printer():
        # the nested function
        print(msg)

    printer()


# executing the function
print_msg("Hello Athensoft!")
