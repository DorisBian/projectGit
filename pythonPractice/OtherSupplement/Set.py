# 集合
"""
集合与列表、元祖类似，可以存储多个数据，但这些数据是不重复的
作用：去重,可以求交集：x&y,并集:x|y,差集：x-y,对称差集：x^y,
补集:
"""
a=[112,42,41,34,34,72,72,72,88,11,11,3,3,3]
b=set(a)
print(b)

a="abcdef"
b=set(a)
print(b)
A="bef"
B=set(A)
print(B)
print(b&B)      # 取交集
print("----------"*10)
A="bdfhuy"
B=set(A)
print(b)
print(B)
print(b|B)     # 取并集
print(b-B)     # 取差集，取属于集合b但不属于集合B的元素
print(b^B)     # 在b和B中，但不会同时出现在二者中


