# 闭包应用
"""
y=x+1的实现与y=4x+5的实现，闭包也可提高代码的可复用性
"""
def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line1=line_conf(1,1)
line2=line_conf(4,5)
print(line1(5))
print(line2(5))