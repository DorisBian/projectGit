# 装饰器
"""
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。

"""
# 闭包
def w1(func):
    def inner():
        print("------正在验证--------")
        if True:
            func()
        else:
            print("没有权限")
    return inner

# @w1相当于f1=w1(f1)
@w1
def f1():
    print("------f1------")
@w1
def f2():
    print("------f2------")

# inner_funct=w1(f1)
# inner_funct()
# 原本调用的是f1()，为了不修改原来已完成的代码，不能用inner_funct变量

# f1=w1(f1)    此行代码也能化简
f1()
f2()