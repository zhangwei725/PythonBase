"""
面向过程的产物
2> 作用
    1>  函数体外部能调用函数体内部的局部变量
    2>  保持局部变量不会被回收
3>
    1> 函数嵌套函数
    2> 内部函数引用外部函数的变量
    3> 把内部函数对象当做外部函数的返回值返回
"""


def outer():
    num = 10

    def inner():
        return num

    return inner


nums = []

for i in range(10):
    def add(x):
        print(x + i)


    # 函数对象加入列表
    nums.append(add)

# 1-11 1-10 10个10

for add in nums:
    add(1)

if __name__ == '__main__':
    # inner = outer()
    # num = inner()
    # print(num + 1)
    pass
