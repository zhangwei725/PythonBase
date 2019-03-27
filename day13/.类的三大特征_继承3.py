"""
私有的属性不能被继承
"""


class Person:
    def __init__(self, name):
        self.name = name
        self._age = 1
        self.__sex = '男'

    def _eat(self):
        print('1111111')


class Student(Person):
    def __init__(self, name, no):
        Person.__init__(self, name=name)
        self.no = no


if __name__ == '__main__':
    # stu = Student(name='宝宝', no=1)
    # print(stu._age)
    # print(stu.__sex)
    # stu._eat()
    pass
