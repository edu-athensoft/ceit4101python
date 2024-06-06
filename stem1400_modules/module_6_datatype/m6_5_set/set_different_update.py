# set method
# different update

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
A.difference_update(B)
print('A = ', A)
print('B = ', B)
print()


#
A = {'a', 'c', 'g', 'f'}
B = {'c', 'f', 'g'}
A.difference_update(B)
print('A = ', A)
print('B = ', B)
print()


#
A = {'a', 'x', 'y'}
B = {'c', 'f', 'g'}
A.difference_update(B)
print('A = ', A)
print('B = ', B)
