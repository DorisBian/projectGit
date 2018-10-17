#单继承
class Animal:
    def eat(self):
        print("-----吃-----")

    def drink(self):
        print("-----喝-----")

class Dog(Animal):
    """
    父类有的方法不用重复写了，子类拥有父类的所有方法
    """
    def bark(self):
        print("-----汪汪叫------")


class Cat(Animal):
    def catch(self):
        print("----捉老鼠----")

wang_cai=Dog()
wang_cai.eat()
wang_cai.drink()
wang_cai.bark()
print("---------------------分割线-------------------------")
jia_fei = Cat()
jia_fei.eat()
jia_fei.drink()
jia_fei.catch()