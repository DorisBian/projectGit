# 死锁示例，程序设计时要尽量避免死锁(银行家算法)
# 避免死锁还可以通过添加超时时间timeout进行处理，即在本例中if mutexB.acquire(2): if mutexA.acquire(2):超时2秒重新运行程序
import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire(2):     # A上锁
            print(self.name+"----do1----up----")
            time.sleep(1)

            if mutexB.acquire():     # A一直等待B释放锁
                print(self.name + "----do1----down----")
                mutexB.release()
            mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire(2):    # B上锁
            print(self.name+"----do2----up----")
            time.sleep(1)

            if mutexA.acquire():     # B一直等待A释放锁，形成僵局
                print(self.name + "----do2----down----")
                mutexA.release()
            mutexB.release()

mutexA=threading.Lock()
mutexB=threading.Lock()

if __name__ == '__main__':
    t1=MyThread1()
    t2=MyThread2()

    t1.start()
    t2.start()