# 进制

# 10进制转成2进制
print(bin(10))
# 2进制转成10进制
print(int("1001",2))
# 10进制转成16进制
print(hex(16))
# 16进制转成10进制
print(int("ff",16))
print(int("0xab",16))
# 16进制转成2进制
print(bin(0xa))
# 10进制转成8进制
print(oct(8))
# 2进制转成16进制
print(hex(0b1001))

# 0b表示2进制
num=0b00000001
print(num)
# num的二进制位向左移动一位，移出位删掉，移进位补0,左移一位相当于乘以2，左移可能会改变一个数的正负
num=num<<1
print(num)
num=num<<1
print(num)
# 右移
num=0b00001000
print(num)
# num的二进制位向左移动一位，移出位删掉，移进位补0,左移一位相当于乘以2，左移可能会改变一个数的正负
num=num>>1
print(num)
num=num>>1
print(num)

# &按位与
num=0b00001000
print(num)
num=num&0b00000001
print(num)

# |按位或
num=0b00001000
print(num)
num=num|0b00000001
print(num)

# ^按位异或,相异为1，相同为0
num=0b00001000
print(num)
num=num^0b00000100
print(num)

# ~取反  ~8=-9
num=0b00001000
print(num)
num=~num
print(num)




