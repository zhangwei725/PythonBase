# 抽象员工类
# 姓名
# 性别
# 编号
# 年龄
# 工资
# 职位
# 入职的日期


# 敲代码
# 端茶倒水
# 公关


# 将面向过程的 函数,变量封装
# name = 'aaa'

# 方法 就是函数
# def show_name():
#     print(name)
class Student:
    guojia = '中国'

    def __init__(self):
        self.num = 1
        self.name = '张三'


class Emp:
    # 重写 __init__ 方法
    def __init__(self):
        # 在开发中 凡是定义在init方法里的变量就是我们的说的普通字段(对象属性,实例属性)
        self.name = None
        self.job = None
        self.sal = None
        self.join_date = None
        self.sex = None
        self.no = None

    def show_name(self):
        print(self.name)


name = '小明'


def show_name():
    print(name)


if __name__ == '__main__':
    # 创建对象
    xiaoming = Emp()
    # 通过对象.字典 = '值'
    xiaoming.name = '小明'
    xiaoming.no = 1
    xiaoming.show_name()
    show_name()
    # 赋值操作
    # 获取操作
    print(Student.guojia)
