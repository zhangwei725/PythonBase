# 修饰器也带不固定参数
# 默认缓存的时间

"""
但我们需要在装饰器中传递参数的时候
1> 在外面函数在嵌套一个函数,把func做为这个函数的参数
2> 将内部核心函数对象作为该函数返回值
3> 将核心函数嵌套在该函数中
4> 将该函数作为外部函数的返回值

"""


def outer(username=None, password=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = func()
            return result

        return inner

    return wrapper


@outer(username='admin', password='123456')
def test():
    print('核心函数装饰器svip版')


class A:
    @outer
    def test(self):
        pass


if __name__ == '__main__':
    # test = outer(test, 'admin', '123456')
    # test()
    test()
