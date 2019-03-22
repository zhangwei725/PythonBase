class Status:
    SHAN_ZHU = '山竹'
    XI_GUA = '西瓜'
    YOU_ZI = '柚子'


class FruitShelf:
    # 1 表示大 2 表示中 3 表示小
    SHELF_SIZE = (1, 2, 3)
    FRUIT_TYPE = ('西瓜', '柚子', '山竹')

    def __init__(self, tier, grid):
        # 货架的层
        self.tier = tier
        # 货架的格子
        self.grid = grid

    @classmethod
    def store_fruit(cls, fruit, num, type):
        flag = False
        if type in cls.SHELF_SIZE and fruit in cls.FRUIT_TYPE:
            if type == 1 and fruit == Status.SHAN_ZHU and num == 1:
                flag = True
            elif type == 2 and (fruit == Status.SHAN_ZHU and num <= 3) or (fruit == Status.YOU_ZI and num == 1):
                flag = True
            elif type == 3 and (fruit == Status.XI_GUA and num <= 2) or (fruit == Status.YOU_ZI and num == 2):
                flag = True
        return flag


class Fruit:
    def __init__(self, name):
        self.name = name
