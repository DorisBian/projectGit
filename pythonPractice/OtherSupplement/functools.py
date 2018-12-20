# functools：放工具函数的工具包
import functools
print(dir(functools))
"""
partial函数(偏函数):
函数在执行时，要带上所有必要的参数进行调用。但是，有时参数可以在函数被调用之前提前获知。这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。
其实就是函数调用的时候，有多个参数，但是其中的一个参数已经知道了，我们可以通过这个参数重新绑定一个新的函数，然后去调用这个新函数。
如果有默认参数的话，他们也可以自动对应上。
"""
def showarg(*args,**kw):
    print(args)
    print(kw)

p1=functools.partial(showarg,1,2,3)
print(p1())
"""
wraps函数:装饰器修复技术
# """
def note(func):
    "note function"
    @functools.wraps(func)      # 带有参数的装饰器
    def wrapper():
        "wrapper function"
        print("note something")
        return func()
    return wrapper

@note
def test():
    "test function"
    print("I am a test")

test()
print(test.__doc__)


