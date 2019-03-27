class E:
    num = 10
    pass


class A(E):
    pass


class B(A):
    pass


class C(E):
    pass


class D(C):
    pass


class F(D, B):
    pass


#


# 查找成员的 先找自身-没有-->左边父类--没有--> 左边的父类的父类
#  如果找到了就直接返回
# 3.x的版本查找成员 深度优先,广度

# 当他们有共同的父类的时候,会广度优先


if __name__ == '__main__':
    f = F()
    print(f.num)
