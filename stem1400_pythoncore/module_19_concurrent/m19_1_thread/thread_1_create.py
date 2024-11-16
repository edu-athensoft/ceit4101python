"""
Creating thread with Thread class

调用 Thread 类的构造器创建线程很简单，直接调用 threading.Thread 类的如下构造器创建线程：
__init__(self, group=None, target=None, name=None, args=(), kwargs=None, *,daemon=None)

通过 Thread 类的构造器创建井启动多线程的步骤如下：
调用 Thread 类的构造器创建线程对象。在创建线程对象时，target 参数指定的函数将作为线程执行体。
调用线程对象的 start() 方法启动该线程。
"""

import threading

# 定义一个普通的action函数，该函数准备作为线程执行体
def action(_max):
    for i in range(_max):
        # 调用threading模块current_thread()函数获取当前线程
        # 线程对象的getName()方法获取当前线程的名字
        print(threading.current_thread().getName() +  " " + str(i))

# main
for i in range(25):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() +  " " + str(i))

    if i == 5:
        # create and start 1st thread
        t1 =threading.Thread(target=action, args=(30,))
        t1.start()

        # create and start 2nd thread
        t2 =threading.Thread(target=action, args=(30,))
        t2.start()
print('main thread execution done.')



