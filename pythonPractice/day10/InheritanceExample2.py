#私有属性和方法是无法被继承的
class Animal:
    def __init__(self,name="动物",color="白色"):
        #私有属性
        self.__name=name
        #非私有属性
        self.color=color
    #私有方法
    def __test(self):
        print(self.__name)
        print(self.color)
    #非私有方法，比较区别
    def test(self):
        print(self.__name)
        print(self.color)

class Dog(Animal):
    def dog_test1(self):
        #print(self.__name)       #不能访问到父类的私有属性
        print(self.color)

    def dog_test2(self):
        #self.__test()          #不能访问到父类的私有方法
        self.test()


a=Animal()
print(a.color)
#print(a.__name)  #程序出现异常，不能访问私有属性
#a.__test()      #程序出现异常，不能访问私有方法
a.test()

print("--"*30)
d=Dog("柴犬","棕色")
print(d.color)
#print(d.__name)
d.dog_test1()
d.dog_test2()



