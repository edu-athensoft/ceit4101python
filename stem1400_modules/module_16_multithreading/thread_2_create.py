"""
create threads with threading.Thread
in OO style
"""

import threading
import time

# exit_flag = 0

class MyThread(threading.Thread):
    def __init__(self, thread_id, name, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting thread...")
        task(self.name, self.delay, 5)
        print("Exited thread")


def task(thread_name, delay, counter):
    while counter:
        # if exit_flag:
        #     thread_name.exit()
        time.sleep(delay)
        print(f"{thread_name}, {time.ctime(time.time())}")
        counter -= 1


# main
print("Starting program...")
t1 = MyThread(1, "thread-1", 3)
t2 = MyThread(2, "thread-2", 4)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done.")


