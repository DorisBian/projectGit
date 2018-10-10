#字典
#名片管理系统2.0

#cardList是列表，card是字典
#存放名字的列表
cardList=[]

def print_menu():
    """打印功能提示"""
    print("=================")
    print("欢迎使用名片管理系统V2.0")
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查看名片")
    print("5.查看所有名字")
    print("0.退出系统")

def add_info():
    """添加信息"""
    #取全局变量可以不用加global这一行，但修改全局变量按道理要加global xx，但添加新的元素可以不用global xxx

    newName = input("请输入一个新的名字:")
    newAge = input("请输入一个新的年龄:")
    newTel = input("请输入一个新的电话:")
    newAddress = input("请输入一个新的地址:")

    card = {"name": newName, "age": newAge, "tel": newTel, "address": newAddress}
    # 把字典添加到列表中
    cardList.append(card)

def del_info():
    """删除名片信息"""
    global cardList
    #列出想删除的字典在列表中的index,这里输入的序号是str型，要转为int
    del_num=int(input("请输入要删除的名片序号："))
    if 0 <= del_num< len(cardList):
        del_flag=input("你确定要删除么？yes Or no:")
        if del_flag=="yes":   #if语句不用必须写else
            #列表像数组一样有index
            del cardList[del_num]
            print("此名片已删除")
    else:
        print("输入有误，请重新输入")



def modify_info():
    """修改名片信息"""
    #取全局变量可以不用加global这一行，但修改全局变量要加global xx，修改是指改变一个元素所指向的内存空间
    global cardList

    modify_num=int(input("请输入要修改的序号："))
    if 0<= modify_num < len(cardList):
        print("你要修改的信息是：")
        print("name:%s,age:%d,tel:%s,address:%s"%(cardList[modify_num]["name"],cardList[modify_num]["age"],cardList[modify_num]["tel"],cardList[modify_num]["address"]))

        cardList[modify_num]["name"]=input("请输入新的姓名：")
        cardList[modify_num]["age"]=int(input("请输入新的年龄："))
        cardList[modify_num]["tel"]=input("请输入新的号码：")
        cardList[modify_num]["address"]=input("请输入新的地址：")

        print("此名片已修改")

    else:
        print("输入有误，请重新输入")





def search_info():
    """查看名片是否在内"""
    findName=input("请输入要查看的名字:")
    #遍历列表，查找是否有z指定名字的字典
    for card in cardList:
        #
        if findName==card["name"]:
            print("找到了")
            break   #当找到名字之后，就不再执行else
    else:    #for语句也有else
        print("没找到")

def print_all_info():
    """查看所有信息"""
    for card in cardList:
        # 拿到名字遍历字典里的数据
        print("姓名：%s  年龄：%s  电话：%s  地址：%s" % (card["name"], card["age"], card["tel"], card["address"]))

def main():
    while True:
        print_menu()

        command=input("请输入要操作的数字:")
        #print("用户输入的命令是:%s"%command)

        if command=="1":
            add_info()

        elif command=="2":
            del_info()

        elif command=="3":
            modify_info()

        elif command=="4":
            search_info()

        elif command=="5":
            print_all_info()
        elif command=="0":
            break

        else:
            print("命令不存在，请检查输入")

#调用主函数
main()