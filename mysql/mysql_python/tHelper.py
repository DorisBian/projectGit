# coding=utf-8
from MysqlHelper import *

# 修改
# name=input("请输入学生姓名：")
# id1=input("请输入学生id：")
#
# sql='update students set name=%s where id=%s'
# params=[name,id1]
#
# mysqlHelper=MysqlHelper('localhost',3306,'python3','root','Root.123')
# mysqlHelper.cud(sql,params)

# 查询
sql='select id,name from students where id<5'
mysqlHelper=MysqlHelper('localhost',3306,'python3','root','Root.123')
result=mysqlHelper.get_all(sql)
print(result)
