# 内置方法：_str_()
"""
在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__str__方法需要返回一个字符串，当做这个对象的描述
"""
class Cat:
    def __init__(self,new_name,new_age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        self.name=new_name
        self.age=new_age

    def __str__(self):
        """返回一个对象的描述信息"""
        return "本喵的名字是%s,今年%d岁"%(self.name,self.age)

    def eat(self):
        print("%s在吃鱼....."%self.name)
    def drink(self):
        print("%s在喝水....."%self.name)

tom=Cat("汤姆",7)
print(tom)

print("="*40)
lan_mao=Cat("蓝猫",2)
print(lan_mao)

