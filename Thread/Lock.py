# 如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
# 使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。如下：
# 多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。
# 一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。
# 那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。
# 锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。
# 经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。
import threading
import time
data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
class setThread(threading.Thread):

    def __init__(self,threadname):
        threading.Thread.__init__(self)
        self.threadname = threadname

    def run(self):
    #    threadLock.acquire()
        set_data()
    #    threadLock.release()

class printThread(threading.Thread):

    def __init__(self,threadname):
        threading.Thread.__init__(self)
        self.threadname = threadname

    def run(self):
     #   threadLock.acquire()
        print_data()
    #    threadLock.release()

threadLock = threading.Lock()

def print_data():
    for index in range(len(data)):
        time.sleep(1)
        print("data:",data[index])

def set_data():
    for index in range(len(data)):
        time.sleep(1)
        print("set data 1")
        data[index] = 1;

threadSet = setThread("Thread-1")
threadPrint = printThread("Thread-2")

threadPrint.start()
threadSet.start()

