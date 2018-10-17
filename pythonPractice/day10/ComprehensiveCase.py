#综合案例

class Game(object):
    #类属性
    top_score=0

    @classmethod
    def show_top_score(cls):
        print("游戏最高分是%d"%cls.top_score)

    @staticmethod
    def show_help():
        print("让僵尸走进房间........")

    def __init__(self,player_name):
        self.player_name=player_name

    def start_game(self):
        print("[%s]开始游戏--------"%self.player_name)

        # 使用类名.修改历史最高分
        Game.top_score=999

# 1. 查看游戏帮助
Game.show_help()
# 2. 查看游戏最高分
Game.show_top_score()
# 3. 创建游戏对象，开始游戏
game=Game("小明")
game.start_game()
# 4. 游戏结束，查看游戏最高分
game.show_top_score()
















