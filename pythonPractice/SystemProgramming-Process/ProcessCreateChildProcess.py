# 第一种创建子进程的方式：process创建的子进程和主进程的结束，不建议用fork创建，不能跨平台
from multiprocessing import Process
import time

def test():
    for i in range(5):
        print("------test--------")
        time.sleep(1)

p=Process(target=test)
p.start()      # 让这个进程开始执行test函数里的代码

# Process创建的进程，主进程必须等子进程们都结束，它才结束