# 元类  类也是对象

class Person(object):
    num=0
    print("-------person----test-------")
    def __init__(self):
        self.name="abc"


print(100)
print("hello")
print("jjjjjjjjjj")
print(Person)


def print_num(self):
    print("-----num--%d----"%self.num)

# 第二个括号里写继承的类的名字
Test3=type("Test3",(),{"print_num":print_num})
t1=Test3()
t1.num=100
t1.print_num()
print("---------"*30)
class PrintNum2:
    def print_num(self):
        print("-----num--%d----"%self.num)

t2=PrintNum2()
t2.num=100
t2.print_num()


