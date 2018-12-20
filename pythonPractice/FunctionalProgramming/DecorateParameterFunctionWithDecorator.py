# 使用装饰器对有参数的函数进行装饰

def func(functionName):
    print("------func---1-------")
    def func_in(a,b):      # 如果a,b没有定义，那么会导致17行的调用失败，参数名可以不同可以相同
        print("-------func----in----1----")
        functionName(a,b)     # 如果没有把a,b当做实参进行传递，那么会导致14行的函数调用失败
        print("-------func----in----2----")

    print("------func---2-------")
    return func_in

@func
def test(a,b):
    print("-------test-a=%d,b=%d-----"%(a,b))

test(11,22)