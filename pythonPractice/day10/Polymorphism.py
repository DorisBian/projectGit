"""
多态：定义时的类型和运行时的类型不一样，此时就成为多态
不同的子类对象调用相同的父类方法，产生不同的执行结果
"""
class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)

class XiaoTianQuan(Dog):
    def game(self):
        print("%s 飞到天上去玩耍......"%self.name)

class Person(object):
    def __init__(self,name):
        self.name=name
    #传入的参数是个对象
    def play_with_dog(self,dog):
        print("%s 和 %s 在一起快乐的玩耍......."%(self.name,dog.name))
        # 让狗玩耍
        dog.game()

# 1. 创建一个狗对象
#wang_cai=Dog("旺财")
wang_cai=XiaoTianQuan("飞天旺财")

# 2. 创建一个小明对象
xiao_ming=Person("小明")

# 3. 让小明调用和狗玩的方法
xiao_ming.play_with_dog(wang_cai)
