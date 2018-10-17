# 一个对象的属性可以是另外一个类创建的对象

# 士兵突击案例
# 先开发Gun这个类
class Gun:
    def __init__(self,model):
        #枪的型号
        self.model=model
        #子弹数量
        self.bullet_count=0

    #枪装填子弹
    def add_bullet(self,count):
        self.bullet_count+=count

    #枪发射子弹
    def shoot(self):
        #判断是否还有子弹
        if self.bullet_count==0:
            print("%s没有子弹了，不能发射子弹"%self.model)
            return
        #发射一颗子弹
        self.bullet_count-=1;
        print("%s发射子弹成功,还剩%d枚子弹"%(self.model,self.bullet_count))


# 在定义属性时，如果不知道设置什么初始值，可以设置为None
# 假设：每一个新兵都没有枪
class Soldier:
    def __init__(self,name):
        self.name=name
        # 士兵初始没有枪 None关键字表示什么都没有
        self.gun=None

    #士兵开火
    def fire(self):
        # 1.判断士兵是否有枪
        if self.gun is None:
            print("[%s]没有枪......"%self.name)
            #没有枪不需要执行后续代码
            return
        # 2. 高喊口号
        print("冲啊.....[%s]"%self.name)
        # 3. 让枪装填子弹
        self.gun.add_bullet(50)
        # 4. 让枪发射子弹
        self.gun.shoot()

#创建gun对象
ak47=Gun("许三多")

xusanduo=Soldier("许三多")
xusanduo.gun=ak47
xusanduo.fire()

"""
is 与 == 区别：
`is` 用于判断两个变量引用对象是否为同一个 
`==` 用于判断引用变量的值是否相等
"""
