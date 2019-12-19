# string formatting

my_string = " My favorate hobby is \"Hockey\". "
print(my_string)

# ignore all escape char or sequence
my_string = r"My favorate hobby is \"Hockey\""
print(my_string)

my_string = r"My favorate hobby is \"Hockey\""
print(my_string)


# formatting out
# format()
# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)


# formatting integers
print("Binary representation of {0} is {0:b}".format(12))
print("Octal representation of {0} is {0:o}".format(12))
print("Hex representation of {0} is {0:x}".format(12))

# formatting floats
print("Exponent representation: {0:e}".format(1566.345))
print("Exponent representation: {0:e}".format(0.0001566345))

# round off
print(1/3)
print("One third is: {0:.3f}".format(1/3))
print("One third is: {0:.2f}".format(1/3))
print("One third is: {0:.1f}".format(1/3))
# print("One third is: {0:d}".format(1/3))        # ValueError


# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))
print("|{:<10}|{:^10}|{:>10}|".format('butter11111111111111111',
                                      'breadddddddddddddddddddddd',
                                      '22222222222222222ham'))


# Old style formatting
# round
x = 12.3456789
print('The value of x is %3.2f' %x)
x = 1.23456789
print('The value of x is %3.2f' %x)
x = 0.123456789
print('The value of x is %3.2f' %x)
x = 0.123456789
print('The value of x is %4.2f teststring' %x)
