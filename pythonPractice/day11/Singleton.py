"""
单例模式：让类创建的对象，在系统中只有一个实例
步骤：1. 定义一个类属性，初始值是None，用于记录单例对象的引用
    2. 重写__new__方法
    3. 如果类属性is None，调用父类方法分配空间，并在类属性中记录结果
    4. 返回类属性中记录的对象引用
"""
class MusicPlayer(object):
    # 定义类属性记录单例对象引用
    instance=None
    # 记录是否执行过初始化动作
    init_flag=False


    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否已经被赋值
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance=super().__new__(cls)
        # 2. 返回类属性的单例引用
        return cls.instance

    #初始化方法
    def __init__(self):
        if not MusicPlayer.init_flag:
            print("播放器初始化........")
            MusicPlayer.init_flag=True

#创建多个对象
music_player1=MusicPlayer()
print(music_player1)

music_player2=MusicPlayer()
print(music_player2)

#结果：控制台输出的内存地址相同，只执行了一次初始化动作，说明只引用了一个对象

