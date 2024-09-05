"""
multiprocessing
process
multicore
queue

"""

import multiprocessing as mp
import time


def job(x, y):
    print("multiprocessing job")
    result = 0
    for i in range(5):
        result += x**i + y**i
    print(result)
    time.sleep(1)


# it is necessary to place main logic into if-main-body
if __name__ == '__main__':
    process1 = mp.Process(target=job, args=(1, 2))
    process2 = mp.Process(target=job, args=(3, 4))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


