#打印图形
def print_line():
    """打印一条横线"""
    print("--"*40)

def print_lines(num):
    i=0
    while i<num:
        print("--"*30)
        i+=1

print_line()
print("+"*80)
print_lines(5)

#求三个数的和
def sum3(num1,num2,num3):
    return  num1+num2+num3
def average_sum3(num1,num2,num3):
    sum_result=sum3(num1,num2,num3)
    return sum_result/3

result=average_sum3(11,22,3)
print("平均值是%d"%result)