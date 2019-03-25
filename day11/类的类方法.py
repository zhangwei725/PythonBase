"""

类方法


语法格式
    @classmethod
    def show_school_name(cls):
        pass
# 当我们需要使用类里的变量或者方法
    第一个参数必须有而且在开发中约定使用cls,可以传递任意参数

应用场景
 当我们需要使用类里的静态字段或者类方法的时候

# 操作类中的静态变量 类方法,静态方法   但是千万不要操作对象变量 对象方法

# 调用
类.类方法
对象.类方法
  特点
不需要对象就直接能够操作该方法
"""


class Student(object):
    SCHOOL_NAME = '1000phone'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        pass

    @classmethod
    def show_school_name(cls, *age, **kwargs):
        print(cls.SCHOOL_NAME)


#     函数是一等对象
# 变量必须先声明在使用


if __name__ == '__main__':
    stu = Student(name='小明', age=2)

    stu.show_school_name()
    # 不需要对象就直接能够操作该方法
    # Student.show_school_name()
    Student.show_school_name()
