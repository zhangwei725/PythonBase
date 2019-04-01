import time

"""
1.装饰带参数
    当修饰的函数有参数的时候,需要将参数定义在装饰器内部函数上
2> 如果修饰的函数有返回值
  1 >  在调用核心函数的地方接受返回值 
  2 >  将返回的结果当做内部函数的返回值
 



"""


# 带参数 无返回值
def outer(func):
    def inner(x, y):
        start = time.time()
        func(x, y)
        end = time.time() - start
        print(end)

    return inner


# 带参数 带返回值
def outer1(func):
    def inner(x, y):
        start = time.time()
        result = func(x, y)
        end = time.time() - start
        print(end)
        return result

    return inner


# 修饰的函数参数不固定,
def outer2(func):
    def inner(x, y):
        start = time.time()
        result = func(x, y)
        end = time.time() - start
        print(end)
        return result

    return inner


@outer1
def add(x, y):
    return x + y


if __name__ == '__main__':
    # add = outer(func=add)
    # add(1,3)
    print(add(1, 2))
