#元祖，元素不能修改，能切片，能获取数据，元祖使用小括号
#应用场景：让列表数据不能被修改，以确保数据安全
d=(11)
print(type(d))
#当定义只有一个数据的元祖时，要在后面加个逗号
d=(11,)
print(type(d))
d=(11,22)
print(type(d))

#元祖的遍历
tuple1=(1,2,5,6,8)
for x in tuple1:
    print(x,end=" ")