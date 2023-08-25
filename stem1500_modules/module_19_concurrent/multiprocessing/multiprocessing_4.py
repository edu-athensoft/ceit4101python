"""
multiprocessing
process
process class
"""

import multiprocessing as mp
import time


class ClockProcess(mp.Process):
    def __init__(self, interval):
        mp.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1


if __name__ == '__main__':
    p = ClockProcess(2)
    p.start()