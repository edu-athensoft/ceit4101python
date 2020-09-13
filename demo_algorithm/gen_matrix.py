"""
monte carlo
random walk
generating a 4 x 4 matrix of (x,y)

(0,0) - (3,3)
"""

import random

mycoord = []

for x in range(4):
    for y in range(4):
        # print((x,y), end="\t")
        mycoord.append([x,y])
    # print()

# print(mycoord)

# offset
def go_west(current, wlimit=3):
    if current[0] < wlimit:
        current[0] += 1  # x = x+1
    return current

def go_east(current, elimit=0):
    if current[0] > elimit:
        current[0] -= 1
    return current

def go_south(current, slimit=3):
    if current[1] < slimit:
        current[1] += 1
    return current

def go_north(current, nlimit=0):
    if current[1] > nlimit:
        current[1] -= 1
    return current

def go(start, end):
    route = []
    # print(random.choice(nextstep))
    current = list(start)
    route.append(list(start))
    while current != end:
        nextstep = random.choice(steps)
        if nextstep == 'e':
            go_east(current, end[0]-start[0])
        if nextstep == 'w':
            go_west(current, end[0]-start[0])
        if nextstep == 's':
            go_south(current, end[1]-start[1])
        if nextstep == 'n':
            go_north(current, end[1]-start[1])

        # print(f"next step:{nextstep} ,  {current}")
        route.append(list(current))
    return route


def clean_route(orgin_route):
    rt = []
    for i in orgin_route:
        if i not in rt:
            rt.append(i)
    return rt



steps = ('e','w','s','n')
# steps = ('w','s')
start_coord = [0,0]
end_coord = [3,3]

# route
# s,s,s,w,w

# for i in range(10):
#     print(random.randint(1,6))

for i in range(10):
    rt = go(start_coord,end_coord)
# print(f"origin route={rt}")

# remove duplicated

    print(f"final route={clean_route(rt)}")

# print((1,0)==(1,0))
