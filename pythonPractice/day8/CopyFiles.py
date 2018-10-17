#复制文件
"""
应用一：制作文件的备份
"""
# 提示输入文件
old_file_name=input("请输入要复制的文件名：")
# 以读的方式打开文件
old_file=open(old_file_name,"r")

#新建一个文件
#提取文件的后缀
#pos是个下标
pos=old_file_name.rfind(".")    # rfind返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
#冒号前面省略了        从pos处取，包含冒号
new_file_name=old_file_name[:pos]+"{复件}"+old_file_name[pos:]
new_file=open(new_file_name,"w")

#读取文件内容  如果是大文件，分节读取
#content=old_file.read()
while True:
    content=old_file.read(1024)

    if len(content)>0:
        # 把旧文件中的数据，写到新文件中
        new_file.write(content)
    else:
        break

# 把旧文件中的数据，复制到新文件中
#new_file.write(content)

# 关闭文件
new_file.close()
old_file.close()
