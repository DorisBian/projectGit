#多继承：子类可以拥有多个父类，并且具有所有父类的属性和方法
# 定义一个父类
class A:
    def printA(self):
        print('----A----')

# 定义一个父类
class B:
    def printB(self):
        print('----B----')

# 定义一个子类，继承自A、B
class C(A,B):
    def printC(self):
        print('----C----')

obj_C = C()
obj_C.printA()
obj_C.printB()

# 开发时，如果父类之间存在同名的属性或者方法，应尽量避免使用多继承
