import fractions

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# limit denominator
print(fractions.Fraction(1.1).limit_denominator())


print()


# As string
# Output: 11/10
print(fractions.Fraction('1.1'))