"""
thread
"""

from threading import Thread, Lock
import time

database_value = 0
lock = Lock()

def increase():
    global database_value

    with lock:  # acquire the lock
        local_copy = database_value
        local_copy += 1
        time.sleep(0.3)
        database_value = local_copy  # write back the new value

if __name__ == "__main__":
    print('Start value: ', database_value)

    threads = []

    for _ in range(10):
        t = Thread(target=increase)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('End value:', database_value)
    print('end main')
