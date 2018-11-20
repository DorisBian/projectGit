
#模块中有__all__
# __all__=["Test","test1"]
# 如果一个文件中有__all__变量，那么也就意味着这个变量中的元素，不会被from xxx import *时导入

class Test(object):
    def test(self):
        print("------Test类中的test函数-------")

def test1():
    print("------test1函数-------")
def test2():
    print("------test2函数-------")


