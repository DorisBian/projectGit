#函数参数高级部分
# 缺省参数
def add_sum(num1,num2):
    print(num1+num2)
add_sum(11,22)
add_sum(45,22)
add_sum(61,22)
add_sum(21,22)

def add_sum(num1,num2=22):
    print(num1+num2)
add_sum(13)  #缺省参数
add_sum(23,58)

#不定长参数
"""
加了星号（*）的变量args会存放所有未命名的变量参数，args为元组
而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典
"""
def add_sum(num1,num2,*args):# 不定长参数
    result=num1+num2
    for num in args:
        result+=num
    print(result)

add_sum(66,98)
add_sum(66,98,11,3,90,100)


def add_sum(num1, num2, operator, *args):# *args全部接收在num2后面的内容，所以operator要放在*args的前面
    if operator=="+":
        result=num1+num2
        for num in args:
            result+=num
        print(result)
    elif operator=="-":
        result = num1 - num2
        for num in args:
            result -= num
        print(result)
add_sum(11,22,"+",35,57,40)
add_sum(11,22,"-",35,57,40)

#命名参数
#一般情况下先写必须的，再写缺省的，再写多余的*args，再写**kwargs
def add_sum(num1, num2, *args,operator="+",**kwargs):#多余的命名参数，加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典

    if operator=="+":
        result=num1+num2
        for num in args:
            result+=num
        print(result)
    elif operator=="-":
        result = num1 - num2
        for num in args:
            result -= num
        print(result)
add_sum(11,22,35,57,40,operator="+",time="28",date="2010")#命名参数，指定"+"给operator




