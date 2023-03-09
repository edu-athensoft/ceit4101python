"""
string method - format_map()

"""

point = {'x':10, 'y':20}

print('{x} {y}'.format(**point))


print('{x} {y}'.format(x=10, y=20))


print('{x} {y}'.format_map(point))

