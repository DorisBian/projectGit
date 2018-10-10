#局部变量和全局变量
#当函数内出现局部变量和全局变量相同名字时，函数内部中的 变量名 = 数据 此时理解为定义了一个局部变量，而不是修改全局变量的值。
a=200     #全局变量
def test1():
    a=300   #局部变量
    print("修改前----a=%d"%a)
    a=200
    print("修改后----a=%d"%a)

def test2():
    print("test2-----a=%d"%a)

test1()
test2()

"""
如何对全局变量进行修改
如果在函数中出现global 全局变量的名字 那么这个函数中即使出现和全局变量名相同的变量名 = 数据 也理解为对全局变量进行修改，而不是定义局部变量
可以使用一次global对多个全局变量进行声明
global a, b
还可以用多次global声明都是可以的
global a
global b
"""
#修改全局变量
print("-----------------------"*20)
a=100     #全局变量
def test1():
    global a
    print("修改前----a=%d"%a)
    a=200
    print("修改后----a=%d"%a)

def test2():
    print("test2-----a=%d"%a)

test1()
test2()
