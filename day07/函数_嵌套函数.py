# 函数可以在定义函数

"""
函数只有调用了才会执行函数体里的代码
函数必须声明在前,使用在后

"""

def outer():
    def inner():
        def inner1():
            print('内内函数')

        inner1()
        print("内部函数")

    print('外部函数')
    inner()
# s1 = ' 131 2321 '
# s2 = s1.strip()


outer()
