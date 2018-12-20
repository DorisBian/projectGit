# 闭包

def test(number):
    # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量统称为闭包
    def test_in(number_in):
        print("in test_in 函数，number_in is %d"%number_in)
        return number+number_in
    # 这里返回的就是闭包的结果，返回test_in函数的引用
    return test_in

def counter(start=0):
    count=[start]
    def incr():
        count[0]+=1
        return count[0]
    return incr

# 给test函数赋值，这个20就是给参数number
ret=test(20)

# 这里的100给了参数number_in
print(ret(100))
print("*"*20)

c1=counter(5)
print(c1())
print(c1())
print(c1())
c2=counter(100)
print(c2())
print(c2())



