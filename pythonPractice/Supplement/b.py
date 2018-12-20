# 循环导入a、b模块，出错
from a import a

def b():
    print("-----------b------------")

def c():
    print("-----------c------------")
    a()

c()