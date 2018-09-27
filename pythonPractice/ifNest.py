#没有危险品才能进站
#进站后，有车票才能上车

danger=0#0表示没有，1表示有票
ticket=1

if danger==0:
    print("可以进站")
    if ticket==1:
        print("可以上车")
    else:
        print("不可以上车")
else:
    print("不能进站")

