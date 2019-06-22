# 主线程会等待所有的子线程结束后才结束

import threading
import time

def sing():
    for i in range(3):
        print("正在唱歌------%d"%i)
        time.sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞------%d"%i)
        time.sleep(1)

if __name__ == '__main__':
    print("------开始-----:%s"%time.ctime())

    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        length=len(threading.enumerate())
        print("当前运行的线程数为：%s"%length)
        if length<=1:
            break
        time.sleep(0.5)

    # time.sleep(5)
    print("------结束-----:%s"%time.ctime())




