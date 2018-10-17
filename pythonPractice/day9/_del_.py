"""内置方法：_del_(),对象销毁时自动调用_del_()
使用场景：当对象在销毁前，希望对象再做点事情时
"""

class Cat:
    def __init__(self,new_name):
        self.name=new_name
        print("%s来了"%self.name)

    def __del__(self):
        print("%s走了"%self.name)

#tom:全局变量
tom=Cat("Tom")
print(tom.name)
print("-"*30)

#del可以删除对象
#del tom


