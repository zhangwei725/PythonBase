# 当我们不知道参数的长度时候可以使用可变长度参数
# 定义的时候在函数*args声明  args变量名是其他 但开发中不要去修改这个变量
# 在一个函数里只能有一个*args
#  在使用的时候我们可以使用任意多个实参,但是实参不能使用关键字参数

def fun(*args):
    # 解包
    for item in args:
        print(item)


fun(1, 2, 3, 54, 5, 6, True, [1, 2, 3, 4])
