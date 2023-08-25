# string method

print("Original is","PrOgRaMiZ")

print("PrOgRaMiZ".lower())

my_str= "PrOgRaMiZ"
print("lower()",my_str.lower())

my_str= "PrOgRaMiZ"
print("upper()",my_str.upper())
print()

# split a string into list
# string.split()
my_str= "This will split all words into a list"
print(my_str)
a = my_str.split()
print(a, type(a))
print()

# string.join()
result = ' '.join(a)
print(result, type(result))

result = ''.join(a)
print(result, type(result))

result = ','.join(a)
print(result, type(result))
print()

# find the first matched string and stop
# string.find()
my_str = 'Happy New Year'
print(my_str.find('ew'))
print(my_str.find('x'))


my_str = 'Happy New Year ew aaa bbb cewcc'
print(my_str.find('ew'))
print(my_str.find('ew',9))
print(my_str.find('ew',17, 30))
print()

# rfind
result = my_str.rfind('ew')
print(result, type(result))

# find all





