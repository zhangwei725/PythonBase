class Dice:
    def __init__(self):
        self.num = 1

    def random_num(self):
        import random
        self.num = random.randint(1, 6)
        return self.num


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 5000


"""
娱乐系统上线了
"""


class HappySys:
    dices = [Dice(), Dice(), Dice()]

    """
    给玩家充值
    """

    @staticmethod
    def put_money(money, player):
        player.money += money

    @classmethod
    def open(cls):
        num = 0
        for dice in cls.dices:
            num += dice.random_num()
        print(num)
        return True if num >= 8 else False

    @staticmethod
    def input_value():
        num = 0
        money = 0
        try:
            num = int(input('请输入大小1,表示打,0表示小'))
            money = int(input('请输入金额!!!'))
        except:
            print('输入有误请重新输入')
        return num, money

    @staticmethod
    def result(player):
        num, money = HappySys.input_value()
        is_open = HappySys.open()
        if is_open == bool(num):
            print('恭喜您中奖了')
            player.money += money
        else:
            print('很遗憾!!奖品与擦肩而过!!!请再接再厉!!!')
            player.money -= money


# 作用域  函数  类  异常处理
def test_happy_sys():
    while True:
        print('游戏开始')
        player = Player(name='老王')
        HappySys.result(player)

object
if __name__ == '__main__':
    test_happy_sys()



