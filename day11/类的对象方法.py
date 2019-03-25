"""
方法
语法格式
def   方法名(参数):
    # 语句块
    return  obj

普通方法(对象方法,实例方法)
对象方法可以掉对象属性,可以调用对象方法(可以调用对象的任意成员)

类方法
静态方法
"""


# this   self
# 自身对象
# 什么时候用对象方法    当我们在方法中需要用对象的变量的时候就需要把方法定义成对象方法
# 在方法中第一个参数使用self参数就是对象方法 指定的对象


#  self指向对象本省


class Student(object):
    SCHOOL_NAME = '1000phone'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        _age = self.get_age()
        print("学生的姓名{}\n学生的年龄是:{}".format(self.name, _age))

    def get_age(self):
        return self.age


if __name__ == '__main__':
    # 声明类
    # 创建对象
    # 通过对象调用对象变量,对象方法(普通方法)
    student = Student(name='小明', age=16)
    student.show()
    age = student.get_age()
    print(student.age)
