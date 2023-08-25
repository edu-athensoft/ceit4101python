"""
multithreading
thread

"""

import threading as td
import time


def job(x,y):
    print("threading job")


t1 = td.Thread(target=job, args=(1,2))
t1.start()
t1.join()

