print('This sentence is output to the screen')


a = 'aaaaaaa'
print('The value of a is', a)


print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')

print(1,2,3,4,sep='#',end='&')

print(1,2,3,4,sep='#')


x=5
y=6
print("Let me add {} and {}, and I got the sum of {}".format(x,y,x+y))

print("Let me add {2} and {1}, and I got the sum of {0}".format(x,y,x+y))

print("Let me add {opt1} and {opt2}, and I got the sum of {result}".format(opt1=x, opt2=y, result=x+y))


x = 12.3456789
print('The value of x is %3.2f' %x)