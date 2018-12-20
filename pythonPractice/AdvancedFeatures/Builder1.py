# 生成器
"""
通过列表生成式，可以直接创建一个列表。但是受到内存限制，列表容量有限。而且，如果只需要访问列表前面几个元素，后面绝大多数元素占用的空间都浪费了。
生成器generator：可以使列表元素在循环过程中不断推算出后续元素，一边循环一边计算，不用创建完整的list，需要用多少元素创建多少,生成器保存的是算法
生成器创建有多种方法
"""
# 法一
a=[x*2 for x in range(10)]       # a是个列表list
print(a)
b=(x*2 for x in range(10))       # b是个生成器generator
print(b)
# 要打印生成器的每个元素，通过next()函数获得生成器的下一个值
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
# 打印出最后一个值之后再打印就异常退出


# 法二



