"""
 +
 -
 *
 /
"""


# str  int   字典  列表
# 字符串能相加 +        列表 + 类名


class User(object):
    def __init__(self, num, name):
        self.num = num
        self.name = name
        pass

    def __add__(self, other):
        return self.name + other.name

    def __mul__(self, other):
        return self.name * other.num


if __name__ == '__main__':
    user = User(num=5, name='123')
    user1 = User(num=3, name='456')
    print(user1)
    print(user + user1)
    print(user1 * user1)
