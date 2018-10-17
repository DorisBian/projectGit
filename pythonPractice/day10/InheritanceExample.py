#继承示例
#定义一个父类
class Cat:
    def __init__(self,name,color="白色"):
        self.name=name
        self.color=color

    def run(self):
        print("%s在跑......"%self.name)

# 定义一个子类，继承Cat类:
class BoSi(Cat):      #class 类名(父类名):
    def set_new_name(self,new_name):
        self.name=new_name

    def eat(self):
        print("%s在吃东西......"%self.name)

bs=BoSi("印度猫")
print(bs.name)
print(bs.color)
bs.run()
bs.eat()
bs.set_new_name("波斯")
bs.eat()
bs.run()

