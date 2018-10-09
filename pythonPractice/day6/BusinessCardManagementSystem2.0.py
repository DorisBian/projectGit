#字典
#名片管理系统2.0

#cardList是列表，card是字典
#存放名字的列表
cardList=[]
while True:
    print("=================")
    print("欢迎使用名片管理系统V2.0")
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查看名片")
    print("5.查看所有名字")
    print("0.退出系统")

    command=input("请输入要操作的数字:")
    #print("用户输入的命令是:%s"%command)

    if command=="1":
        newName=input("请输入一个新的名字:")
        newAge=input("请输入一个新的年龄:")
        newTel=input("请输入一个新的电话:")
        newAddress=input("请输入一个新的地址:")

        card = {"name": newName, "age": newAge, "tel": newTel, "address": newAddress}
        #把字典添加到列表中
        cardList.append(card)
        print("最新的列表是%s:"%cardList)

    elif command=="2":
        pass

    elif command=="3":
        pass

    elif command=="4":
        findName=input("请输入要查看的名字:")
        #遍历列表
        for card in cardList:
            #
            if findName==card["name"]:
                print("找到了")
                break
        else:    #for语句也有else
            print("没找到")

    elif command=="5":
        for card in cardList:
            #拿到名字遍历字典里的数据
            print("姓名：%s  年龄：%s  电话：%s  地址：%s"%(card["name"],card["age"],card["tel"],card["address"]))

    elif command=="0":
        break

    else:
        print("命令不存在，请检查输入")