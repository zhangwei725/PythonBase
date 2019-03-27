"""
设计模式    优秀的程序员在开发中碰到问题,解决特定问题的一种总结
1 设计原则(后期补充)

# 23中设计模式  (淡化)
1>单例模式
2>工厂模式
3>观察者模式
"""
"""
什么是单例
作用: 让类在创建对象的时候,在整个系统的生命周期中只有一个实例
# 在开发软件过程中,有些类每个模块都要频繁用到  数据连接(经常回收) (这样的话减少系统创建对象和回收对象负担)

如何创建单例模式 
1>使用模块
2> 重新__new__方法
3> 基于装饰器
4> 重写元类  

"""
"""

__new__ 底层创建对象分配内存的方法 在__init__方法之前执行.必须调用有返回值,(调用父类的创建对象)
__init__ 构造方法,初始化成员变量




1>第一步重新__new_-方法
2>第二歩定义一个私有的静态变量
3> 判断如果第二歩定义静态变量为None表示该类是第一次创建实例调用父类的__new__方法创建的迹象
4> 如果步是第一次创建对象,直接返回定义的私有的静态变量即可
"""


class Person:
    pass


class User:
    """
    脑瓜疼

    """
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
            return cls.__INSTANCE
        else:
            return cls.__INSTANCE

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('对象被销毁了')

    def __str__(self):
        return 'name:{}'.format(self.name)

    # 可以把类的对象当做函数来调用
    #  通过对象()的方法会来调用该方法
    def __call__(self, *args, **kwargs):
        print("__call__")


if __name__ == '__main__':
    user = User(name='小明')
    # print(id(user), id(user1), id(user2))
    # p1 = Person()
    # p2 = Person()
    # p3 = Person()
    user()

    # 将对象转化成字典

    # print(user.__dict__)
    print(user.__doc__)

    # print(user)
    #
    # print(id(p1), id(p2), id(p3))
