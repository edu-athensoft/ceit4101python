"""
list all built-in functions
"""

import builtins  # Import the builtins module

# Get a list of all attributes (including functions) in the builtins module
builtin_attributes = dir(builtins)

# Filter the attributes to get only functions
builtin_functions = [attr for attr in builtin_attributes if callable(getattr(builtins, attr))]

# Print the list of built-in functions
count = 1
for func in builtin_functions:
    print(func, end="\t ")
    if count%5 ==0:
        print()
    count += 1
