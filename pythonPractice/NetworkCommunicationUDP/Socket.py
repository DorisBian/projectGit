import socket



# 创建tcp的套接字，套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ...这里是使用套接字的功能（省略）...

# 不用的时候，关闭套接字
s.close()

# 创建udp的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ...这里是使用套接字的功能（省略）...

# 不用的时候，关闭套接字
s.close()



# socket.socket(AddressFamily,Type)

