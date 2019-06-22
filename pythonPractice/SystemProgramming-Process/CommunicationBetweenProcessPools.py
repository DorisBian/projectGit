# 进程池中的进程如何通信：

# 修改import中的Queue为Manager
from multiprocessing import Manager,Pool
import os,time,random

# 写数据进程执行的代码
def writer(q):
    print("writter启动(%s),父进程为%s"%(os.getpid(),os.getppid()))
    for i in "Doris":
        q.put(i)

# 读数据进程执行的代码
def reader(q):
    print("reader启动(%s),父进程为%s"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))

if __name__=="__main__":
    print("(%s)start"%os.getpid())
    # 父进程创建Queue，并传递给各个子进程
    q=Manager().Queue()
    po=Pool()
    # 使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writter完全执行完成后，再用reader
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) end"%os.getpid())




