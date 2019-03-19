"""
 打断点
 熟练使用F8执行下一行代码 ,F7执行函数体的代码 F9执行下一个断点

 不要在声明函数的哪一行打断点

"""

num = 10


def test():
    print(1111)
    print(11231321321)
    print(1231321321)


def hello_debug():
    print('F9跳转下一个断点')


test()
hello_debug()

print('hello')
