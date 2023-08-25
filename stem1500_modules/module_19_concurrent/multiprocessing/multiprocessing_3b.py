"""
multiprocessing
process
multicore
queue
transfer data, output from a process
"""

import multiprocessing as mp
import os
import time


def job(name):
    print("multiprocessing job", name, 'pid:', os.getpid())
    result = 0
    for i in range(1000):
        result += i + i**2
    # q.put(result)
    # time.sleep(1)


# it is necessary to place main logic into if-main-body
if __name__ == '__main__':
    process1 = mp.Process(target=job, args=('process-1',))
    process2 = mp.Process(target=job, args=('process-2',))

    process1.start()
    process2.start()

    print("The number of CPU is:" + str(mp.cpu_count()))
    for p in mp.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))

    process1.join()
    process2.join()
