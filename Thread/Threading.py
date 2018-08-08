import _thread
import time
import threading
#
# def print_time(threadName,delay):
#     count = 0;
#     while count < 5:
#         time.sleep(delay)
#         count += 1;
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#
# try:
#     _thread.start_new(print_time,("Thread-1",2,))
#     _thread.start_new(print_time("Thread-2",4))
# except:
#     print("error")
#
# while 1:
#     pass


# Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。
# _thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
# threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 主线程中，创建了子线程B，并且在主线程A中调用了B.join()，那么，主线程A会在调用的地方等待，
# 直到子线程B完成操作后，才接着往下执行。参数time代表线程运行最大时间，即如果超过这个时间，不管这个此线程有
# 没有执行完毕都会被回收，然后主线程或函数都会接着执行的。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。

exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, 2,self.counter)
        print ("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        # if exitFlag:
        #     threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = MyThread(1, "Thread-1", 5)
thread2 = MyThread(2, "Thread-2", 5)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")
