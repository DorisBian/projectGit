# 私有化
# 带下划线的属性相当于java中的private
# 私有属性添加getter和setter方法

class Test(object):
    def __init__(self):
        self.__num=100  #外部不能直接访问，想直接用，可以设置两个方法，一个获取值，一个设置值


    def get_num(self):
        print("---------getter--------")
        return self.__num


    def set_num(self,new_num):
        print("---------setter--------")
        self.__num=new_num
    num=property(get_num,set_num)       # 机器自己识别先调getter还是setter

t=Test()
# t.__num=200      # 添加同名属性
# print(t.__num)

# print(t.get_num())
# t.set_num(50)
# print(t.get_num())
# print("*"*20)

t.num=400      # 相当于t.set_num(400)
print(t.num)

