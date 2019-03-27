class Person:
    # 指定只能特点特定的属性
    # __slots__ = ('name', 'age')
    pass


"""
属性不需要声明,直接可以通过对象动态的添加属性
"""

if __name__ == '__main__':
    p = Person()
    p.name = '123'
    p.age = 10
    p.li = []
    p.dic = {}
    print(p)
