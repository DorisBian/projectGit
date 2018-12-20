"""
python是动态语言，在运行过程中可修改代码
"""

import types

# 1.运行过程中给对象绑定(添加)属性
class Person(object):
    num=0
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age

    def eat(self):
        print("eat food-------------")

p=Person("小明",20)
p.sex="female"
#对象p有了sex属性
print(p.sex)

# 2.运行过程中给类绑定(添加)属性
p1=Person("小李",25)
# p1.sex     #出错

Person.sex=None
p1=Person("小李",25)
print(p1.sex)       # 不出错

# 3.运行过程中给类绑定(添加)方法
def run(self,speed):
    print("%s 在移动，速度是%d km/h"%(self.name,speed))

# 定义一个类方法
@classmethod
def test_class(cls):
    cls.num=100

# 定义一个静态方法
@staticmethod
def test_static():
    print("------static method-----")


p=Person("小红",24)
p.eat()
# p.run()     出错      加import types
"""
用MethodType将方法绑定到类，并不是将这个方法直接写到类内部，而是在内存中创建一个link指向外部的方法，在创建实例的时候这个link也会被复制。
"""
# 给对象添加实例方法
p.run=types.MethodType(run,p)
# 调用实例方法
print(p.run(180))


# 给Person类绑定类方法
Person.test_class=test_class
# 调用类方法
print(Person.num)
Person.test_class()
print(Person.num)

# 给Person类绑定静态方法
Person.test_static=test_static
# 调用静态方法
print(Person.test_static)

"""避免动态坑，可用__slots__方法"""




