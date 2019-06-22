# 多线程使用非全局变量
# 非全局变量不需要加锁
from threading import Thread
import threading
import time

def test1():
    name=threading.current_thread().name
    print("the threading name is %s------"%name)
    g_num=100
    if name=="Thread-1":
        g_num += 1
    print("---test1---g_num=%d"%g_num)
    time.sleep(2)
    print("---the thread is %s---g_num=%d"%(name,g_num))
#
# def test2():
#     time.sleep(1)
#     g_num = 100
#     print("---test2---g_num=%d"%g_num)

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test1)
p2.start()