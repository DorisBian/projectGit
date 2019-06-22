import pymysql

try:
    # 打开
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='Root.123',database='python3',charset='utf8')
    cursor1=conn.cursor()

    name=input("请输入学生姓名:")
    sql='insert into students(name) values(%s)'
    cursor1.execute(sql,[name])    # 第二个参数是个列表
    # 提交事务
    conn.commit()

    # 关闭
    cursor1.close()
    conn.close()
    print('ok')

except Exception as result:
    print(result)