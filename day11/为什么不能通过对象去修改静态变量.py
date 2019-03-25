# ctrl+ shift + u  大小写转化
class Test:
    HELLO = 'world'

    def __init__(self):
        pass


# 静态变量是所有对象共享

def test1():
    # 不要跟傻逼讲道理,
    t1 = Test()
    t2 = Test()
    t3 = Test()
    # 分析 通过对象修改了静态变量, 发现只有该对象被修改
    t1.HELLO = 'Hello World 改变世界'
    print(t1.HELLO)
    t1.HELLO = '1231321321'
    print(t1.HELLO)

    print(t2.HELLO)
    print(t3.HELLO)
    print(Test.HELLO)


def test2():
    # 不要跟傻逼讲道理,
    t1 = Test()
    t2 = Test()
    t3 = Test()
    # 分析 通过对象修改了静态变量, 发现只有该对象被修改
    Test.HELLO = '编程改变世界'
    print(t1.HELLO)
    print(t2.HELLO)
    print(t3.HELLO)
    print(Test.HELLO)


if __name__ == '__main__':
    test2()
