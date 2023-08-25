# declare a function
# call

def say_hello():
    """docstring say_hello()"""
    print("Hi, how are you")


say_hello()


def say_hello(name):
    """docstring say_hello(name)"""
    print("hi, how are you",name,"tttttt")

say_hello('Mary')
# say_hello()

print(say_hello.__doc__)