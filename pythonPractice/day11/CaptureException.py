#捕获异常
"""
#coding=utf-8
try:
    print('-----test--1---')
    open('123.txt','r') # 如果123.txt文件不存在，那么会产生 IOError 异常
    print('-----test--2---')
    print(num)# 如果num变量没有定义，那么会产生 NameError 异常

except (IOError,NameError):
    #如果想通过一次except捕获到多个异常可以用一个元组的方式
"""

try:
    # 提示用户输入一个数字
    num = int(input("请输入数字："))
except:
    print("请输入正确的数字")

try:
    # 尝试执行的代码
    num=int(input("请输入一个整数："))
    result=num/8
    print(result)
except ValueError:
    # 针对错误类型，对应的代码处理
    print("请输入正确的整数")
except ZeroDivisionError:
    print("除 0 错误")
except Exception as result:
    # 打印错误信息
    print("未知错误 %s"%result)
else:
    # 没有异常才会执行的代码
    print("正常执行")
finally:
    # 无论是否有异常，都会执行的代码
    print("正常执行，但不保证正确")


