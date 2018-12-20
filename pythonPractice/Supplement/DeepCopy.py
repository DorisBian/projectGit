# 深拷贝
import copy

a=[11,22,33]
print(a)
print(id(a))

b=copy.deepcopy(a)      # copy.deepcopy():copy模块的deepcopy方法
print(b)
# copy了内容并重新创了一个空间存储
print(id(b))

a.append(44)
print(a)
print(b)
print("----------------------------分割线-----------------------------------")
a=[11,22,33]
b=[44,55,66]
c=[a,b]
d=c
print(id(c))
print(id(d))
e=copy.deepcopy(c)
print(id(e))

a.append(44)
print(a)
print(b)
print(c)
print(e)

f=copy.deepcopy(c)
a.append(88)
print(a)
print(b)
print(c)
print(e)
print(f)

