# 使用property取代getter和setter方法

class Money(object):
    def __init__(self):
        self.__money=0

    @property
    def money(self):      # 函数名money
        return self.__money

    @money.setter        #装饰器
    def money(self,value):
        if isinstance(value,int):
            self.__money=value
        else:
            print("不是整型数字")

a=Money()

a.money=50     # 属性名必须叫money
print(a.money)
print("---"*20)
