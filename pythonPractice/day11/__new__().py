# __new__()方法

class MusicPlayer(object):
    #__new__()提供内存空间
    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        # 2. 调用父类的方法，为第一个对象分配空间
        instance=super().__new__(cls)
        # 3. 返回类属性保存的对象引用
        return instance


    #初始化方法
    def __init__(self):
        print("播放器初始化........")

music_player=MusicPlayer()
print(music_player)

#重写 __new__ 方法一定要return super().__new__(cls)


