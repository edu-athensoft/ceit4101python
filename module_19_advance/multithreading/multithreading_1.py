import threading
import time


def print_hello_three_times():
    for i in range(10):
        time.sleep(0.2)
        print("Hello")



def print_hi_three_times():
    for i in range(10):
        time.sleep(0.4)
        print("Hi")



t1 = threading.Thread(target=print_hello_three_times)
t2 = threading.Thread(target=print_hi_three_times)

t1.start()
t2.start()

