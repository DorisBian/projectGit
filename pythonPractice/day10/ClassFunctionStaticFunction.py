#类方法和静态方法
"""
使用场景：通过实例对象和类对象去访问类方法
        对类属性进行修改
"""
class People(object):
    #类属性
    country="china"

    #类方法，用classmethod来进行修饰
    @classmethod
    def get_country(cls):
        return cls.country
    # 对类属性进行修改
    @classmethod
    def set_counry(cls,country):
        cls.country=country

    # 静态方法：需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数
    @staticmethod
    def get_country():
        return People.country


p=People()
print(p.country)
print(p.get_country())  #可以通过实例对象引用
print(People.get_country())     #可以通过类对象引用

p.set_counry("Japan")
print(p.get_country())
print(People.get_country())

print("-------"*10)
#调用静态方法
print(People.get_country())