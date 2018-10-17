#类属性和实例属性(对象属性)

class People(object):
    name = 'Tom'  #公有的类属性
    __age = 12     #私有的类属性

p = People()

print(p.name)
print(People.name)
#print(p.__age)            #错误，不能在类外通过实例对象访问私有的类属性
#print(People.__age)        #错误，不能在类外通过类对象访问私有的类属性



class People(object):
    address = "江苏" # 类属性
    def __init__(self):
        self.name = "xiaowang" #实例属性
        self.age = 20 #实例属性

p = People()
p.age =12 #实例属性
print(p.address)
print(p.name)
print(p.age)

print(People.address)
#print(People.name)    #错误
#print(People.age)     #错误


# 通过实例(对象)去修改类属性
class People(object):
    country = 'china' #类属性

print(People.country)
p = People()
print(p.country)
p.country = 'japan'
print(p.country)      #实例属性会屏蔽掉同名的类属性
print(People.country)
del p.country    #删除实例属性
print(p.country)