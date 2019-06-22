# coding=utf-8
# 只要重复使用代码就要考虑封装,这里MysqlHelper封装了所有重复使用的操作
from pymysql import *
# import pymysql

class MysqlHelper:
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset

    def open(self):
        self.conn=connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
        self.cursor=self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    # 增改查操作封装
    def cud(self,sql,params):
        try:
            self.open()

            self.cursor.execute(sql,params)
            self.conn.commit()

            self.close()
            print('ok')
        except Exception as result:
            print(result)

    # 查询
    def get_all(self,sql,params=[]):
        try:
            self.open()

            self.cursor.execute(sql,params)
            # fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
            result=self.cursor.fetchall()
            self.conn.commit()

            self.close()
            return result
            print('ok')
        except Exception as result:
            print(result)
