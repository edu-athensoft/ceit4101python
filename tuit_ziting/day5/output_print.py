print('This sentence is output to the screen')

a = 5

print('The value of a is', a)


print(1,2,3,4)

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='\n')



x = 5
y = 6
print('let me add {} and {}, and I got {}'.format(x,y,x+y))

print('let me add {2} and {1}, and I got {0}'.format(x,y,x+y))

print('let me add {opt1} and {opt2}, and I got {result}'.format(opt1 = x, opt2 = y, result = x+y))


x = 12.3456789
print('The value of x is %3.2f' %x)