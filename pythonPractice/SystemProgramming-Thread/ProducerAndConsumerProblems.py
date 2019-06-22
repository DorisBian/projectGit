# 生产者与消费者模式问题
"""
目的：解决数据生产方和数据处理方速度不匹配的问题
当速度不匹配时，为了解决这个问题，在中间架设管道(缓冲)，生产的数据往缓冲区里放
耦合：耦合性越强，程序越不好
如果多个线程中有多任务要做，并且速度不一样，往往采用队列(相当于缓冲区，用于给生产者消费者解耦解耦)
"""
# 此队列Queue是线程中用的，非进程中用的
from queue import Queue
import threading
import time

# 如果当前队列里商品个数小于1000，有2个线程，每人每次生产100个扔进队列，延时0.5秒，
class Producer(threading.Thread):
    def run(self):
        global queue
        count=0
        while True:
            if queue.qsize()<1000:       # qsize()判断队列中是否还有数据
                for i in range(100):
                    count=count+1
                    msg="生成产品"+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

# 只要当前队列里商品数量大于100，那么有五个线程，每人每次获取3个，延时1秒
class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize()>100:
                for i in range(3):
                    msg=self.name+"消费了"+queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue=Queue()

    for i in range(500):
        queue.put("初始产品"+str(i))

    for i in range(2):
        # 创建2个Producer线程
        p=Producer()
        p.start()

    for i in range(5):
        # 创建5个Consumer线程
        c=Consumer()
        c.start()
