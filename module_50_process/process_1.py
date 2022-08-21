"""
multil-process
"""
import time
from multiprocessing import Process


def foo(fname):
    print(f'[subprocess-1]received {fname}')
    print(f'[subprocess-1]running sub-process #1')


if __name__ == "__main__":
    print('[main]main process started')
    proc1 = Process(target=foo, args=('sub-process_name',))
    proc1.start()
    time.sleep(2)

    print('[main]running main process')
