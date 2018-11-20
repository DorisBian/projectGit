#异常的传递
import time
"""
函数嵌套调用
def demo1():
    return int(input("请用户输入一个整数："))

def demo2():
    demo1()

try:
    print(demo2())
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误%s"%result)
"""

# 在try嵌套中
try:
    f=open("test.txt")
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)

    finally:
        f.close()
        print("关闭文件")

except:
    print("没有这个文件")


