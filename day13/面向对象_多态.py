class Bird:
    def walk(self):
        print('鸟在走路')

    def swimming(self):
        print('鸟在游泳')

    def jiao(self):
        print('鸟在叫')


class Person:
    def walk(self):
        print('鸟在走路')

    def swimming(self):
        print('鸟在游泳')

    def jiao(self):
        print('鸟在叫')


class Duck:
    def walk(self):
        print('鸭子在走路')

    def swimming(self):
        print('鸭子在游泳')

    def jiao(self):
        print('鸭子在叫')


def test(duck):
    duck.walk()
    duck.swimming()
    duck.jiao()
    

if __name__ == '__main__':
    bird = Bird()
    duck = Duck()
    test(bird)
