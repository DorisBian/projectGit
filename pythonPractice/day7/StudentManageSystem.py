
# 定一个列表，用来存储所有的学生信息(每个学生是一个字典)
info_list=[]

def print_menu():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")

def add_new_info():
    global info_list
    """添加学生信息"""
    new_name=input("请输入姓名：")
    new_tel=input("请输入手机号：")
    new_qq=input("请输入qq:")

    for temp_info in info_list:
        if temp_info==new_name:
            print("此用户名已被占用，请重新输入")
            return

        # 定义一个字典，用来存储用户的学生信息(这是一个字典)
        info = {}
        #向字典中添加数据
        info["name"]=new_name
        info["tel"]=new_tel
        info["QQ"]=new_qq
        # 向列表中添加这个字典
        info_list.append(info)

def print_all_info():
    """遍历学生信息"""
    print("序号\t姓名\t手机号\tQQ号")
    #
    i=0
    #遍历列表
    for temp in info_list:
        #temp是一个字典
        print("%d\t%s\t%s\t%s"%(i,temp["name"],temp["tel"],temp["QQ"]))
        i+=1


def main():
    while True:
        """用来控制整个流程"""
        print_menu()
        # 获取用户的选择
        num=input("请输入要进行的操作(数字):")

        if num=="1":
            add_new_info()
        elif num=="2":
            pass
        elif num=="3":
            pass
        elif num=="4":
            pass
        elif num=="5":
            print_all_info()
        elif num=="6":
            break
        else:
            print("您输入的指令不存在，请重新输入")

#程序的开始
main()




