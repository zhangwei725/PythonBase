"""
这个是文档
"""


#  函数没有名称


# 语法格式
# 在普通函数中一行代码能实现的,基本可以转化成匿名函数
# 复杂程序千万不要使用匿名函数
# lambda 参数列表:表达式
def add(a, b):
    return a + b


x = 0

# 等价
# 声明完成赋值给变量
num = lambda a, b: a + b
# 通过变量名()的方式去调用
print(num(1, 2))
# 声明完成之后直接调用
print((lambda x, y, z: x * y)(2, 3, 3))


def test(x, y=10):
    return x // y


# 默认值参数
num = (lambda x, y=10: x // y)(20)
print(num)


def test(*args):
    return args


# 不定长关键字
tup = (lambda *args: args)(1, 2, 3, 4)
print(tup)

# 不定长关键字参数
dic = (lambda **kwargs: kwargs)(name='13213', price='10.00')
print(dic)

li = [(lambda x: x + 1)(2)]


# 作用域
# v = 0
# for x in range(10):
#     v = x + 1
#
# print(v)
# if True:
#     x = 1
#
# print(x)
# 在函数体声明的变量只能在函数中使用(包括参数)
def test(x):
    v = x + 1
    print(v)
    return v

