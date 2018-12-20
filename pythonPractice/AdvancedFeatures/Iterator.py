# 迭代器
"""
列表，元祖，字典，字符串，集合(set)
另一类是生成器，包括生成器和带yield的generator Function。
这些可直接作用于for循环的对象统称为可迭代对象：Iterable
"""
from collections.abc import Iterator
from collections.abc import Iterable

# 可用isinstance()判断对象是否可迭代
print(isinstance([],Iterable))     # 列表可迭代
print(isinstance((),Iterable))     # 元祖可迭代
print(isinstance("abc",Iterable))  # 字符串可迭代
"""
生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
"""
print(isinstance((x for x in range(10)),Iterable))     # 生成器可迭代
print(isinstance(100,Iterable))    # 整数不可迭代

"""
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象：
"""
print("-------"*30)
print(isinstance((x for x in range(10)),Iterator))   # 生成器都是迭代器对象
print(isinstance([],Iterator))   # 列表不是迭代器对象
print(isinstance({},Iterator))   # 字典不是迭代器
print(isinstance((),Iterator))   # 元祖不是迭代器
print(isinstance("abc",Iterator)) # 字符串不是迭代器

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print("-------"*30)
print(isinstance(iter([]),Iterator))
print(isinstance(iter("abc"),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter(()),Iterator))