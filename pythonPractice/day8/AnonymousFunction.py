#匿名函数
"""
匿名函数不能写return
匿名函数不能直接调用print，因为lambda需要一个表达式
"""
#定义一个普通函数
def sum(num1,num2):
    return num1+num2

result=sum(33,90)
print(result)

"""定义匿名函数
用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。
lambda 形参：执行语句
"""
f=lambda num1,num2:num1+num2
result=f(11,22)
print(result)

# 应用一
def control_num(a,b,func):
    return func(a,b)

r=control_num(11,22,lambda x,y:x+y)
print(r)
r=control_num(11,22,lambda x,y:x-y)
print(r)
r=control_num(11,22,lambda x,y:x*y)
print(r)

# 应用二：对列表排序
nums=[123,3290546,326543,689070764,326237,37647,437,1238,38758010,16,30,1]
nums.reverse()  # 倒序
print(nums)
info=[{"name":"zhangsan","age":20},{"name":"lisi","age":22}]
info.reverse()
info.sort(key=lambda x:x["name"])   #列表里的字典之间不能排序，解决方法：匿名函数
print(info)   #l在z前面，升序排列
info.sort(key=lambda x:x["age"])
print(info)   #20在22前面