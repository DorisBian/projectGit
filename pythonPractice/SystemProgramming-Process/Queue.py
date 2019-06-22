# 进程间通信
"""
进程间通信方式之一：队列Queue
可以使用multiProcessing模块的Queue实现多进程间的数据传递
"""
from multiprocessing import Queue

q=Queue(3)      # 初始化一个Queue对象，最多可接首三条put消息
q.put("消息1")      # 将消息值写入队列
print(q.full())   # 若队列满了，返回True，否则，返回alse
q.put("消息2")
q.put("消息3")
print(q.full())

# 因为消息队列已满，下面的try都会抛出异常，第一个try会等待两秒后抛出异常
try:
    q.put("消息4",True,2)
except:
    print("消息队列已满，现有消息数量：%s"%q.qsize())

try:
    q.put("消息5")
except:
    print("消息队列已满，现有消息数量：%s"%q.qsize())

# 推荐的方式：先判断消息队列是否写满，再写入
if not q.full():
    q.put_nowait("消息4")
# 读取队列时，先判断消息队列是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
