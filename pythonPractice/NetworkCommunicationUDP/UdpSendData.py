# udp网络程序发送接收数据
from socket import *

# 1. 创建udp套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)

# 2. 准备接收方的地址
# '192.168.1.103'表示目的ip地址
dest_addr=("haha",("127.0.0.1",8080)) #注意 是元祖，ip是字符串，端口是数字

# 3. 从键盘获取数据
send_data=input("请输入要发送的数据：")

# 4. 发送数据到指定的电脑上的指定程序中
udp_socket.sendto(send_data.encode("utf-8"),dest_addr)

# 5. 等待接收对方发送的数据
recv_data=udp_socket.recvfrom(1024)

# 6. 显示对方发送的数据
# 接收到的数据recv_data是一个元组
# 第1个元素是对方发送的数据
# 第2个元素是对方的ip和端口
print(recv_data[0].decode("gbk"))
print(recv_data[1])

# 7. 关闭套接字
udp_socket.close()
