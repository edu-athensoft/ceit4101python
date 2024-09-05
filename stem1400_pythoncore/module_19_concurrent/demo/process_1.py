"""
process
"""

from multiprocessing import Process
import os
import time


def calculate():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()
    print(f"Number of processes: {num_processes}")

    # Create and start processes
    for i in range(num_processes):
        p = Process(target=calculate)
        processes.append(p)
        p.start()

    # Join processes
    for p in processes:
        p.join()

    print('end main')