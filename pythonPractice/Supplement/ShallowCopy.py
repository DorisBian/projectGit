# 浅拷贝
"""
浅拷贝：对一个对象的顶层拷贝，拷贝了对象，没拷贝内容
深拷贝：对一个对象所以层次的拷贝(递归)
"""
import copy     #深拷贝模块的导入

a=[11,22,33]
print(id(a))
b=a
print(id(b))

a.append(44)
print(a)
print(b)

a={"name":"xiaowang"}
print(id(a))
b=a
print(id(b))
a["id"]=100
print(a)
print(b)
print("----------------------------分割线-----------------------------------")
# 浅拷贝对不可变类型和可变类型的copy不同,使用copy模块的copy功能时，它会根据当前copy的对象是可变还是不可变类型有不同的处理方式
a=[11,22,33]  # 列表元素可修改
b=copy.copy(a)       #深拷贝，copy.copy():copy模块的copy方法
print(id(a))
print(id(b))
a.append(44)
print(a)
print(b)

print("----------------------------分割线-----------------------------------")
a=(11,22,33)   # 元祖的元素不能修改
b=copy.copy(a)       #浅拷贝
print(id(a))
print(id(b))

a="abc"
b=a[:]
print(b)

# 字典的copy方法可以copy一整个字典
d=dict(name="zhangsan",age=27)
co=d.copy()
print(co)






