"""
类装饰器,就是在类上使用装饰器


"""


class ObjectDecorator:
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)

        return cls.__INSTANCE

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print(111)


"""
先要将类的对象保存在字典中
如果对象存在字典中 则直接返回该对象
否则通过class创建对象

"""

#

"""
1>将cls对象直接作为参数传递给装饰器
2> 创建字典对象用于保存类的单例对象
3> 创建内部函数获取或者创建单例
3.1> 判断单例对象是否存在字典中
3.2>  如果不存在就创建这个对象,保存到字典中
3.3> 如果存在从字典中获取该单例对象直接返回
"""


def singleton(*args, **kwargs):
    instances = {}

    def wrapper(cls):
        # 用来保存创建对象
        def get_instance(*args, **kwargs):
            #  判断instances字典中是否包含了cls
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]

        return get_instance

    return wrapper


@singleton
class A:
    pass


@singleton
class B:
    pass


if __name__ == '__main__':
    a = A()
    a1 = A()
    print(id(a))
    print(id(a1))
    b = B()
    b1 = B()
