#交换两个变量的值
a=4
b=5


# 法一
c=a
a=b
b=c
print(a,b)

#法二
a,b=b,a
print(a,b)