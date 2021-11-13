"""
adding attribute to an instance
"""


class Duck:
    pass


# main program
duck1 = Duck()

# test non-existing attribute: name
member_list = dir(duck1)
# print(type(member_list))
if 'name' not in member_list:
    print('No such attribute: \'name\' defined in Duck class')

# adding and attribute
duck1.name = "Tom"
print(duck1.name)
