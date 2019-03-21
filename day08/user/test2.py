from day08.user.test1 import world

name = '循环引入测试'


def hello():
    world()
    print('hello')


if __name__ == '__main__':
    hello()
