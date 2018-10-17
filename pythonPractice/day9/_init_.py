#内置方法： _init_()
class Cat:
    def __init__(self,new_name,new_age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        self.name=new_name
        self.age=new_age
    def eat(self):
        print("%s在吃鱼....."%self.name)
    def drink(self):
        print("%s在喝水....."%self.name)
    def introduce(self):
        print("本喵的名字是%s,今年%d岁"%(self.name,self.age))

tom=Cat("汤姆",7)
tom.eat()
tom.drink()
print(tom.name)
print(tom.age)
print("-"*40)
tom.introduce()

print("="*40)
lan_mao=Cat("蓝猫",2)
lan_mao.eat()
lan_mao.drink()
lan_mao.introduce()
