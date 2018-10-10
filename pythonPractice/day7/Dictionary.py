#字典
a={"name":"zhangsan"}
print(a["name"])
#报错
#print(a["age"])
print(a.get("name"))
#不报错，age不存在，返回none
print(a.get("age"))
#不存在age，返回默认值19
print(a.get("age",19))


b={"name":"zhangsan","age":18,"sex":"m"}
#获取键
print(b.keys())
#获取值
print(b.values())
print(b.items())
print(b.copy())
#判断字典里是否有age这个键
print("age" in b)
print("zhangsan" in b)
print(b.__len__())


#遍历字典的键
b={"name":"zhangsan","age":18,"sex":"m"}
for key in b.keys():
    print(key)

#遍历字典的值
b={"name":"zhangsan","age":18,"sex":"m"}
for value in b.values():
    print(value)

#遍历字典的项
b={"name":"zhangsan","age":18,"sex":"m"}
for item in b.items():
    print(item)

#遍历字典的键值对
b={"name":"zhangsan","age":18,"sex":"m"}
for key,value in b.items():
    print("key=%s,value=%s"%(key,value))

#实现带下标索引的遍历
char={"a","b","c","d"}
i=0
for ch in char:
    print("%d %s"%(i,ch))
    i+=1


#每次遍历enumerate（）都会返回一个集合（键值对），只有一个变量，那么这个变量就是一个集合类型
char={"a","b","c","d"}
i=0
for ch in enumerate(char):
    print("i=%d ch=%s"%(i,ch))
    i+=1

#如果是两个变量，集合会分别赋值键值对
char={"a","b","c","d"}
i=0
for i,ch in enumerate(char):
    print("i=%d ch=%s"%(i,ch))
    i+=1


char={"a","b","c","d"}
i=0
for i,ch in enumerate(char):
    print(i,ch)
    i+=1