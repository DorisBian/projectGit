# 异步
from multiprocessing import Pool
import time
import os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d---"%(os.getpid(),os.getppid()))
    for i in range(3):  #循环三次打印，每次延时一秒，共用3秒
        print("---%d----"%i)
        time.sleep(1)
    return "haha"
# 线程执行完毕，一个线程的生命周期结束，此线程dead，操作系统告知主进程，主进程执行callback,callback回调test2

def test2(args):
    # 当前所获得的id是主进程id，说明主线程执行了test2方法
    print("---callback func-pid=%d"%os.getpid())
    print("---callback func-args=%s"%args)

# 创建进程池，进程池里有三个线程
pool=Pool(3)
pool.apply_async(func=test,callback=test2)

# 异步的理解：主进程正在做某件事情，突然来了一件更需要立刻去做的事情，
# 那么这种，在父进程去做某件事情的时候，并不知道是什么时候去做另外一件事的模式，就称为异步
# ajax:
while True:
    # 主线程睡1秒执行print
    time.sleep(1)
    print("----主进程-pid=%d----"%os.getpid())       # getpid()：查看当前进程
