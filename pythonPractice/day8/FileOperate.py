#文件的操作

#写入文件换行与输出换行不同，写入文件换行需要使用变量
print("hello world!I am here!\nwelcome to shanghai")

#打开
f=open("xxx.txt","r")
#操作
content=f.read()
print(content)
#关闭
f.close()

#write
f = open('test.txt', 'w')
f.write("hello world!I am here!\twelcome to shanghai")
f.close()

#read  尽量不要一次把文件全读完
f=open("test.txt","r")
content=f.read(5)
print(content)
print("-"*40)
content=f.read()
print(content)
f.close()

#readlines
f=open("test.txt","r")
content=f.readlines()
print(content)
print(type(content))

i=1
for temp in content:
    print("%i:%s"%(i,temp))
    i+=1
f.close()
#运行失败，找fault

#readline
f=open("test.txt","r")
content=f.readline()
print("1：%s"%content)
print("2：%s"%content)
f.close()



