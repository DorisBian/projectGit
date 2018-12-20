# 使用装饰器对有返回值的函数进行装饰

def func(functionName):
    print("------func---1-------")
    def func_in():
        print("-------func----in----1----")
        ret=functionName()    # 保存返回来的haha
        print("-------func----in----2----")
        return ret        # 把haha返回到19行处的调用

    print("------func---2-------")
    return func_in

@func
def test():
    print("-------test----------")
    return "haha"

ret=test()
print("test return value is %s"%ret)