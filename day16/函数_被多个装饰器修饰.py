def outer1(func):
    def inner(*args, **kwargs):
        print('装饰器1')
        result = func(*args, **kwargs)
        print('核心代码执行后---->1')
        return result

    return inner


def outer2(func):
    def inner(*args, **kwargs):
        print("装饰器2")
        result = func(*args, **kwargs)
        print('核心代码执行后---->2')
        return result

    return inner


@outer1
@outer2
def test():
    print('核心代码被执行')


@outer1
@outer2
def test1(x, y):
    print('核心代码被执行')
    return x + y


"""
当有多个装饰器修饰同一个函数的时候
从上之下执行装饰器的代码,然后在执行核心

如果装饰器的核心代码执行前后都有代码
1> 先执行最上面的装饰器的核心代码执行前的代码,直到最后一个装饰器的核心代码执行前的代码执行完
2> 执行核心代码(核心代码只会执行一次)
3> 先执行最下面的装饰器核心代码执行后的代码直到最上面的装饰器的核心代码执行前的代码执行完


"""
if __name__ == '__main__':
    # test()
    print(test1(1, 3))
