"""
multilprocessing

problem in Windows

pid -       process id
ppid -      parent process id
getpid()
getppid()

"""
import os
import time
from multiprocessing import Process, freeze_support


def foo():
    # print(f'[subprocess PID-{os.getpid()}]')
    # print(f'[subprocess PID-{os.getpid()}]running sub-process {fname}')
    print(f'[subprocess PID-{os.getpid()}]parent process id PPID {os.getppid()}')



if __name__ == "__main__":
    freeze_support()
    print(f'[main PID-{os.getpid()}]main process started')

    NUM_OF_PROCESS = 3
    for i in range(NUM_OF_PROCESS):
        # proc = Process(target=foo, args=('sproc_'+str(i),))
        proc = Process(target=foo)
        proc.start()
        # time.sleep(1)
        # proc.join()

    print(f'[main PID-{os.getpid()}]running main process')
