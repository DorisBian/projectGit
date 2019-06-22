# mysql数据库的增删改查
import pymysql

try:
    # 打开
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='Root.123',database='python3',charset='utf8')
    cursor1=conn.cursor()
    # 添加
    # sql='insert into students(name) values("刘备")'        # values()括号内要用双引号
    # 修改
    # sql='update students set name="刘备备" where id=11'
    # 删除
    sql='delete from students where id=6'
    cursor1.execute(sql)

    # mysql执行增删改查默认开启事务
    conn.commit()
    # 关闭
    cursor1.close()
    conn.close()
    print('ok')

except Exception as result:
    print(result)