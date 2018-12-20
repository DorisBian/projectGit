# 生成器
# send
def test():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1

t=test()
print(t.__next__())
print(t.__next__())
print(t.send("hhhhh"))