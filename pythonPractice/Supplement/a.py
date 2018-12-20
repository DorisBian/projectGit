# 循环导入
from b import b

def a():
    print("-----------1------------")
    b()

a()
