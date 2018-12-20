# 动态创建类
"""
类也是对象
"""
def choose_class(name):
    if name=="foo":
        class Foo(object):
            pass
        return Foo     # 返回的是类，不是类的实例
    else:
        class Bar(object):
            pass
        return Bar

MyClass =choose_class("foo")
print(MyClass)    # 函数返回的是类，不是类的实例
print(MyClass())   # 可以通过这个类创建类实例，也就是对象
"""
使用type动态创建类
语法：type(类名，由父类名称组成的元祖(可以为空)，包含属性的字典(名称和值))
"""

class Test():
    pass

print(Test())

Test2=type("Test2",(),{})
print(Test2())

MyDogClass=type("MyDog",(),{})
print(MyDogClass)

help(Test)
help(Test2)

"""
type接受一个字典来为类定义属性
"""
Foo=type("Foo",(),{"bar":True})
print(Foo)
print(Foo.bar)
f=Foo()
print(f)
print(f.bar)

# 可以继承
class FooChild(Foo):
    # 用type创建带有方法的类
    def echo_bar(self):
        print(self.bar)

    # 添加静态方法
    @staticmethod
    def test_static():
        print("-------static method--------------------------")



FooChild=type("FooChild",(Foo,),{"echo_bar":"echo_bar"})
print(FooChild)
print(FooChild.bar)       # bar属性是继承来的
print("---------------------------------分割线-----------------------------------")
print(hasattr(Foo,"echo_bar"))      # 父类没有
print(hasattr(FooChild,"echo_bar"))   # 子类有


"""
FooChild=type("FooChild",(Foo,),{"echo_bar":"echo_bar","test_static":"test_static"})
foochild=FooChild()
print(foochild.test_static)
print(foochild.test_static())
"""

