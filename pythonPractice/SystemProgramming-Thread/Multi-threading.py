# 多线程：用来完成多任务
# 使用线程的方法一
import threading
import time

def say_sorry():
    print("亲爱的，我错了，我可以吃饭了吗")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t=threading.Thread(target=say_sorry)
        t.start()   # 启动线程
