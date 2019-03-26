"""
=面向  对属性 行为


完全可以使用函数替代

应用场景, 当我们不需要使用类里的任何东西的时候,可以定义静态方法
一般通过类.静态方法去调用

"""


class Student:
    def __init__(self):
        pass

    @classmethod
    def cls_method(cls):
        pass

    @staticmethod
    def static_method():
        pass

    @staticmethod
    def test():
        pass


if __name__ == '__main__':
    Student.test()
