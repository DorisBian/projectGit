i=1
sum1=0

while i<=100:
    if i%2==0:
        sum1=sum1+i
        print("i=%d,sum1=%d"%(i,sum1))
    i+=1
print("结果为：%d"%sum1)