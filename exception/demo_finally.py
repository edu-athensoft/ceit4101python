# exception handling

"""finally"""

'''
file = open('myfile.txt','r')

for line in file:
    print(line)

file.close()
'''


try:
    file = open('myfile.txt', 'r')

    for line in file:
        print(line)

    # raise ZeroDivisionError

except:
    print('error occured')

finally:
    file.close()
