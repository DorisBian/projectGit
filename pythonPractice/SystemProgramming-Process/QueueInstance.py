# Queue实例：在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import Queue,Process
import os,time,random

# 写数据进程执行的代码
def write(q):
    for value in ["A","B","C"]:
        print("put %s into Queue"%value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    while True:
        if not q.empty():
            value=q.get(True)
            print("get %s from Queue"%value)
            time.sleep(random.random())
        else:
            break

if __name__=="__main__":
    # 父进程创建Queue，并传递给各个子进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    # 启动子进程pw,写入
    pw.start()
    # 等待pw结束
    pw.join()
    # 启动子进程pr,读取
    pr.start()
    pr.join()
    # pr进程里的是死循环，无法等待其结束，只能强行终止
    print("")
    print("所有数据都写入并且读完")
