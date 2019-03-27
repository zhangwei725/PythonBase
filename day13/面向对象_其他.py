"""
isinstance
type
函数的区别是什么
type  输出对象的类型

isinstance       是否是同一个类型,包括父类 (父类不能子类)
"""


class A:
    pass


class B(A):
    pass


class C:
    pass


if __name__ == '__main__':
    b = B()
    a = A()
    c = C()
    # print(type(b))
    # print(type(a))

    # print(isinstance(b, B))
    # print(isinstance(b, A))

    # print(isinstance(a, B))
    # print(isinstance(c, A))

    #     is
    # str1 = '123'
    # str2 = '123'
    # print(id(str1))
    # print(id(str2))
    # print(str1 is 123)

    a2 = a1 = A()
    # 判断内存地址是否相等
    print(id(a1), id(a2))

    print(a1 is a2)
