# 飞鸽传书
from socket import *
import time
import os

udp_socket=None   # 保存udp套接字
feiQ_port=2425    # 飞鸽传书的端口
feiQ_version=1    # 飞秋的版本
feiQ_user_name="doris_test"  # 用户名
feiQ_host_name="mac_pro"    # 主机名字
broadcast_ip="255.255.255.255"   # 广播ip

#飞秋command
IPMSG_BR_ENTRY=0x00000001    # 表示上线提醒
IPMSG_BR_EXIT=0x00000002     # 表示下线提醒

def create_udp_socket():
    """创建udp套接字"""
    global udp_socket

    #1. 创建socket
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    #2. 绑定2425端口      注意：bind()只接受一个参数
    udp_socket.bind(("",feiQ_port))
    #3. 设定允许广播
    # 默认情况下 一个程序是不能发送广播数据（就是当前局域网内所有的电脑都能收到数据），需要下面代码来进行设定
    udp_socket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

def send_broadcast_online():
    """发送上线广播"""

    # demo如下
    # 1:1500816649:doris-test:mac-pro:1:doris-test
    #拼装一个飞鸽传书的数据包
    msg="%d:%d:%s:%s:%d:%s"%(feiQ_version,int(time.time()),feiQ_user_name,feiQ_host_name,IPMSG_BR_ENTRY,feiQ_user_name)

    # print(msg)  # for test

    # 因为windows是使用是gbk编码所以需要编码为gbk
    udp_socket.sendto(msg.encode("gbk"),(broadcast_ip,feiQ_port))




def send_broadcast_offline():
    """发送下线广播"""

    # 1:1500816649:doris-test:mac-pro:1:doris-test
    msg="%d:%d:%s:%s:%d:%s"%(feiQ_version,int(time.time()),feiQ_user_name,feiQ_host_name,IPMSG_BR_EXIT,feiQ_user_name)

    # print(msg)  # for test

    # 因为windows是使用是gbk编码所以需要编码为gbk
    udp_socket.sendto(msg.encode("gbk"), (broadcast_ip, feiQ_port))

def command_menu():
    """打印命令功能菜单"""
    os.system("clear") # 清屏
    print("     飞鸽传书(python)-v1.0")
    print(" 1: 发送上线广播")
    print(" 2: 发送下线广播")
    print(" 0: 退出飞秋")
    print("")
    command_str=input("请输入数字：")
    return command_str

def main():
    """完成整体控制"""
    # 1. 创建udp套接字
    create_udp_socket()

    # 2. 在while循环中获取用户的指令，然后进行相应的操作
    while True:
        # 打印功能菜单
        command_str=command_menu()

        if command_str=="1":
            # 发送上线广播
            send_broadcast_online()
        if command_str == "2":
            # 发送下线广播
            send_broadcast_offline()
        elif command_str=="0":
            # 先发送下线提醒
            send_broadcast_offline()
            # 退出程序
            exit()

if __name__=="__main__":
    main()