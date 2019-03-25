"""
如何声明
操作
变量赋值操作
    获取操作

特点


"""

# 学生管理系统
# list[字典]
# 增删改查

# 实例化 通过类创建对象的过程

# 开发规范 常用使用字母大写,静态变量使用字母大写

"""
需求
# 定义商品信息
# 字段
#   id  商品名称  价格
# 方法
#   打印商品的id 商品的名称 商品的价格
# 测试
#    创建一个商品
"""


class Goods:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def show_info(self):
        print(self.id, self.name, self.price)


class Student(object):
    # 每一个学生名字是不是不一样
    # 构造方法  初始化方法
    SCHOOL_NAME = '1000phone'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 变量   赋值操作
#        取值操作

def test_goods():
    wawa = Goods(id=1, name='空空', price=998.00)
    wawa.show_info()


if __name__ == '__main__':
    pass
    # s = Student(name='金旭宝', age=18)
    # print(s.name)
    #
    s2 = Student('左勇杰', age=19)
    print(s2.name)
    print(s2.age)
    # 修改操作
    # 对象.变量名 = 值
    s2.name = '徐俊杰'
    print(s2.name)

    #  错误的调用方式
    # print(Student.name)

    #     调用静态变量
    print(Student.SCHOOL_NAME)
    # 开发中尽量不要使用对象调用静态变量
    # 千万不要去通过对象修改静态变量
    print(s2.SCHOOL_NAME)
    test_goods()
