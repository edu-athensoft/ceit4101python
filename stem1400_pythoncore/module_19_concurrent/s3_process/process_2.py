"""
multil-process
"""
import time
from multiprocessing import Process


def foo(fname):
    print(f'[subprocess-1]received {fname}')
    print(f'[subprocess-1]running sub-process #1')
    print()


def foo2(fname, age):
    print(f'[subprocess-1]received {fname}, {age}')
    print(f'[subprocess-1]running sub-process #2')
    print()


if __name__ == "__main__":
    print('[main]main process started\n')

    print('[main]running main process')
    proc1 = Process(target=foo, args=('sub-process_name',))
    proc1.start()
    time.sleep(2)

    print('[main]running main process')
    proc2 = Process(target=foo2, args=('sub-process_name_2', 20))
    proc2.start()
    time.sleep(2)

    print('[main]running main process')
