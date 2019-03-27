class Hero:
    def __init__(self, nickname, lev, hp, mp, agg):
        self.nickname = nickname
        self.lev = lev
        self.hp = hp
        self.mp = mp
        self.agg = agg

    def attack(self, hero):
        hero.hp -= self.agg


"""
如何在父类的基础上面增加属性
"""


# 护甲  方法重写
class SF(Hero):
    #
    def __init__(self, nickname, lev, hp, mp, agg, armor):
        # 第一种使用方法 直接调用父类的init方法
        Hero.__init__(self, nickname, lev, hp, mp, agg)
        self.armor = armor


class JiQiMao(Hero):
    #
    def __init__(self, nickname, lev, hp, mp, agg, mokang):
        # 第一种使用方法 直接调用父类的init方法
        Hero.__init__(self, nickname, lev, hp, mp, agg)
        self.mokang = mokang

    """
    部分重写父类的方法
    """

    def attack(self, hero):
        print('你可真秀')
        Hero.attack(self, hero)
        print('你可真厉害')


if __name__ == '__main__':
    h1 = SF(nickname='快扶我起来,我还能送', lev=1, hp=800, mp=300, agg=40, armor=4)
    h2 = JiQiMao(nickname='朝日天', lev=1, hp=750, mp=400, agg=38, mokang=20)
    h1.attack(h2)
    print(h2.hp)
    h2.attack(h1)
    print(h1.hp)
