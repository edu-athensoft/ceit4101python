"""
Create thread by extending Thread class

通过继承 Thread 类来创建并启动线程的步骤如下：
定义 Thread 类的子类，并重写该类的 run() 方法。
run() 方法的方法体就代表了线程需要完成的任务，因此把 run() 方法称为线程执行体。
创建 Thread 子类的实例，即创建线程对象。
调用线程对象的 start() 方法来启动线程。
"""

import threading

class FkThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0

    # 重写run()方法作为线程执行体
    def run(self):
        while self.i < 30:
            # 调用threading模块current_thread()函数获取当前线程
            # 线程对象的getName()方法获取当前线程的名字
            print(threading.current_thread().getName() +  " " + str(self.i))
            self.i += 1


# main thread
for i in range(100):
    # 调用threading模块current_thread()函数获取当前线程
    print(threading.current_thread().getName() +  " " + str(i))

    if i == 20:
        # create and run the 1st thread
        ft1 = FkThread()
        ft1.start()

        # create and run the 2nd thread
        ft2 = FkThread()
        ft2.start()
print('Main-thread done.')

