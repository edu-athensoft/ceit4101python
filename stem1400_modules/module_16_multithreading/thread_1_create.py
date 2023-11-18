"""
creating threads with threading
"""

import threading
import time


def task1():
    thread_name = 'ThreadName-1'
    duration = 3
    count = 0
    while count < 3:
        time.sleep(duration)
        count += 1
        print(f"{thread_name}, {time.ctime(time.time())}")

def task2():
    thread_name = 'ThreadName-2'
    duration = 2
    count = 0
    while count < 3:
        time.sleep(duration)
        count += 1
        print(f"{thread_name}, {time.ctime(time.time())}")

try:
    print("Starting main")

    # create threads
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    # start threads
    t1.start()
    t2.start()

    # wait threads to stop
    t1.join()
    t2.join()

    print("Done.")


except:
    print("[Error] Cannot start a thread!")


"""
def task3(thread_name, duration):
    count = 0
    while count < 5:
        time.sleep(duration)
        count += 1
        print(f"{thread_name}, {time.ctime(time.time())}")
"""

