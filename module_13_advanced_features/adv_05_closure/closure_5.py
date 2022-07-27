"""
module: 15
closure

outer function returns the nested function with argument(s) passed to

example of defining closure and usage

checking data in the closure
"""


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

print()
# checking closure
print("checking closure")
print(make_multiplier_of.__closure__)

print("checking closure")
print(times3.__closure__)
print(times5.__closure__)
print()

print("checking closure")
print(times3.__closure__[0].cell_contents)

print("checking closure")
print(times5.__closure__[0].cell_contents)


