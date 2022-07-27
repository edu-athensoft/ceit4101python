"""
multiprocessing
process
multicore

"""

import multiprocessing as mp
import time


def job(x, y):
    print("multiprocessing job")
    time.sleep(10)

# it is necessary to place main logic into if-main-body
if __name__ == '__main__':
    # check at task manager
    # related tasks appeared when the process get started
    # after specified time=10sec, those tasks disappeared
    process1 = mp.Process(target=job, args=(1, 2))
    process1.start()
    process1.join()


