# 第三种创建子进程的方式：进程池
"""
如果需要创建的子进程数目较多，则进程池比较合适
刚开始就创建多个进程，用的时候分配给它，不用的时候再把进程还给进程池
特点：可以完成多任务
"""
from multiprocessing import Pool
import os,time

def worker(num):
    for i in range(5):
        print("===pid=%d,num=%d==="%(os.getpid(),num))
        time.sleep(1)

#3表示 进程池中最多有3个进程一起执行
po=Pool(3)
for i in range(10):
    print("---%d---"%i)
    #向进程池中添加任务
    """
    注意：如果添加的任务数量超过了进程池中进程的个数的话，那么不会导致添加不进去
    添加到进程中的任务如果还没有被执行的话，那么此时他们会等待进程池中的进程完成一个任务之后，
    会自动的去用刚刚的那个进程完成当前的新任务
    """
    po.apply_async(worker,(i,))

po.close()   # 关闭进程池，相当于不能够再次添加新任务了
po.join()    # 主进程创建／添加任务后，主进程默认不会等待进程池中的任务执行完后才结束
             # 而是当主进程的任务做完之后立马结束,如果这个地方没join,会导致
             # 进程池中的任务不会执行
"""
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
调用close()之后就不能继续添加新的Process了。
"""




