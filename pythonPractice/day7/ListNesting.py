#嵌套列表
import random

a=[[1,2,3],[11,22,33],[111,222,333]]
print(a[1])
b=[{"name":"xx","age":18},{"name":"hh","age":20}]
print(b[1])
#获取第二个字典的age
print(b[1]["age"])
print(b[0]["name"])

#3个办公室，8个老师等待工位的分配，完成随机分配
office=[[],[],[]]
techers=["a","b","c","d","e","f","g","h"]
#让八个老师挨个选办公室
for techer in techers:
    index=random.randint(0,2)
    office[index].append(techer)
print("结果为：%s"%office)

