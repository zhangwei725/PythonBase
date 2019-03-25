# 新式类

class 类名:
    #
    静态字段 = 10
    def __init__(self):
        #  实例字段
        self.字段1 = None

    # 对象方法
    def bark(self):
        pass

    # 类方法
    @classmethod
    def tian(cls):
        pass

    # 静态方法
    @staticmethod
    def yao():
        pass

    @property
    def age(self):
        pass
