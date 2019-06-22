# 使用线程的方法二:定义子类，继承threading.Thread，重写run方法
# 线程的启动顺序，run函数中每次循环的执行顺序不能确定
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg="I'm "+self.name+" @ "+str(i)      # name属性中保存的是当前线程的名字
            print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()



