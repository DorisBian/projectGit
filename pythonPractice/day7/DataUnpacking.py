"""
数据拆包
拆包时要注意，需要拆的数据的个数要与变量的个数相同，否则程序会异常
除了对元组拆包之外，还可以对列表、字典等拆包
"""
def get_my_info():
    """获取我的信息"""
    name="doris"
    age=19
    address="shanghai"
    #return [name,age,address]
    #return {"name":name,"age":age,"address":address}
    return name,age,address      # 默认是元组

name, age, address=get_my_info()
print(name)
print(age)
print(address)