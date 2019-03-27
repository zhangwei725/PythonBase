import random


class Fish:
    def __init__(self):
        self._x = 0
        self._y = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if 0 <= x <= 10:
            self._x = x
        else:
            raise Exception('x out go l')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if 0 <= y <= 10:
            self._y = y
        else:
            raise Exception('y out go l')
        #  乌龟

    def move(self):
        temp_x = self.x + random.choice([1, -1])
        temp_y = self.y + random.choice([1, -1])
        self._x = self.is_verify(temp_x)
        self._y = self.is_verify(temp_y)
        # 每移动一次就体力-1

    def is_verify(self, value):
        """
        验证x y的坐标是否合法,并返回合理的值
        :param value:
        :return:
        """
        if 0 <= value <= 10:
            return value
        elif value < 0:
            return abs(value)
        else:
            return 20 - value


class Tortoise:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #  体力
        self.strength = 100

    #  乌龟
    def move(self):
        temp_x = self.x + random.choice([1, 2, -1, -2])
        temp_y = self.y + random.choice([1, 2, -1, -2])
        self.x = self.is_verify(temp_x)
        self.y = self.is_verify(temp_y)
        # 每移动一次就体力-1
        self.strength -= 1

    def eat(self):
        self.strength = self.strength + 20 if self.strength + 20 <= 100 else 100

    def is_verify(self, value):
        """
        验证x y的坐标是否合法,并返回合理的值
        :param value:
        :return:
        """
        if 0 <= value <= 10:
            return value
        elif value < 0:
            return abs(value)
        else:
            return 20 - value


class GameManger:

    @staticmethod
    def start():
        fishes = []
        for i in range(10):
            fish = Fish()
            fish.x = random.randint(0, 10)
            fish.y = random.randint(0, 10)
            fishes.append(fish)
        tortoise = Tortoise(x=random.randint(0, 10), y=random.randint(0, 10))
        while

        print('游戏开始咯!!!')

    @staticmethod
    def is_position(tortoise, fishes):
        if fishes:
            for fish in fishes:
                if tortoise.x == fish.x and tortoise.y == fish.y:
                    tortoise.eat()
                    fishes.remove(fish)
                    print('吃掉一条毛毛鱼')
                    break


if __name__ == '__main__':
    GameManger.start()
