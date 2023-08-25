"""
multilprocessing

pid -       process id
ppid -      parent process id
getpid()
getppid()

"""
import os
import time
from multiprocessing import Process


def foo(fname):
    # print(f'[subprocess PID-{os.getpid()}]')
    # print(f'[subprocess PID-{os.getpid()}]running sub-process {fname}')
    print(f'[subprocess PID-{os.getpid()}]parent process id PPID {os.getppid()}')
    return fname;


if __name__ == "__main__":
    print(f'[main PID-{os.getpid()}]main process started')
    print(f'[main PID-{os.getpid()}]parent process id PPID {os.getppid()}')

    NUM_OF_PROCESS = 3
    for i in range(NUM_OF_PROCESS):
        proc1 = Process(target=foo, args=('sproc_'+str(i),))
        proc1.start()
        # time.sleep(1)

    print(f'[main PID-{os.getpid()}]running main process')
