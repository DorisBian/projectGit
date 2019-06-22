"""
进程、线程的同步：协同步调，按预定的先后次序进行运行。比如：你说完，我再说。
互斥锁：使用互斥锁的效率比轮询效率要高很多
加锁的代码行尽量少，可以放在for循环里面，把必须要加锁的东西加锁，加的越少多任务越明显
等待开锁的方式：通知
"""

from threading import Thread,Lock

g_num = 0

def test1():
    global g_num
    """
    这个线程和test2线程都在抢着对这个锁进行上锁，如果有一方成功上锁，那么导致另外
    一方会堵塞（一直等待）到这个锁被解开为止
    """
    mutex.acquire()   # 上锁
    for i in range(1000000):
        g_num += 1
    mutex.release()    # 解锁，用来对mutex指向的这个锁进行解锁，只要开了锁，那么接下来会让所有因为
                       # 这个锁被上了锁而堵塞的线程，进行抢着上锁

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num

    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()

    print("---test2---g_num=%d"%g_num)

# 创建一把互斥锁，这个锁默认是没有上锁的
mutex=Lock()

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)