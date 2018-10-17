#递归函数
#阶乘
def cal_num(num):
   if num>=1:
       result=num*cal_num(num-1)
   else:
       result=1
   return result

a=cal_num(4)
print(a)

