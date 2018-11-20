#抛出自定义异常

def input_password():
    # 1. 提示用户输入密码
    pwd=input("请输入密码：")

    # 2. 判断密码长度，如果长度 >= 8，返回用户输入的密码
    if len(pwd)>= 8:
        return pwd

    # 3. 密码长度不够，需要抛出异常
    # 1> 创建异常对象 - 使用异常的错误信息字符串作为参数
    ex=Exception("密码长度不够")

    # 2> 主动抛出异常对象
    raise ex

try:
    user_pwd=input_password()
    print(user_pwd)
except Exception as result:
    print("发现错误：%s"%result)



class ShortInputException(Exception):
    """自定义的异常类"""
    def __init__(self, length, at_least):
        #super().__init__()
        self.length = length
        self.at_least = at_least

def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise引发一个自定义的异常，主动抛出异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:#x这个变量被绑定到了错误的实例
        #捕获未知错误
        print("ShortInputException: 输入的长度是 %d,长度至少应是 %d"% (result.length, result.at_least))
    else:
        print("没有异常发生.")

main()
