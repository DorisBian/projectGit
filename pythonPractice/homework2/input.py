user=input("请输入用户名：")
password=input("请输入密码：")
if user=="admin" and password=="123":
    print("欢迎进入%s的世界"%user)
else:
    print("用户名或密码错误")