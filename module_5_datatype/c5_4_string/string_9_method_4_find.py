# string method

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

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

a = list(find_all('xxx xxx xxx xxx', 'xxx'))

print(a)





