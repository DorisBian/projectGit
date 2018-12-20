# 内建属性
# __getattribute__方法中禁止使用return self.函数名

class Itcast(object):
    def __init__(self,subject1):
        self.subject1=subject1
        self.subject2="cpp"

    # 属性访问时的拦截器，打log,有这个方法后所以访问属性的地方一定是先调用这个方法
    def __getattribute__(self, obj):     # obj---->"subject1"
        print("====>1>%s"%obj)
        if obj=="subject1":
            print("log subject1")
            return "redirect python"
        else:        # 测试时注释掉这2行，将找不到subject2
            temp=object.__getattribute__(self,obj)
            print("=====>2>%s"%str(temp))
            return temp

    def show(self):
        print("this is Itcast")

s=Itcast("python")
print(s.subject1)
print(s.subject2)
s.show()
# 1. 先获取show属性对应的结果，，，，应该是一个方法
# 2. 方法()