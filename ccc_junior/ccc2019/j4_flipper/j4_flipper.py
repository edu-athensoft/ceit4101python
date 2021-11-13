"""
CCC 2019 Junior
Problem J4. Flipper

status:
AC

Resources: 0.548s, 11.14 MB
Maximum runtime on single test case: 0.037s
Final score: 15/15 (3.0/3 points)

Key points
count out how many H in the sequence
count out how many V in the sequence
"""

# flip_str = 'VVHH'
# flip_str = 'HV'

flip_str = input()

num_v = flip_str.count('V')
num_h = flip_str.count('H')
# print(num_h, num_v)

flip_v = num_v % 2
flip_h = num_h % 2

a11 = 1
a12 = 2
a21 = 3
a22 = 4

def swap_h():
    global a11,a21
    tmp = a11
    a11 = a21
    a21 = tmp

    global a12,a22
    tmp = a12
    a12 = a22
    a22 = tmp

def swap_v():
    global a11,a12
    tmp = a11
    a11 = a12
    a12 = tmp

    global a21,a22
    tmp = a21
    a21 = a22
    a22 = tmp

if flip_h > 0:
    swap_h()
if flip_v > 0:
    swap_v()

print(a11,a12)
print(a21,a22)






