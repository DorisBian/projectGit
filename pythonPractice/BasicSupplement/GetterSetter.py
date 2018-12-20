# 私有属性添加getter和setter方法
# 使用property升级getter和setter方法

class Money(object):
    def __init__(self):
        self.__money=0

    def get_money(self):
        return self.__money

    def set_money(self,value):
        if isinstance(value,int):
            self.__money=value
        else:
            print("不是整型数字")

    money=property(get_money,set_money)

a=Money()
# print(a.get_money())
# a.set_money(10)
# print(a.get_money())
print("---"*20)

print(a.money)
a.money=50
print(a.money)
print("---"*20)








