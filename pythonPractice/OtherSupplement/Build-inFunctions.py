# 内建函数

# map函数：根据提供的函数对指定序列做映射。返回值是list
ret=map(lambda x:x*x,[1,2,3])
for tmp in ret:
    print(tmp)

print("--------"*20)
ret=map(lambda x,y:x+y,[1,2,3],[4,5,6])
for tmp in ret:
    print(tmp)

print("--------"*20)
def f1(x,y):
    return x,y
l1=[0,1,2,3,4,5,6]
l2=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
l3=map(f1,l1,l2)
print(list(l3))

# filter函数：对指定序列执行过滤操作，filter函数会对序列参数sequence中的每个元素调用Function函数，最后返回的结果只包含调用结果为True的元素，1为True，0为False
print("--------"*20)
list1=filter(lambda x:x%2,[1,2,3,4])
print(list(list1))

filter(None,"she")   # 不过滤
print("--------"*20)

# reduce函数：对参数序列中元素进行累积
from functools import reduce
ret=reduce(lambda x,y:x+y,[1,2,3,4])    # 1+2+3+4
print(ret)

ret=reduce(lambda x,y:x+y,[1,2,3,4],5)  # 1+5+2+3+4
print(ret)

ret=reduce(lambda x,y:x+y,["aa","bb","cc"],"dd")
print(ret)

# sorted函数：
print("--------"*20)
a=[12,45,34,76,98,122,453,214,561,43]
a.sort()
print(a)
a.sort(reverse=True)    # 倒序排列
print(a)
print("*********"*10)
print(sorted([1,5,9,3,7,2]))
print(sorted([1,5,9,3,7,2],reverse=1))
print(sorted(["dd","aa","cc","bb"]))
print(sorted(["dd","aa","cc","bb"],reverse=1))



