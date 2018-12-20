# 垃圾回收GC
"""
小整数对象池，避免为整数频繁申请和销毁空间，小整数：[-5,257)，不会被垃圾回收
引用计数机制
一个对象引用计数为0时会被删除销毁
引用计数是Python垃圾回收的主要机制，但无法解决两个对象相互引用、占用对方内存空间的问题
下例为引用计数无法解决的示例

另一种方法，隔代回收：generationZero可以解决引用计数无法解决的问题，需要三条链，第零代，第一代，第二代
核心思想：变量在没有引用的情况下计数不为0，此时将计数都减一，看是否为0，为0则表示是垃圾
Python垃圾回收机制：引用计数为主，隔代回收为辅。标记清除是ruby的回收机制
"""
# gc模块
import gc

class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(hex(id(self))))

def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        gc.collect()

gc.disable()

f2()



