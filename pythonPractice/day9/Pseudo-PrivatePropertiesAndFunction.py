#伪私有属性和方法
"""
 提示：在日常开发中，不要使用这种方式，访问对象的私有属性或私有方法
 Python中，并没有真正意义的私有
 处理方式：在名称前面加上_类名=>_类名__名称
"""

class Women:
    def __init__(self,name):
        self.name=name
        # 不要问女生的年龄
        self.__age = 18

    def __secret(self):
        print("我的年龄是 %d" %self.__age)

feifei=Women("菲菲")
# 伪私有属性，外部不能直接访问
print(feifei._Women__age)
# 伪私有方法，外部不能直接调用
feifei._Women__secret()

