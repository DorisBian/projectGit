"""
函数定义：
def 函数名():
    函数内部代码
"""
def print_fo_zu():
        print("佛祖镇楼                                 Bug辟易")
        print("佛祖镇楼                                 Bug辟易")
        print("佛祖镇楼                                 Bug辟易")

print("我们的系统开始运行了")
print_fo_zu()
print("欢迎使用我们的系统")
print_fo_zu()
print("我们的系统倒闭了")

#计算两个数之和
def sum1():
    """可以计算两个数字之和"""        #定义文档说明
    a=100
    b=200
    c=a+b
    print(c)
sum1()
help(sum1)

#带参函数，函数传参
def sum2(a,b):
    """可以计算两个数字之和"""        #定义文档说明
    c=a+b
    return c
result=sum2(100,475)
print(result)
#返回值的另一种使用
print(sum2(73,10))

def sum3(a,b):
    """可以计算两个数字之和"""        #定义文档说明
    c=a+b
    return c      #当函数执行到return会立即终止函数的运行，并返回到调用的地方，只有第一个return被执行了
    print("----------1----------")
    return 55
#如果函数没有返回值，变量接收none，表示没有返回数据
print(sum3(73,10))





