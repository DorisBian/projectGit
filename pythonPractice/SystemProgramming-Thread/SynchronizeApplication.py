# 同步的应用
"""
堵塞和非堵塞
确定执行的顺序，则为同步；不确定执行的顺序，则为异步；
本例中：通过多个互斥锁完成了多个线程并且有序执行，它就是同步(只要保证有规律执行即可)
"""
from threading import Thread,Lock
from time import sleep

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("------Task 1 -----")
                sleep(0.5)
                lock2.release()     # lock2解锁

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("------Task 2 -----")
                sleep(0.5)
                lock3.release()    # lock3解锁

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("------Task 3 -----")
                sleep(0.5)
                lock1.release()   # lock1解锁

#使用Lock创建出的锁默认没有“锁上”
lock1 = Lock()
#创建另外一把锁，并且“锁上”
lock2 = Lock()
lock2.acquire()
#创建另外一把锁，并且“锁上”
lock3 = Lock()
lock3.acquire()

# 3个线程
t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()

