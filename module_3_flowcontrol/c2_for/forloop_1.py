# for loop

# case 1 - print out a list

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
round 1:    fetch 0 from my_list
            print out
round 2:    fetch 1 from my_list
            print out
round 3:    fetch 2 from my_list
            print out
...
round 10:   fetch 9 from my_list
            print out
'''

'''
round 1:    fetch my_list[0]
            print out
round 2:    fetch my_list[1]
            print out
round 3:    fetch my_list[2]
            print out
...
round 10:   fetch my_list[9]
            print out
'''

'''
round 0:    fetch my_list[0]
            print out
round 1:    fetch my_list[1]
            print out
round 2:    fetch my_list[2]
            print out
...
round 9:   fetch my_list[9]
            print out
'''

'''
i  => index

round i:    fetch my_list[i]
            print out

i = 0..9
'''

for item in my_list:
    print(item)

