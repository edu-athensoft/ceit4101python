# exponent function
# loop


def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result *= base
    return result


print(raise_to_power(3,2))


