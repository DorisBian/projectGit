#列表List
#名片管理系统
print("=================")
print("欢迎使用名片管理系统V1.0")
print("1.添加名片")
print("2.删除名片")
print("3.修改名片")
print("4.查看名片")
print("5.查看所有名字")
print("0.退出系统")

#存放名字的列表
cardList=[]
while True:
    command=input("请输入要操作的数字：")
    print("用户输入的命令是:%s"%command)

    if command=="1":
        newName=input("请输入一个新的名字:")
        #把名字保存到列表
        cardList.append(newName)
        print("最新的名字列表是%s:"%cardList)

    elif command=="2":
        delName=input("请输入要删除的名字：")
        cardList.remove(delName)
        print("最新的名字列表是%s:"%cardList)

    elif command=="3":
        modifyName = input("请输入要修改的名字：")
        newName=input("请输入修改后的名字：")
        if modifyName in cardList:
            #获取要修改的名字的下标
            index=cardList.index(modifyName)
            #使用下标来修改数据,newName在等号右边
            cardList[index]=newName
            print("最新的名字列表是%s:" % cardList)
        else:
            print("名字不在无法修改")

    elif command=="4":
        findName=input("请输入要查看的名字:")
        if findName in cardList:
            print("找到了")
        else:
            print("没找到")

    elif command=="5":
        for name in cardList:
            print(name)

    elif command=="0":
        break

    else:
        print("命令不存在，请检查输入")