# set method
# different update

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)


#
A = {'a', 'c', 'g', 'f'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)



#
A = {'a', 'x', 'y'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)

print('A = ', A)
print('B = ', B)
print('result = ', result)