# apply阻塞式添加任务
"""
阻塞：必须等条件满足才能运行下一步
"""
from multiprocessing import Pool
import os,time

def worker(num):
    for i in range(5):
        print("===pid=%d,num=%d==="%(os.getpid(),num))
        time.sleep(1)

po=Pool(3)
for i in range(10):
    print("---%d---"%i)
    #向进程池中添加任务
    po.apply(worker,(i,))    # 阻塞的方式

po.close()   # 关闭进程池，相当于不能够再次添加新任务了
po.join()    # 主进程创建／添加任务后，主进程默认不会等待进程池中的任务执行完后才结束
             # 而是当主进程的任务做完之后立马结束,如果这个地方没join,会导致
             # 进程池中的任务不会执行