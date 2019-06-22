# 使用fork可以在Python程序中创建子进程，fork()在Windows系统中没有
import os
import time

ret=os.fork()
if ret==0:
    while True:
        print("-------1-------")
        time.sleep(1)
else:
    while True:
        print("-------2-------")
        time.sleep(1)