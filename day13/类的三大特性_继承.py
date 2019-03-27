"""

"""


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def study(self):
        print('{}在学习'.format(self.name))


# 模型对象
# save   update


class XiaoMing(Person):
    """
    重写父类的方法
    """

    def study(self):
        print('{}认真的学习'.format(self.name))


class XiaoHong(Person):
    """
    在父类的基础上进行扩展
    """

    def tanlianai(self, person):
        print('{}在跟{}谈恋爱'.format(self.name, person.name))


if __name__ == '__main__':
    p1 = XiaoHong(name='小红', age=18, sex='女')
    p2 = XiaoMing(name='小明', age=18, sex='男')
    p1.study()
    p2.study()
    p1.tanlianai(p2)
