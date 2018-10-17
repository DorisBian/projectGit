#多层继承

class Animal:
    def eat(self):
        print("-----吃-----")

    def drink(self):
        print("-----喝-----")

class Dog(Animal):
    def bark(self):
        print("-----汪汪叫------")

class xiao_tian_quan(Dog):
    """定义了一个哮天犬类,继承Dog类"""
    """
    重写(override)父类方法:当父类的方法实现不能满足子类需求时，可以对方法进行重写
    重写有两种情况：覆盖和扩展
    调用父类的方法：super().方法或者父类名.方法(self)，后者不推荐使用
    """
    #扩展
    def bark(self):
        #1.针对子类中特有的需求，编写代码
        print("--------神一样的叫唤----------")

        #2.使用super()，调用原本在父类中封装的方法
        # super是特殊类，父类名和super()两种方式不要混用
        #Dog.bark(self)   #括号里的self参数要带上，python2.7使用的    此行和下一行代码相同，但不推荐用这种写法
        super().bark()
        # 如果使用当前子类名调用方法，会形成递归调用，出现死循环
        #xiao_tian_quan.bark(self)     #递归调用

        #3.增加其他子类的代码，扩展
        print("-----嗷嗷叫------")

class Cat(Animal):
    def catch(self):
        print("----捉老鼠----")

xtq=xiao_tian_quan()
xtq.drink()
xtq.eat()
xtq.bark()
print("---------------------分割线-------------------------")

