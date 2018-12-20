# 生成器----多任务（多任务三种模式：协程、进程、线程，本例协程）

def test1():
    while True:
        print("------1-------")
        yield None

def test2():
    while True:
        print("------2-------")
        yield None

t1=test1()
t2=test2()
while True:
    print(t1.__next__())
    print(t2.__next__())