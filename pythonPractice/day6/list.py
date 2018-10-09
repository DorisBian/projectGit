#列表，列表索引从0开始
name=["张学友","林志玲","吴彦祖","杨幂","梁朝伟","李易峰","黄轩"]
print(name[0])
print(name[2])
#排序
print(name.sort())
name.sort(reverse=True)
print(name)
#反转
name.reverse()
print(name)



#添加数据
name.append("刘德华")
print(name)
name.insert(3,"hhhhh")
print(name)
stu=["11","22","33"]
name.append(stu)
print(name)
#把列表拆分成单独元素
name.extend(stu)
print(name)

#删除数据
name.remove("李易峰")
print(name)
#删除最后一个元素
name.pop()
print(name)
#通过下标删
del name[2]
print(name)

#修改数据
name[4]="景甜"
print(name)
print(len(name))
#查找元素
if "星星" in name:
    print("列表中含有星星")
else:
    print("列表中没有星星")

