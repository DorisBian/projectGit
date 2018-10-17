#烤地瓜
"""
属性：cooked_level : 数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了！地瓜开始时是生的
cooked_string : 字符串；描述地瓜的生熟程度
condiments : 地瓜的配料列表，比如番茄酱、芥末酱等
方法：cook() : 把地瓜烤一段时间
add_condiments() : 给地瓜添加配料
__init__() : 设置默认的属性
__str__() : 让print的结果看起来更好一些
"""
class SweetPototo:
    def __init__(self):
        self.cooked_level=0
        self.cooked_string="生的"
        self.condiments=[]

    def cook(self,time):
        self.cooked_level+=time
        if 0<=self.cooked_level<=3:
            self.cooked_string="地瓜是生的"
        elif 3<self.cooked_level<=5:
            self.cooked_string="地瓜半生不熟"
        elif 5<self.cooked_level<=8:
            self.cooked_string="地瓜烤好了"
        elif self.cooked_level>8:
            self.cooked_string="地瓜已经烤成木炭了"

    def __str__(self):
        #必须要加下面这句，如果没有，msg=xxxxxxx,当if条件不成立时return msg就不知道返回的是什么，
        msg="地瓜"+self.cooked_string
        if len(self.condiments)>0:
            for temp in self.condiments:
                msg=msg+"("+temp+","
            msg=msg.strip(",")
            msg=msg+")"
        return msg


    def add_condiments(self,condiment):
        self.condiments.append(condiment)

my_sweet_potato=SweetPototo()
print("有了一个地瓜，还没有烤---------")
print(my_sweet_potato.cooked_level)
print(my_sweet_potato.cooked_string)
print(my_sweet_potato.condiments)
print("---------接下来要进行烤地瓜了-------------")
my_sweet_potato.cook(4)
print("---------地瓜已烤了4分钟--------")
print(my_sweet_potato)
my_sweet_potato.cook(3)
print("---------地瓜又烤了3分钟--------")
print(my_sweet_potato)
print("---------接下来要添加配料---番茄酱--------")
my_sweet_potato.add_condiments("番茄酱")
print(my_sweet_potato)
my_sweet_potato.cook(5)
print("---------地瓜又被烤了5分钟---------")
print(my_sweet_potato)
print("---------接下来要添加配料---芥末酱--------")
my_sweet_potato.add_condiments("芥末酱")
print(my_sweet_potato)



