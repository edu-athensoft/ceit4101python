"""
a+b+c=1000
a^2+b^2=c^2

how many groups of (a,b,c) make them true at the same time?

analysis:
c = 1000-a-b
a>0, b>0, c>0

"""
import time



def process():
    nums = []
    start_time = time.time()
    SUM = 1000
    for a in range(0,SUM-1):
        for b in range(0,SUM-a):
            c = 1000-a-b
            if a**2+b**2==c**2 :
                # print(a,b,c)
                nums.append((a,b,c))

    end_time = time.time()
    print(f'time escaped : {end_time - start_time}, {nums}')


for i in range(50):
    process()