import os

ret=os.fork()   # 父进程中fork的返回值，就是刚刚创建出来的子进程的id
print(ret)
if ret>0:
    # 进程用getpid()获取当前进程的id
    print("-------父进程执行-------%d--"%os.getpid())
else:
    # 子进程用gettppid()获取父进程的id
    print("-------子进程执行-----%d--%d--"%(os.getpid(),os.getppid()))

