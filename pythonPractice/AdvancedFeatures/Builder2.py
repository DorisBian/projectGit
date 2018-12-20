# 生成器   Fibonacci数列
"""
变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
在循环过程中不断调用yield，就会不断中断。
把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
"""

def creat_num():
    print("-----------start------------")
    a,b=0,1
    for i in range(5):
        print("---------1---------")
        # 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
        yield b         # 加上yield函数，就变成了生成器
        print("---------2---------")
        a,b=b,a+b
        print("---------3---------")
    print("-----------stop------------")

# 创建一个生成器对象
a=creat_num()

# print(next(a))
# print(a.__next__())   # 只要创建了对象，这种方式也可以打印下一个值


for num in a:
    print(num)

