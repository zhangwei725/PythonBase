# 函数可以在定义函数

"""
函数只有调用了才会执行函数体里的代码
函数必须声明在前,使用在后
"""


def outer():
    name = '空空'

    def inner():
        nonlocal name
        name = '美美'
        print(name)

    inner()
    print(name)


outer()
