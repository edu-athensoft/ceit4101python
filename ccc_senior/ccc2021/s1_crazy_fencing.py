"""
Problem S1. Crazy fencing
"""


N = -1
N_MAX = 10000

# input N
while(True):
    strprompt = 'input N (1<N<='+str(N_MAX)+'):'
    N = int(input(strprompt))
    if N <1 or N >N_MAX:
        print("N does not make any sense, input again please!")
        continue
    else:
        # print(N)
        break

# input sides
h_rawinput = input('input '+str(N+1)+' num of side height:\n')
h_list = h_rawinput.split()
print(h_list)

# input widths
w_rawinput = input('input '+str(N)+' num of width:\n')
w_list = w_rawinput.split()
print(w_list)

# process
def shape_area(left_h, right_h, width):
    return (left_h+right_h)*width/2

total_area = 0

for i in range(N):
    left_h = int(h_list[i])
    right_h = int(h_list[i+1])
    width = int(w_list[i])
    total_area += shape_area(left_h,right_h,width)

print(total_area)

