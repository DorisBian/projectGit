# 模块
# hashlib:通常用来加密
import hashlib
import datetime

m=hashlib.md5()
m.update(b"itcast")
print(m.hexdigest)
m.update(b"itcasthsjdsfgjsbjhfgjpassword=jshjfdvs")
print(m.hexdigest)

KEY_VALUE="Itcast"
now=datetime.datetime.now()
m=hashlib.md5()
str="%s%s"%(KEY_VALUE,now.strftime("%Y%m%d"))
m.update(str.encode("utf-8"))
value=m.hexdigest()
print(value)
