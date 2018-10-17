#使用self替换对象中的方法名
class Cat:
    def eat(self):
        print("%s在吃鱼....."%self.name)
    def drink(self):
        print("%s在喝水....."%self.name)
    def introduce(self):
        print("本喵的名字是%s,今年%d岁"%(self.name,self.age))

#创建对象
tom=Cat()
tom.name="汤姆"
tom.age=5
tom.eat()
tom.drink()
print(tom.name)
print(tom.age)
print("-"*40)
tom.introduce()

print("="*40)
lan_mao=Cat()
lan_mao.name="蓝猫"
lan_mao.age=2
lan_mao.eat()
lan_mao.drink()
lan_mao.introduce()
