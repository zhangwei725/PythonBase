def except_example():
    from datetime import datetime,timedelta
    # datetime.now() + timedelta(days=7)

    try:
        '1' + 1
    except Exception as e:
        pass

"""
:except 可以是多个
在核心代码中 直接使用 try: except: 对程序同一处理
如果不管你是执行成功或者失败都要去执行的代码写在finally语句块中

"""


def except_example1():
    try:
        li = [1, 2, 3]
        li[0]
        print(li[10])
        # print(a)
    except TypeError as e:
        print(1111)
    except IndexError as e:
        print(1111)
    except NameError as e:
        print('未定义!!!')


def except_example2():
    try:
        name = int('asaaa')
        print('这个正常的代码')
    except:
        print('这个是异常的代码')
    finally:
        print('不管你是处异常还是正常执行完成,都会走的代码!!!')


"""
如何手动的抛出异常
"""

"""
reise  异常信息对象
必须继承自Exception或者他的子类
"""


# 用户名   验证  用户不符合规范

# 第一种  函数 可以改变作用域   第二种 异常可以改变作用域     第三种 类可以改变作用域
def raise_example():
    try:
        print(11111)
        raise Exception('手动抛出异常')
        print(222)
        name = '小明'
    except:
        print(name)


"""
自定义异常
"""
"""
函数  作用域
"""

if __name__ == '__main__':
    # except_example()
    # except_example1()
    # except_example2()
    raise_example()
    print(11231321)
