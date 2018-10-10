#函数返回值高级部分
# 函数中下面的代码不会被执行，因为return除了能够将数据返回之外，还有一个隐藏的功能：结束函数
def get_my_info():
    """获取我的信息"""
    name="doris"
    return name
    age=19
    return age
    address="shanghai"
    return address

result=get_my_info()
print(result)
result=get_my_info()
print(result)
result=get_my_info()
print(result)

def get_my_info():
    """获取我的信息"""
    name="doris"
    age=19
    address="shanghai"
    #return [name,age,address]
    #return {"name":name,"age":age,"address":address}
    return name,age,address      # 默认是元组
result=get_my_info()
print(result)
print(result[0])
print(result[1])
print(result[2])

