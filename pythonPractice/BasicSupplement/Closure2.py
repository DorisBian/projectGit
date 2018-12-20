# 闭包
# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。

def test(number):
    # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量统称为闭包
    def test_in(number_in):
        print("in test_in 函数，number_in is %d"%number_in)
        return number+number_in
    # 这里返回的就是闭包的结果，返回test_in函数的引用
    return test_in

def counter(start=0):
    def incr():
        # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        nonlocal start
        start+=1
        return start
    return incr

c1=counter(5)
print(c1())
print(c1())
print(c1())
c2=counter(50)
print(c2())
print(c2())

print(c1())
print(c1())
print(c2())
print(c2())



