#存放家具的类
#被使用的类先开发
class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        #%.2f是将该浮点数float保留两位小数。2表示保留的位数
        return "[%s] 占地%.2f平米"%(self.name,self.area)

class House:
    #只有需要传递的才写在函数的形参中，不需要传递可以初始化的不需要形参
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area

        #剩余面积
        self.free_area=area
        #家具名称列表
        self.item_list=[]

    def __str__(self):
        #Python 能够自动的将一对括号内部的代码连接在一起
        return "户型：%s\n总面积：%.2f[剩余面积：%.2f]\n家具：%s"\
               %(self.house_type,self.area,
                  self.free_area,self.item_list)

    # 添加家具
    def add_item(self, item):
        print("要添加的家具是：%s"%item)
        # 1.判断家具面积是否大于剩余面积
        if item.area>=self.free_area:
            print("%s的面积太大了，无法添加"%item)
            #不执行后面的代码，用return关键字
            return
        else:
            # 2.将家具的名称添加到列表中
            self.item_list.append(item)
        # 3.计算剩余面积
        self.free_area-=item.area

#创建家具
bed=HouseItem("席梦思",18)
print(bed)
#创建衣柜
chest=HouseItem("衣柜",2)
print(chest)
#创建餐桌
table=HouseItem("餐桌",52)
print(table)

#2.创建房子对象
my_home=House("两室一厅",60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)

"""
 主程序只负责创建房子对象和家具对象
 让房子对象调用add_item方法将家具添加到房子中
 面积计算、剩余面积、家具列表等处理都被封装到房子类的内部
"""


