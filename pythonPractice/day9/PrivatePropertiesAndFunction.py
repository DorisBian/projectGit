#私有属性和方法
# 在定义属性或方法时，在属性名或者方法名前增加两个下划线，定义的就是私有属性或方法
class Women:
    def __init__(self,name):
        self.name=name
        # 不要问女生的年龄
        self.__age = 18

    def __secret(self):
        print("我的年龄是 %d" %self.__age)

feifei=Women("菲菲")
# 私有属性，外部不能直接访问
print(feifei.__age)
# 私有方法，外部不能直接调用
feifei.__secret()

