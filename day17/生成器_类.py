"""
__next__
__iter__

"""


# 如果想让对象实现可迭代,就需要重写上面的两个方法

class Person:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        return self.num + 1


if __name__ == '__main__':
    person = Person(num=1)
    for p in person:
        print(p)
