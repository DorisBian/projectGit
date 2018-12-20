# 使用装饰器对无参数的函数进行装饰

from time import ctime,sleep

def time_fun(func):
    def wrapped_func():
        print("%s called at %s"%(func.__name__,ctime()))
        func()
    return wrapped_func

@time_fun
def foo():
    print("I am a foo-----------")

foo()



def func(functionName):
    print("------func---1-------")
    def func_in():
        print("-------func----in----1----")
        functionName()
        print("-------func----in----2----")

    print("------func---2-------")
    return func_in

@func
def test():
    print("-------test----------")

test()

