# 私有化
class Person(object):
    def __init__(self,name,age,taste):
        self.name=name      # 不带下划线的属性是公有变量
        self._age=age       # 带下划线的属性相当于java中的private，私有变量
        self.__taste=taste  # 双下划线的属性，子类不继承，也不能访问

    def show_person(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    def do_work(self):
        self._work()
        self.__away()

    def _work(self):
        print("I'm working........")

    def __away(self):
        print("I'm going away.......")

class Student(Person):
    def construction(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste

    def show_student(self):
        print(self.name)
        print(self._age)
        print(self.__taste)

    @staticmethod
    def test_bug():
        _Bug.show_bug()

#模块内可以访问，当from cur_module import *时，不导入
class _Bug(object):
    @staticmethod
    def show_bug():
        print("show bug")

s1=Student("jack",25,"football")
s1.show_person()
print("*"*20)

# s1.show_student()     # 执行出错，Student对象没有Student的私有属性__state,无法在外部直接访问
print("*"*20)

Student.test_bug()

