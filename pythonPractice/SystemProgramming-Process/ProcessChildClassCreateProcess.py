# 第二种创建子进程的方式：Process子类创建进程
# 将复杂的任务放入一个类中实现
from multiprocessing import Process
import time

class MyNewProcess(Process):
    # 重写了Process类的run方法
    def run(self):
        while True:
            print("-----------1-----------")
            time.sleep(1)


p=MyNewProcess()
p.start()       # start()内部一定会调用重写后的run方法

while True:
    print("--------main--------")
    time.sleep(1)