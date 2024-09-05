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
# import random


def long_time_task(name):
    print('Run task {} ({})...'.format(name, os.getpid()))
    start = time.time()
    time.sleep(1)
    end = time.time()
    print('Task {} runs {:0.2f} seconds.'.format(name, (end - start)))


if __name__=='__main__':
    print('Parent process {}'.format(os.getpid()))
    p = mp.Pool(7)
    for i in range(7):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
