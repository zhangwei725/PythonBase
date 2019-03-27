"""
super() 函数
"""


class Month:
    def __init__(self):
        super().__init__()
        self.name = '这个是母类的name'


class Father:
    def __init__(self):
        super().__init__()
        print('这个是父类的__init__')

    def give_money(self):
        print('父类赚钱的方法')


class Child(Father,Month):
    pass


# 将复杂的问题简单化

if __name__ == '__main__':
    child = Child()
    print(child.name)
    print(child.give_money())
