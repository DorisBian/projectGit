# __getattribute__()的坑
# 重点：__getattribute__方法中禁止使用return self.方法or属性

class Person(object):
    def __getattribute__(self, obj):
        print("-----test------")
        if obj.startswith("a"):
            return "hahha"
        else:
            # 返回的是self对象的test方法的引用
            return self.test

    def test(self):
        print("heihei")

t=Person()
t.a   # 正常
# t.b  会让程序挂掉
"""
当t.b执行obj=b，执行else里的内容，return self.test,test是方法名,
此处返回的是self对象的test方法的引用，也是对象的属性，
那么必然会调用__getattribute__方法，
形成死循环
"""
