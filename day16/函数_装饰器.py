# 装饰本质是一个函数
# 有一个需求 两个相加  打印函数执行的时间

import time


# 这个就的定义装饰器
def outer(func):
    def inner():
        start = time.time()
        func()
        end = time.time() - start
        print(end)

    return inner
# 在函数体修改,在执行函数核心代码开始之前和开始之后

@outer
def test():
    print('这个是测试')


@outer
def test2():
    print('这个是测试13123123')



def add(x, y):
    start = time.time()
    value = x + y
    time.sleep(0.5)
    end = time.time() - start
    print(end)
    return value
# 升级版  将重复代码提取到另外一个函数, 把要测试的函数作为参数
# 在函数体调用测试的核心方法
# 主要的技术, 函数是对象, 函数可以当做参数传递 ,可以通过参数调用函数
# 特点在不修改源代码,实现上述功能
def count_time(func, *args, **kwargs):
    start = time.time()
    func(args, kwargs)
    end = time.time() - start
    print(end)


# 究极版
# 不修改源代码,不改变函数的调用(方式)名称
# 代码复用


#

# 熟悉语法
if __name__ == '__main__':
    # count_time(test)
    # count_time(test2)
    # test = outer(test)
    # test2 = outer(test2)
    # test2()
    test()
    test2()

