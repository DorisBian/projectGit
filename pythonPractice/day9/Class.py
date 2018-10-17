# 类名的 命名规则 要符合 大驼峰命名法
class Cat:
    def eat(self):
        print("猫在吃鱼.....")
    def drink(self):
        print("猫在喝水.....")
    def introduce(self):
        print("本喵的名字是%s,今年%d岁"%(tom.name,tom.age))

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
lan_mao.age="2"
lan_mao.eat()
lan_mao.drink()
