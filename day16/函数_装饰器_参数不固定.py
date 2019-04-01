import time

# 修饰的函数参数不固定,
"""
1> 在内部函数上面 使用*args 和 **kwargs
2> 在调用核心方法上使用*args和**kwargs

"""


#  手写  熟练掌握
def outer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(end)
        return result

    return inner


# 了解   掌握  熟练掌握
@outer
def add(x, y):
    return x + y


@outer
def add1(x):
    return x * 100


@outer
def add2(x, y=10):
    return (x + y) * 100


if __name__ == '__main__':
    # add = outer(func=add)
    # add(1,3)
    print(add(1, 2))
    print(add1(1))
    print(add2(1, y=100))
