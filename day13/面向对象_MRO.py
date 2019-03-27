class A:
    pass


class B(A):
    pass


class C:
    num = 4
    pass


class D(C):
    num = 1
    pass


#
class E(B, D):
    pass


# 查找成员的 先找自身-没有-->左边父类--没有--> 左边的父类的父类
#  如果找到了就直接返回
# 3.x的版本查找成员 深度优先,广度


if __name__ == '__main__':
    e = E()
    print(e.num)
