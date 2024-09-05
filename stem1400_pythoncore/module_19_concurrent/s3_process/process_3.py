"""
multil-process
"""
import time
from multiprocessing import Process


def foo(fname):
    print(f'[subprocess-1]received {fname}')
    print(f'[subprocess-1]running sub-process {fname}')


if __name__ == "__main__":
    print('[main]main process started')

    NUM_OF_PROCESS = 5
    for i in range(NUM_OF_PROCESS):
        proc1 = Process(target=foo, args=('sproc_'+str(i),))
        proc1.start()
        time.sleep(1)

    print('[main]running main process')
