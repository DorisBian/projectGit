# Process创建子进程
# multiProcessing模块是跨平台版本的多进程模块
from multiprocessing import Process
import time

def test():
    while True:
        print("------test--------")
        time.sleep(1)

p=Process(target=test)     # Process创建了一个对象p，p就可以当做一个进程来看待，target指向这个进程对象要执行的对象名称
p.start()      # 让这个进程开始执行test函数里的代码

while True:
    print("------main-------")
    time.sleep(1)