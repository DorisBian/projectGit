# 使用装饰器装饰有不定长参数的函数

def func(functionName):
    print("------func---1-------")
    def func_in(*args,**kwargs):
        print("-------func----in----1----")
        functionName(*args,**kwargs)
        print("-------func----in----2----")

    print("------func---2-------")
    return func_in

@func
def test(a,b,c):
    print("-------test-a=%d,b=%d,c=%d-----"%(a,b,c))

@func
def test2(a,b,c,d):
    print("-------test-a=%d,b=%d,c=%d,d=%d-----"%(a,b,c,d))

test(11,22,33)
test2(44,55,66,77)