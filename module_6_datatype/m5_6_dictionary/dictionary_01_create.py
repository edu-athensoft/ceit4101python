#
my_dict = {}
print(my_dict, type(my_dict))

#
my_dict = {
    1: 'mon',
    2: 'tue',
    3: 'wed',
    4: 'thu',
    5: 'fri',
    6: "sat",
    7: "sun"
}
print(my_dict)


my_dict = {
    "M": 'mon',
    "T": 'tue',
    "W": 'wed',
    "H": 'thu',
    "F": 'fri',
    "S": "sat",
    "N": "sun"
}
print(my_dict)


my_dict = {
    "M": 'mon',
    "T": 'tue',
    "W": 'wed',
    "H": 'thu',
    "F": 'fri',
    "S": "sat",
    "S": "sun"
}
print(my_dict)



my_dict = {
    1: 'mon',
    2: 'tue',
    3: 'wed',
    "H": 'thu',
    "F": 'fri',
    "S": "sat",
    "S": "sun"
}
print(my_dict)

# Can value be None?
# YES

# Can key be None?
# YES

# Can it be more than 1 None?
# YES, but the last one takes effect

# Can key be ''?
# YES

my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)

