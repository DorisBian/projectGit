# coding:utf-8
# 类之间需要有两个空行
class Bar(object):
    """"""
    pass


class Foo(object):
    """"""
    def __init__(self):
        pass

    def __getattr__(self, item):
        # 这个函数经常使用
        print(item),
        return self

    def __getattribute__(self, item):
        # 这个函数很少改动
        pass

    def __str__(self):
        return ""

    def say_hello(self):
        pass

# obj=Foo()
# "think" obj.think
# obj.different

print(Foo().think.different.itcast)

# 要返回的是think different itcast
# 类首字母大写，变量小写字母，单词之间加下划线;函数也一样，小写字母，单词之间加下划线
