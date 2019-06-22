# 用户登录功能：登录实际是查询操作，注册时插入操作
# 1.接收用户输入
# 2.根据用户名查询密码  是否查到，查到则有用户，否则，用户名错误
# 3.查到，匹配密码
# 4.匹配成功，提示登录成功；否则，提示密码错误

# coding=utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1

# 接收用户输入
name=input("请输入用户名：")
password=input("请输入密码：")

# 加密
s1=sha1()
s1.update(password.encode('utf8'))
password2=s1.hexdigest()

# 根据用户名查询密码
sql='select passwd from users where name=%s'
mysqlHelper=MysqlHelper('localhost',3306,'python3','root','Root.123')
result=mysqlHelper.get_all(sql,[name])
if len(result)==0:
    print("用户名错误")
elif result[0][0]==password2:
    print("登录成功")
else:
    print("密码错误")

# print(result)
# (('123'),)



