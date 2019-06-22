# Join子进程
"""
join：主进程阻塞，等待子进程的退出，必须在close()或terminate()之后使用
"""
from multiprocessing import Process
import time
import random

def test():
    for i in range(random.randint(1,5)):
        print("------%s--------"%i)
        time.sleep(1)

p=Process(target=test)
p.start()
# p.join()     # 等到对象标记的子进程test执行结束之后才往下走
p.join(1)      # 等待的最长时间是1秒，若1秒内test未执行结束，主进程继续往下走，不等子进程结束
print("-----------main-------------")
